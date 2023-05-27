ERROR_PLUGIN_QUERY_FAIL = 1003
ERROR_PLUGIN_PARSE_RESULT_FAIL = 1004

PLUGINID = 'com.synology.TMDBExample'
THEMOVIEDB_URL = 'https://api.themoviedb.org/3/'
BANNER_URL = 'https://image.tmdb.org/t/p/w500'
BACKDROP_URL = 'https://image.tmdb.org/t/p/original'
DEFAULT_EXPIRED_TIME = 86400
DEFAULT_LONG_EXPIRED_TIME = 86400 * 30
#TODO: you should assign your own APIKEY here
APIKEY = ""

MOVIE_DATA_TEMPLATE = {
    'title': '',
    'tagline': '',
    'original_available': '',
    'original_title': '',
    'summary': '',
    'certificate': '',
    'genre': [],
    'actor': [],
    'director': [],
    'writer': [],
    'extra': {}
}

"""
movie extra template
    'extra': {
        PLUGINID: {
            'poster': [],
            'backdrop': [],
            'reference': {
                'themoviedb': None,
                'imdb': None
            },
            'rating': {
                'themoviedb': None
            },
            'collection_id': {
                'themoviedb': -1
            }
        }
    }
"""


TVSHOW_DATA_TEMPLATE = {
    'title': '',
    'original_available': '',
    'original_title': '',
    'summary': '',
    'extra': {}
}

"""
tvshow extra template
    'extra': {
        PLUGINID: {
            'poster': [],
            'backdrop': [],
        }
    }
"""


TVSHOW_EPISODE_DATA_TEMPLATE = {
    'title': '',
    'tagline': '',
    'original_available': '',
    'summary': '',
    'certificate': '',
    'genre': [],
    'actor': [],
    'director': [],
    'writer': [],
    'season': -1,
    'episode': -1,
    'extra': {}
}

"""
tvshow_episode extra template
    'extra': {
        PLUGINID: {
            'tvshow': TVSHOW_DATA_TEMPLATE,
            'poster': [],
            'reference': {
                'themoviedb_tv': None,
                'imdb': None
            },
            'rating': {
                'themoviedb_tv': None
            }
        }
    }
"""

MOVIE_SIMILAR_DATA_TEMPLATE = {
    'title': '',
    'id': -1
}
