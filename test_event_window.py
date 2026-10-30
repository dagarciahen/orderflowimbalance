import pytest
from event_window import EventWindow


def make_book(bp, bq, ap, aq):
    return {"bid_price": bp, "bid_qty": bq, "ask_price": ap, "ask_qty": aq}


def test_deque_descarta_viejo():
    w = EventWindow(maxlen=3)
    w.push(make_book(100, 1, 101, 1))
    w.push(make_book(100, 2, 101, 1))
    w.push(make_book(100, 3, 101, 1))
    w.push(make_book(100, 4, 101, 1))   
    assert len(w) == 3
    assert w.to_list()[0]["bid_qty"] == 2.0


def test_ofi_ventana():
    w = EventWindow(maxlen=10)
    w.push(make_book(100, 50, 101, 40))
    w.push(make_book(100, 60, 101, 40))   # +10
    w.push(make_book(100, 55, 101, 40))   # -5
    w.push(make_book(100, 60, 101, 40))   # +5
    assert w.ofi() == 10.0


def test_ofi_sin_suficientes_eventos():
    w = EventWindow(maxlen=10)
    w.push(make_book(100, 50, 101, 40))
    assert w.ofi() == 0.0
    assert not w.is_ready()


def test_maxlen_invalido():
    with pytest.raises(ValueError):
        EventWindow(maxlen=1)


def test_latest():
    w = EventWindow(maxlen=10)
    assert w.latest() is None
    w.push(make_book(100, 50, 101, 40))
    assert w.latest()["bid_qty"] == 50.0