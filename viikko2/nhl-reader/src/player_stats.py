from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []
        for p in self.reader.players:
            if p.nationality == nationality:
                players.append(p)
        return players

    