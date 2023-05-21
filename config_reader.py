from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    openai_api_key: SecretStr

    # Вложенный класс с дополнительными указаниями для настроек
    class Config:
        # Имя файла, откуда будут прочитаны данные
        env_file = '.env'
        # Кодировка читаемого файла
        env_file_encoding = 'utf-8'


config = Settings()
