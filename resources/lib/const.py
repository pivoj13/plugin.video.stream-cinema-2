class GENERAL:
    PLUGIN_ID = 'plugin.video.stream-cinema-2'


class FILTER_TYPE:
    TITLE_OR_ACTOR = 'titleOrActor'
    STARTS_WITH_LETTER = 'startsWithL'
    STARTS_WITH = 'startsWith'
    GENRE = 'genre'


class COLLECTION:
    TV_SHOWS = 'tvshows'
    MOVIES = 'movies'
    DIRECTORIES = 'directories'


class RENDERER:
    TV_SHOWS = COLLECTION.TV_SHOWS
    MOVIES = COLLECTION.MOVIES
    DIRECTORIES = 'directories'


class ENDPOINT:
    MEDIA = 'media'
    COLLECTION = MEDIA + '/<collection>'
    FILTER = COLLECTION + '/filter/<filter_name>/<filter_value>'
    MEDIA_PLAYED = COLLECTION + '/<media_id>/played'
    TV_SHOW_PLAYED = COLLECTION + '/<media_id>/<season>/<episode>/played'
    POPULAR = COLLECTION + '/popular/-1'


class PROTOCOL:
    PLUGIN = 'plugin'


class REGEX:
    ROUTER_PARAMS = r"<.*?>"


class ROUTE:
    A_TO_Z = '/a_to_z/<collection>'
    SHOW_CACHED_MEDIA = '/show_cached_media/<collection>'
    NEXT_PAGE = '/next_page/<collection>/<url>'
    FILTER = '/filter/<collection>/<filter_type>/<filter_value>'
    SEARCH = '/search/<collection>'
    COMMAND = '/command/<what>'
    MEDIA_MENU = '/media/<collection>'
    MAIN_MENU = '/main_menu'
    GENRE_MENU = '/genre_menu/<collection>'
    SEARCH_RESULT = '/search_result/<collection>/<search_value>'
    SELECT_STREAM = '/select_stream/<media_id>'
    PLAY_STREAM = '/play_stream/<ident>'
    SELECT_SEASON = '/select_season/<media_id>'
    SELECT_EPISODE = '/select_episode/<media_id>/<season_id>'
    SELECT_TV_SHOW_STREAM = '/select_tv_show_stream/<media_id>/<season_id>/<episode_id>'
    POPULAR = MEDIA_MENU + '/popular'


class URL:
    API = 'http://beta.plugin.sc2.zone/api'


class COMMAND:
    SEARCH = 'search'
    OPEN_SETTINGS = 'open-settings'


class STORAGE:
    COLLECTION = 'collection'
    MEDIA_LIST = 'media_list'
    PLUGIN_URL_HISTORY = 'plugin_url_history'
    PLUGIN_LAST_URL_ADDED = 'plugin_last_url_added'
    SELECTED_MEDIA_ID = 'selected_media_id'
    SERVICE = 'service'


class SERVICE:
    PLAYER_SERVICE = 'player_service'


class SERVICE_EVENT:
    PLAYBACK_STARTED = 'playback_started'


class CACHE:
    EXPIRATION_TIME = 10
    PLUGIN_URL_HISTORY_LIMIT = 5


class DOWNLOAD_TYPE:
    VIDEO_STREAM = 'video_stream'
    FILE_DOWNLOAD = 'file_download'


class SETTINGS:
    UUID = 'uuid'
    DEBUG = 'debug'
    PROVIDER_NAME = 'provider.name'
    PROVIDER_USERNAME = 'provider.username'
    PROVIDER_PASSWORD = 'provider.password'
    PROVIDER_TOKEN = 'provider.token'
    EXPLICIT_CONTENT = 'explicit_content'


class STRINGS:
    STREAM_TITLE_BRACKETS = '[{}]'
    SEASON_TITLE = '{} {}'
    BOLD = '[B]{}[/B]'
    TABLE_SPACES = '  '


