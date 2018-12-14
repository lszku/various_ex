class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("""{} got message "{}" """.format(self.name, message))


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who: Subscriber):
        self.subscribers.add(who)

    def unregister(self, who: Subscriber):
        self.subscribers.remove(who)

    def dispatch(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)
