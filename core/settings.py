from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    APP_NAME:str='Prism — Financial Intelligence Platform'
    CACHE_TTL:int=300
    DEFAULT_THEME:str='dark'
settings=Settings()