class LANG:
    GENERAL = 30010
    SOURCE = 30011
    USERNAME = 30101
    PASSWORD = 30102
    PROVIDER = 30103
    WEBSHARE_CZ = 30104
    DEBUG = 30105
    MOVIES = 30200
    SERIES = 30201
    MAIN_MENU = 30202
    NEXT_PAGE = 30203
    SEARCH = 30204
    SEARCH_MEDIA = 30207
    SETTINGS = 30208
    GENRE = 30209
    A_Z = 30211
    POPULAR = 30211
    WATCHING_NOW = 30212
    ACTION = 30213
    ANIMATED = 30214
    ADVENTURE = 30215
    DOCUMENTARY = 30216
    DRAMA = 30217
    EROTIC = 30218
    FANTASY = 30219
    HISTORICAL = 30220
    HORROR = 30221
    MUSIC = 30222
    IMAX = 30223
    CATASTROPHIC = 30224
    COMEDY = 30225
    SHORT = 30226
    CRIME = 30227
    MUSICAL = 30228
    MYSTERIOUS = 30229
    EDUCATIONAL = 30230
    FAIRYTALE = 30231
    PORNOGRAPHIC = 30232
    PSYCHOLOGICAL = 30233
    JOURNALISTIC = 30234
    REALITY = 30235
    TRAVEL = 30236
    FAMILY = 30237
    ROMANTIC = 30238
    SCI_FI = 30239
    COMPETITION = 30240
    SPORTS = 30241
    STAND_UP = 30242
    TALK_SHOW = 30243
    TELENOVELA = 30244
    THRILLER = 30245
    MILITARY = 30246
    WESTERN = 30247
    BIOGRAPHICAL = 30248
    SELECT_A_MEDIA_SOURCE = 30250
    _0_9 = 30251
    SEASON = 30920
    EPISODE = 30921
    MISSING_PROVIDER_CREDENTIALS = 30300
    SERVER_ERROR = 30301
    NOTHING_FOUND = 30302
    FOUND__NUM__RECORDS = 30303
    ACTIVATE_VIP = 30304


api_genres = {
    LANG.EROTIC: 'Erotic',
    LANG.PORNOGRAPHIC: 'Pornographic',
    LANG.ACTION: 'Action',
    LANG.ANIMATED: 'Animated',
    LANG.ADVENTURE: 'Adventure',
    LANG.BIOGRAPHICAL: 'Biographical',
    LANG.CATASTROPHIC: 'Catastrophic',
    LANG.COMEDY: 'Comedy',
    LANG.COMPETITION: 'Competition',
    LANG.CRIME: 'Crime',
    LANG.DOCUMENTARY: 'Documentary',
    LANG.FAIRYTALE: 'Fairytale',
    LANG.DRAMA: 'Drama',
    LANG.FAMILY: 'Family',
    LANG.FANTASY: 'Fantasy',
    LANG.HISTORICAL: 'Historical',
    LANG.HORROR: 'Horror',
    LANG.IMAX: 'IMAX',
    LANG.EDUCATIONAL: 'Educational',
    LANG.MUSIC: 'Music',
    LANG.JOURNALISTIC: 'Journalistic',
    LANG.MILITARY: 'Military',
    LANG.MUSICAL: 'Musical',
    LANG.MYSTERIOUS: 'Mysterious',
    LANG.PSYCHOLOGICAL: 'Psychological',
    LANG.REALITY: 'Reality',
    LANG.ROMANTIC: 'Romantic',
    LANG.SCI_FI: 'Sci-Fi',
    LANG.SHORT: 'Short',
    LANG.SPORTS: 'Sports',
    LANG.STAND_UP: 'Stand-Up',
    LANG.TALK_SHOW: 'Talk-Show',
    LANG.TELENOVELA: 'Telenovela',
    LANG.THRILLER: 'Thriller',
    LANG.TRAVEL: 'Travel',
    LANG.WESTERN: 'Western'
}

explicit_genres = [LANG.EROTIC, LANG.PORNOGRAPHIC]
