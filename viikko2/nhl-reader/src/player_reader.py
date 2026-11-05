import requests
from player import Player
class PlayerReader:
    def __init__(self, url):
        response = requests.get(url, timeout=30).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        self.players = sorted(players, key=lambda x: x.points, reverse=True)
