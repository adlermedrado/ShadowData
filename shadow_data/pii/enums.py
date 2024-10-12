from enum import Enum


class ModelSize(Enum):
    SMALL = 'sm'
    MEDIUM = 'md'
    LARGE = 'lg'
    TRF = 'trf'


class ModelLang(Enum):
    ENGLISH = 'en'
    PORTUGUESE = 'pt'
    SPANISH = 'es'
    GERMAN = 'de'
    FRENCH = 'fr'


class ModelCore(Enum):
    NEWS = 'core_news'
    WEB = 'core_web'
