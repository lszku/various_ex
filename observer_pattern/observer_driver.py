from observer_pattern.observer1 import Publisher, Subscriber

pub = Publisher()
bob = Subscriber('Bob')
alice = Subscriber('Alice')

l1 = [1,2,3]

pub.register(bob)
pub.register(alice)

pub.dispatch("It's lunch time!")

pub.unregister(alice)
pub.dispatch("Another cookie for sale!")

pub.dispatch(l1)