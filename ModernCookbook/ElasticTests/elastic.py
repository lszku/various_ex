from elasticsearch import Elasticsearch

client = Elasticsearch()

playerId = int


class Player(object):
    def __init__(self, id: playerId, name: str, desc: str = None):
        self.id = id
        self.name = name
        self.desc = desc

    def play(self):
        print("Let's play!")

    def __repr__(self):
        return f"Player {self.id}:{self.name}:{self.desc}"

    def __str__(self):
        return f"Player str {self.id}:{self.name}:{self.desc}"

player1 = Player(1,"test1","long desc!")
player1.play()
print(player1)
print(str(player1))