from observer_pattern.observer2 import Publisher, Subscriber

pub = Publisher(['lunch', 'cookie'])
bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register('lunch', bob)
pub.register('cookie', alice)
pub.register('lunch', john)

pub.dispatch('lunch', "It's lunch time!")

pub.unregister('lunch', john)
pub.dispatch('cookie', "Another cookie for sale!")

# pub.dispatch(l1)
