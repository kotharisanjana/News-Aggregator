
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
countries_initial = {'ae':'United Arab Emirates', 'ar':'Argentina', 'at':'Austria', 'au':'Australia', 'be':'Belgium', 'bg':'Bulgaria', 'br':'Brazil',
            'ca':'Canada', 'ch':'Switzerland', 'cn':'China', 'co':'Colombia', 'cu':'Cuba', 'cz':'Czech Republic', 'de':'Germany', 'eg':'Egypt',
            'fr':'France', 'gb':'United Kingdom', 'gr':'Greece', 'hk':'Hong Kong', 'hu':'Hungary', 'id':'Indonesia', 'ie':'Ireland', 'il':'Israel',
            'in':'India', 'it':'Italy', 'jp':'Japan', 'kr':'South Korea', 'lt':'Lithuania', 'lv':'Latvia', 'ma':'Morocco', 'mx':'Mexico', 'my':'Malaysia',
            'ng':'Nigeria', 'nl':'Netherlands', 'no':'Norway', 'nz':'New Zealand', 'pk':'Pakistan', 'ph':'Philippines', 'pl':'Poland', 'pt':'Portugal',
            'ro':'Romania','rs':'Serbia', 'ru':'Russia', 'sa':'Saudi Arabia', 'se':'Sweden', 'sg':'Singapore', 'si':'Slovenia', 'sk':'Slovakia', 'th':'Thailand',
            'tr':'Turkey', 'tw':'Taiwan', 'ua':'Ukraine', 'us':'United States', 've':'Venezuela', 'za':'South Africa'}
languages_initial = {'ar':'Arabic', 'de':'German', 'en':'English', 'es':'Spanish', 'fr':'French', 'he':'Hebrew', 'it':'Italian', 'nl':'Dutch', 'no':'Norwegian',
            'pt':'Portuguese', 'ru':'Russian', 'se':'Swedish', 'ud':'Pakistani', 'zh':'Chinese'}
countries = dict(sorted(countries_initial.items(), key=lambda kv:(kv[1], kv[0])))
languages = dict(sorted(languages_initial.items(), key=lambda kv:(kv[1], kv[0])))