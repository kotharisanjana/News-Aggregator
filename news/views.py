# Create your views here.
from django.shortcuts import render
from newsapi import NewsApiClient
from django.contrib import messages
import datetime
from .staticdata import *
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='')

sources = {}
category_to_sources = {}
country_to_sources = {}

def top_headlines(request):
    query = category = country = None
    if 'querysearch' in request.GET:
        query = request.GET['querysearch']
    if 'category' in request.GET:
        category = request.GET['category']
    if 'country' in request.GET:
        country = request.GET['country']

    top_news = newsapi.get_top_headlines(q=query, country=country, category=category)
    headlines_list = top_news['articles']

    news_title = []
    url = []
    news_source = []

    for article in headlines_list:
        news_title.append(article['title'])
        news_source.append(article['source']['name'])
        url.append(article['url'])

    display_list = zip(news_title, news_source, url)
        
    context = {
        'display_list' : display_list,
        'category_choices' : categories,
        'country_choices' : countries,
    }
    return render(request, 'news/topheadlines.html', context)


def categorywise_news(request):
    get_from_sources_api()

    lang = 'en'
    final_category_list = [[]]
    if 'language' in request.GET:
        lang = request.GET['language']

    for key,value in category_to_sources.items():
        s = ','.join(value)
        cat_news = newsapi.get_everything(language=lang, sort_by='popularity', sources=s, from_param=datetime.date.today()-datetime.timedelta(1), 
                                            to=datetime.date.today())
        if len(cat_news['articles'])==0:
            continue

        cat_news_list = cat_news['articles']
        if len(cat_news_list)>6:
            upperlimit = 6
        else:
            upperlimit = len(cat_news_list) 

        news_title = []
        img = []
        description = []
        url = []
        news_source = []

        for i in range(upperlimit):
            articles = cat_news_list[i]
            news_title.append(articles['title'])
            news_source.append(articles['source']['name'])
            img.append(articles['urlToImage'])
            description.append(articles['description'])
            url.append(articles['url'])
        cat_list = zip(news_title, news_source, img, description, url)
        final_category_list.append([key.upper(),cat_list])
    del final_category_list[0]

    context = {
        'category_wise_list' : final_category_list,
        'country_choices' : countries,
        'source_choices' : sources,
        'language_choices': languages
    }

    if len(final_category_list)==0:
        messages.error(request, "News in the chosen language is not currently available")
        return render(request, 'news/categorynews.html', context)

    return render(request, 'news/categorynews.html', context)

def search(request):
    search = country = s = None
    sources_selected = []
    news_title = []
    img = []
    description = []
    url = []
    news_source = []
    page_size = 100

    if 'search' in request.GET:
        search = request.GET['search']
    if 'country' in request.GET:
        country = request.GET['country']
    if 'sources' in request.GET:
        sources_selected = request.GET.getlist('sources')
    
    if ((not search) and (not country) and (not sources_selected)):
        messages.error(request, 'Please be specific in your search.')
        return render(request, 'news/search.html')
    else:
        if country and sources_selected:
            if country in country_to_sources:
                common_sources = list(set(country_to_sources.get(country)) & set(sources_selected))
                s = ','.join(common_sources)
            if not s:
                messages.error(request, 'This news source is not available in the selected country.')
                return render(request, 'news/search.html')  
        elif country and (not sources_selected):
            s_value = country_to_sources.get(country)
            if s_value:
                s = ','.join(s_value)
            else:
                if search:
                    messages.error(request,"No news is available from this country for the searched keyword. Please try again!")
                else:
                    messages.error(request, 'No news is available from this country at the moment')
                return render(request, 'news/search.html')
        elif (not country) and sources_selected:
            if sources_selected:
                s = ','.join(sources_selected)
            else:
                if search:
                    messages.error(request, 'No news is available from this source for the searched keyword. Please try again!')
                else:
                    messages.error(request, 'No news is available from this source at the moment.')
                return render(request, 'news/search.html')
        full_news = newsapi.get_everything(q=search, sources=s, page_size=page_size)
        if len(full_news['articles'])==0: 
            messages.error(request, "This combination of inputs is invalid. Please try again!")
            return render(request, 'news/search.html')

    articles_list = full_news['articles']
    for i in range(len(articles_list)):
        articles = articles_list[i]
        news_title.append(articles['title'])
        news_source.append(articles['source']['name'])
        img.append(articles['urlToImage'])
        description.append(articles['description'])
        url.append(articles['url'])
    display_list = zip(news_title, news_source, img, description, url)

    context = {
        'display_list' : display_list,
    }
    return render(request, 'news/search.html', context)

def get_from_sources_api():
    sources_list_all = newsapi.get_sources()
    sources_list = sources_list_all['sources']

    for i in range(len(sources_list)):
        source = sources_list[i]
        if source['country'] in country_to_sources:
            country_to_sources[source['country']].append(source['id'])
        else:
            country_to_sources[source['country']] = []
            country_to_sources[source['country']].append(source['id'])
        sources[source['id']] = source['name']

        if source['category'] in category_to_sources:
            category_to_sources[source['category']].append(source['id'])
        else:
            category_to_sources[source['category']] = []
            category_to_sources[source['category']].append(source['id'])