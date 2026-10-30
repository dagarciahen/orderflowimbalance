# test_ofi.py
from ofi import event_contribution, mid_price

def test_bid_qty_aumenta():
    prev = {"bid_price": 100.0, "bid_qty": 50.0,
            "ask_price": 101.0, "ask_qty": 40.0}
    curr = {"bid_price": 100.0, "bid_qty": 60.0,
            "ask_price": 101.0, "ask_qty": 40.0}
    assert event_contribution(prev, curr) == 10.0

def test_bid_price_sube():
    prev = {"bid_price": 100.0, "bid_qty": 50.0,
            "ask_price": 101.0, "ask_qty": 40.0}
    curr = {"bid_price": 100.5, "bid_qty": 20.0,
            "ask_price": 101.0, "ask_qty": 40.0}
    assert event_contribution(prev, curr) == 20.0

def test_ask_qty_baja_sube_ofi():
    prev = {"bid_price": 100.0, "bid_qty": 50.0,
            "ask_price": 101.0, "ask_qty": 40.0}
    curr = {"bid_price": 100.0, "bid_qty": 50.0,
            "ask_price": 101.0, "ask_qty": 30.0}
    assert event_contribution(prev, curr) == 10.0

def test_mid_price():
    book = {"bid_price": 100.0, "bid_qty": 1.0,
            "ask_price": 102.0, "ask_qty": 1.0}
    assert mid_price(book) == 101.0