##pip install pydantic 

from decimal import Decimal
from pydantic import BaseModel, Field
from enum import Enum
from typing import Generic, List, TypeVar
from typing import Generic, TypeVar


##records
class BookLevel(BaseModel):
    price: Decimal
    quantity: Decimal


class SymbolInfo(BaseModel):
    symbol: str
    status: SymbolStatus


class ExchangeInfoResponse(BaseModel):
    symbols: List[SymbolInfo]


class AveragePrice(BaseModel):
    interval_mins: int
    price: Decimal
    close_time: int


class AveragePriceStream(BaseModel):
    event_type: str
    event_time: str
    symbol: str
    avg_price_interval: int
    average_price: Decimal
    last_trade_time: int


class BookTicker(BaseModel):
    symbol: str
    bid_price: Decimal
    bid_qty: Decimal
    ask_price: Decimal
    ask_qty: Decimal

##class

class TwentyFourHoursPrice(BaseModel):
    symbol: str
    price_change: Decimal
    price_change_percent: Decimal
    weighted_avg_price: Decimal

    last_qty: Decimal

    bid_qty: Decimal
    ask_price: Decimal

    open_price: Decimal
    high_price: Decimal
    low_price: Decimal

    volume: Decimal
    quote_volume: Decimal

    open_time: int
    close_time: int

    first_id: int
    last_id: int
    count: int


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


class BidsToUpdate(BaseModel):
    price: float
    quantity: float


class AsksToUpdate(BaseModel):
    price: float
    quantity: float


class DiffDepthStream(BaseModel):
    event_type: str = Field(alias="e")
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    trade_id: int = Field(alias="t")
    bids_to_update: List[BidsToUpdate] = Field(alias="b")
    asks_to_update: List[AsksToUpdate] = Field(alias="a")
    


class KlineDto(BaseModel):
    event_type: str = Field(alias="e")
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")

    kline: KlinePayloadDto = Field(alias="k")


class KlinePayloadDto(BaseModel):
    start_time: int = Field(alias="t")
    close_time: int = Field(alias="T")
    symbol: str = Field(alias="s")
    interval: str = Field(alias="i")

    open: Decimal = Field(alias="o")
    close: Decimal = Field(alias="c")
    high: Decimal = Field(alias="h")
    low: Decimal = Field(alias="l")

    volume: Decimal = Field(alias="v")

    number_of_trades: int = Field(alias="n")
    is_closed: bool = Field(alias="x")

    quote_volume: Decimal = Field(alias="q")




class IndividualSymbolStream(BaseModel):
    event_type: str = Field(alias="e")
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    price_change: Decimal = Field(alias="p")
    price_change_percent: Decimal = Field(alias="P")
    weighted_avg_price: Decimal = Field(alias="w")
    first_trade_price: Decimal = Field(alias="x")
    last_price: Decimal = Field(alias="c")
    last_quantity: Decimal = Field(alias="Q")
    best_bid_price: Decimal = Field(alias="b")
    best_bid_quantity: Decimal = Field(alias="B")
    best_ask_price: Decimal = Field(alias="a")
    best_ask_quantity: Decimal = Field(alias="A")
    open_price: Decimal = Field(alias="o")
    high_price: Decimal = Field(alias="h")
    low_price: Decimal = Field(alias="l")
    total_traded_base_volume: Decimal = Field(alias="v")
    total_traded_quote_volume: Decimal = Field(alias="q")
    stats_open_time: int = Field(alias="O")
    stats_close_time: int = Field(alias="C")
    first_trade_id: int = Field(alias="F")
    last_trade_id: int = Field(alias="L")
    total_number_of_trades: int = Field(alias="n")
    
class WindowTicker(BaseModel):
    event_type: str = Field(alias="e")
    event_time: int = Field(alias="E")
    symbol: str = Field(alias="s")
    price_change_percent: Decimal = Field(alias="P")
    open_price: Decimal = Field(alias="o")
    high_price: Decimal = Field(alias="h")
    low_price: Decimal = Field(alias="l")
    last_price: Decimal = Field(alias="c")
    weighted_avg_price: Decimal = Field(alias="w")
    total_traded_base_volume: Decimal = Field(alias="v")
    total_traded_quote_volume: Decimal = Field(alias="q")
    stats_open_time: int = Field(alias="O")
    stats_close_time: int = Field(alias="C")
    first_trade_id: int = Field(alias="F")
    last_trade_id: int = Field(alias="L")
    total_number_of_trades: int = Field(alias="n")

class BookTickerStream(BaseModel):
    update_id: int = Field(alias="u")
    symbol: str = Field(alias="s")
    best_bid_price: Decimal = Field(alias="b")
    best_bid_qty: Decimal = Field(alias="B")
    best_ask_price: Decimal = Field(alias="a")
    best_ask_qty: Decimal = Field(alias="A")

class Trade(BaseModel):
    id: str
    price: str
    qty: str
    time: int
    is_buyer_marker: bool
    is_best_match: bool

class RateLimit(BaseModel):
    rate_limit_type: str
    interval: str
    interval_num: str
    limit: int
    count: int


class BinanceStreamResult(BaseModel):
    id: str
    status: int
    result: List[Trade]
    rate_limits: List[RateLimit]

class OrderBook(BaseModel):
    last_update_id: int
    bids: List[BookLevel] = []
    asks: List[BookLevel] = []

class MultipleBookTicker(BaseModel):
    many_book_tickers: List[BookTicker] = Field(default_factory=list)

class MultipleDailyResponse(BaseModel):
    daily_prices_all: List[TwentyFourHoursPrice] = Field(default_factory=list)

class AveragePriceResponse(BaseModel):
    mins: int
    price: str
    close_time: int


class OrderBookResponse(BaseModel):
    last_update_id: int

    bids: List[List[str]] = Field(default_factory=list)
    asks: List[List[str]] = Field(default_factory=list)


class OrderBookStreamResponse(BaseModel):
    event_type: str
    event_time: int
    symbol: str
    first_update_id: int
    final_update_id: int
    bids: List[BookLevel] = Field(default_factory=list)
    asks: List[BookLevel] = Field(default_factory=list)


T = TypeVar("T")

class StreamMessageResponse(BaseModel, Generic[T]):
    stream: str
    data: T

#enums
class SymbolStatus(Str, Enum):
    TRADING = "TRADING",
    HALT = "HALT",
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