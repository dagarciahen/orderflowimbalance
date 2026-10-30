import time
from models import BookTickerStream
from binancestreamapi import BinanceStreamClient
from ofi import event_contribution, mid_price


class OFIStream:
    ##todo get settings from json or config configurable
    def __init__(self, client: BinanceStreamClient, symbol: str, interval: float = 2.0):
        self.client = client
        self.symbol = symbol
        self.interval = interval 

    @staticmethod #pongo static pq necesito instanciarlo sin los atributos de la clase
    def _to_dict(bt: BookTickerStream) -> dict:
        return {
            "bid_price": float(bt.best_bid_price),
            "bid_qty" : float(bt.best_bid_qty),
            "ask_price" : float(bt.best_ask_price),
            "ask_qty" : float(bt.best_ask_qty)
        }
    
    async def run(self):
        prev = None
        ofi_acc = 0.0
        n_events = 0
        last_mid = None
        window_start = time.time()

        async for bt in self.client.book_ticker_stream(self.symbol):
            curr = self._to_dict(bt)
            if prev is not None:
                ofi_acc += event_contribution(prev, curr)
                n_events +=1

            prev = curr
            last_mid = mid_price(Curr)

            if time.time() - window_start >= self.interval:
                if n_events > 0:
                    yield {
                        "timestamp" : window_start,
                        "ofi" : ofi_acc,
                        "mid" : last_mid,
                        "n_events": n_events,
                    }

                ofi_acc = 0.0
                n_events = 0
                window_start = 0
                window_start = time.time()

    