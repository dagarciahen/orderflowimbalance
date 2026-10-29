from pydantic_settings import BaseSettings

class BinanceConfig(BaseSettings):
    api_ky : str,
    secret_key: str,
    base_url : str = ""

    model_config = {
        ""
    }

