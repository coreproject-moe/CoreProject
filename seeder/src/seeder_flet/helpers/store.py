import asyncio
from rx.subject import BehaviorSubject


class Store:
    def __init__(self, initial_value):
        self.__subject = BehaviorSubject(initial_value)
        self.__lock = asyncio.Lock()

    def subscribe(self, observer):
        return self.__subject.subscribe(observer)

    def get_value(self):
        return self.__subject.value

    async def async_get_value(self):
        async with self.__lock:
            return self.__subject.value

    def set_value(self, new_value):
        self.__subject.on_next(new_value)

    async def async_set_value(self, new_value):
        async with self.__lock:
            self.__subject.on_next(new_value)
