import asyncio
from rx.subject import BehaviorSubject


class Store:
    def __init__(self, initial_value):
        self._subject = BehaviorSubject(initial_value)
        self._lock = asyncio.Lock()

    def subscribe(self, observer):
        return self._subject.subscribe(observer)

    def get_value(self):
        return self._subject.value

    async def async_get_value(self):
        async with self._lock:
            return self._subject.value

    def set_value(self, new_value):
        self._subject.on_next(new_value)

    async def async_set_value(self, new_value):
        async with self._lock:
            self._subject.on_next(new_value)
