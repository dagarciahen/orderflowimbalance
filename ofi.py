def event_contribution(prev: dict, curr: dict) -> float:

    if curr["bid_price"] > prev["bid_price"]:
        e_bid = curr["bid_qty"]
    elif curr["bid_price"] < prev["bid_price"]:
        e_bid = -prev["bid_qty"]
    else:
        e_bid = curr["bid_qty"] - prev["bid_qty"]

    if curr["ask_price"] < prev["ask_price"]:
        e_ask = -curr["ask_qty"]
    elif curr["ask_price"] > prev["ask_price"]:
        e_ask = prev["ask_qty"]
    else:
        e_ask = prev["ask_qty"] - curr["ask_qty"]
    return e_bid + e_ask

def mid_price(book: dict) -> float:
    return (book["bid_price"] + book["ask_price"])/2.0
