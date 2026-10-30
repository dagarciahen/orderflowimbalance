from decimal import Decimal
from pydantic import BaseModel, Field
from enum import Enum
from typing import Generic, List, TypeVar, Optional


class SymbolStatus(str, Enum):
    TRADING = "TRADING"
    HALT = "HALT"
    BREAK = "BREAK"


class KlineInterval(str, Enum):
    ONE_SECOND = "1s"
    ONE_MINUTE = "1m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    TWELVE_HOURS = "12h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


class BookLevel(BaseModel):
    price: Decimal
    quantity: Decimal

    @classmethod
    def from_list(cls, values: List[str]) -> "BookLevel":
        return cls(price=Decimal(values[0]), quantity=Decimal(values[1]))


class TradeStream(BaseModel):
    event_type: str = Field(alias="e")
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    trade_id: int = Field(alias="t")
    price: Decimal = Field(alias="p")
    quantity: Decimal = Field(alias="q")
    trade_time: int = Field(alias="T")
    buyer_maker: bool = Field(alias="m")
    ignore: bool = Field(alias="M")


class AveragePriceStream(BaseModel):
    event_type: str = Field(alias="e")          # "avgPrice"
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    avg_price_interval: str = Field(alias="i")  # "5m"
    average_price: Decimal = Field(alias="w")
    last_trade_time: int = Field(alias="T")


class BookTickerStream(BaseModel):
    update_id: int = Field(alias="u")
    symbol: str = Field(alias="s")
    best_bid_price: Decimal = Field(alias="b")
    best_bid_qty: Decimal = Field(alias="B")
    best_ask_price: Decimal = Field(alias="a")
    best_ask_qty: Decimal = Field(alias="A")


class DiffDepthStream(BaseModel):
    event_type: str = Field(alias="e")     # "depthUpdate"
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    first_update_id: int = Field(alias="U")
    final_update_id: int = Field(alias="u")
    bids_to_update: List[List[str]] = Field(alias="b")
    asks_to_update: List[List[str]] = Field(alias="a")


class PartialDepthStream(BaseModel):
    last_update_id: int = Field(alias="lastUpdateId")
    bids: List[List[str]] = Field(alias="bids")
    asks: List[List[str]] = Field(alias="asks")


T = TypeVar("T")


class StreamMessageResponse(BaseModel, Generic[T]):
    stream: str
    data: T