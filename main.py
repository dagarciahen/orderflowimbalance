import asyncio

from config import BinanceConfig
from binancestreamapi import BinanceStreamClient
from ofistream import OFIStream


async def main():
    settings = BinanceConfig()
    client = BinanceStreamClient(settings)
    stream = OFIStream(client, symbol="BTCUSDT", interval=2.0)

    async for row in stream.run():
        print(
            f"OFI={row['ofi']:+12.4f}   "
            f"mid={row['mid']:10.2f}   "
            f"eventos={row['n_events']:3d}"
        )


if __name__ == "__main__":
    asyncio.run(main())