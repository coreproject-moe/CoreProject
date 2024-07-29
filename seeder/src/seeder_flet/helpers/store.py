from rx.subject import BehaviorSubject


class Store:
    def __init__(self, initial_value=None):
        self._subject = BehaviorSubject(initial_value)

    def subscribe(self, observer):
        return self._subject.subscribe(observer)

    def get_value(self):
        return self._subject.value

    def set_value(self, new_value):
        self._subject.on_next(new_value)
