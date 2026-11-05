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

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = [player for player in self.reader.players if player.team == team]
        return sorted(players, key=lambda player: player.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(self.reader.players, key=lambda player: player.goals, reverse=True)[:how_many]
