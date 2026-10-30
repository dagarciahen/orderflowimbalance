import asyncio
import json
import websockets
import models
from config import BinanceConfig

class BinanceStreamClient:
    def __init__(self, settings: BinanceConfig):
        self.settings = settings
        self.endpoint = settings.endpoint

    async def trade_stream(self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@trade"

        async with websockets.connect(uri) as ws:
            while True:
                message = await ws.recv()
                payload = json.loads(message)
                yield models.TradeStream.model_validate(payload)

    async def average_price_stream(self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@avgPrice"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                avgprice = models.AveragePriceStream.model_validate(json.loads(message))
                yield avgprice

    async def kline_stream(self, symbol: str, interval: str):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@kline_{interval}"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                payload = json.loads(message)
                yield models.KlineDto.model_validate(payload)

    async def partial_depth_stream(self, symbol: str, levels: int = 10, speed_ms: int = 1000):
        suffix = f"@depth{levels}" if speed_ms == 1000 else f"@depth{levels}@100ms"
        uri = f"{self.endpoint}/ws/{symbol.lower()}{suffix}"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                payload = json.loads(message)
                yield models.PartialDepthStream.model_validate(payload)

    async def diff_depth_stream(self, symbol: str, speed_ms: int = 1000):
        suffix = "@depth" if speed_ms == 1000 else "@depth@100ms"
        uri = f"{self.endpoint}/ws/{symbol.lower()}{suffix}"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                payload = json.loads(message)
                yield models.DiffDepthStream.model_validate(payload)

    async def book_ticker_stream(self, symbol: str):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@bookTicker"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                yield models.BookTickerStream.model_validate(json.loads(message))

