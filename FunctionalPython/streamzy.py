from streamz import Stream

source = Stream()

a = source.map(lambda x: x + 1).sink(print)

print(dir(a))
# print(a.visualize(rankdir='LR'))

