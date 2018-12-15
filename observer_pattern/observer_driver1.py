from observer_pattern.observer1 import Publisher, SubscriberOne, SubscriberTwo

pub = Publisher()
bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john = SubscriberOne('John')

l1 = [1,2,3]

pub.register(bob, bob.update)
pub.register(alice, alice.receive)
pub.register(john)

pub.dispatch("It's lunch time!")

pub.unregister(john)
pub.dispatch("Another cookie for sale!")

# pub.dispatch(l1)