from enum import Enum


class ModelSize(Enum):
    SMALL = 'sm'
    MEDIUM = 'md'
    LARGE = 'lg'


class ModelLang(Enum):
    ENGLISH = 'en'
    PORTUGUESE = 'pt'
    SPANISH = 'es'
    GERMAN = 'de'
    FRENCH = 'fr'


class ModelCoreNews(Enum):
    CORE_NEWS = 'core_news'
