class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("""{} got message "{}" """.format(self.name, message))


class Publisher:
    def __init__(self, events: list):
        self.subscribers = {event: dict() for event in events}

    def register(self, event, who, callback=None):
        if not callback:
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self,event, message: str):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)

    def get_subscribers(self, event):
        return self.subscribers[event]
