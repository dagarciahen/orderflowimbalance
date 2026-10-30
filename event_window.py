from collections import deque 

from ofi import event_contribution

class EventWindow:
    def __init__(self, maxlen: int):
        if maxlen < 2:
            raise ValueError("at least 2 levels of events")
        self._events: deque[dict] = deque(maxlen=maxlen)
        
    def push(self, event: dict) -> None:
        self._events.append(event)

    def __len__(self) -> int:
        return len(self._events)

    def is_ready(self) -> bool:
        return len(self._events) >= 2

    def ofi(self) -> float:
        if not self.is_ready():
            return 0.0
        suma = 0
        for i in range(1, len(self._events)):
            suma += event_contribution(self._events[i-1], self._events[i])

        return suma

    def latest(self) -> dict | None:
        return self._events[-1] if self._events else None

    def to_list(self) -> list[dict]:
        return list(self._events)

    

    