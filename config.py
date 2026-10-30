from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class BinanceConfig(BaseSettings):
    endpoint: str = "wss://stream.binance.com:9443"

    symbols: List[str] = Field(default_factory=lambda: ["BTCUSDT", "ETHUSDT"])

    kline_interval: str = "1m"
    depth_levels: int = 10          # 5, 10, 20
    depth_speed_ms: int = 1000      # 1000 o 100

    model_config = SettingsConfigDict(
        env_prefix="BINANCE_",
        env_file=".env",
        extra="ignore",
    )

    @field_validator("symbols", mode="before")
    @classmethod
    def _split_symbols(cls, v):
        if isinstance(v, str):
            return [s.strip().upper() for s in v.split(",") if s.strip()]
        return [s.upper() for s in v]

    @field_validator("kline_interval")
    @classmethod
    def _validate_interval(cls, v: str) -> str:
        allowed = {
            "1s", "1m", "3m", "5m", "15m", "30m",
            "1h", "2h", "4h", "6h", "8h", "12h",
            "1d", "3d", "1w", "1M",
        }
        if v not in allowed:
            raise ValueError(f"kline_interval inválido: {v}. Permitidos: {allowed}")
        return v

    @field_validator("depth_levels")
    @classmethod
    def _validate_levels(cls, v: int) -> int:
        if v not in (5, 10, 20):
            raise ValueError("depth_levels -> 5, 10 o 20")
        return v

    @field_validator("depth_speed_ms")
    @classmethod
    def _validate_speed(cls, v: int) -> int:
        if v not in (100, 1000):
            raise ValueError("depth_speed_ms -> 100 o 1000")
        return v