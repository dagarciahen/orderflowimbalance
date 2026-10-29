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
        uri = f"{self.endpoint}/ws/{symbol.lower()}@depth"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                avgprice = models.AveragePriceStream.model_validate(json.loads(message))
                yield avgprice

    async def order_book_stream(self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@depth"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                orderbook = models.OrderBookStreamResponse.model_validate(json.loads(message))
                yield orderbook


    async def kine_stream(self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@depth"
        async with websockets.connect(uri) as ws:
            async for message in ws:
        pass

    async def partial_depth_stream(Self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@depth"
        async with websockets.connect(uri) as ws:
            async for message in ws:
        pass

    async def diff_depth_stream(self, symbol):
        uri = f"{self.endpoint}/ws/{symbol.lower()}@depth"
        async with websockets.connect(uri) as ws:
            async for message in ws:
                diffdepth = models.DiffDepthStream.model_validate(json.loads(message))
                yield diffdepth

                
