import unittest
from types import SimpleNamespace

from player_stats import PlayerStats


class StubPlayerReader:
    def __init__(self, players):
        self.players = players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        self.players = [
            SimpleNamespace(
                name="Alex",
                nationality="FIN",
                team="AAA",
                goals=10,
                assists=20,
                points=30,
            ),
            SimpleNamespace(
                name="Blake",
                nationality="CAN",
                team="AAA",
                goals=15,
                assists=5,
                points=20,
            ),
            SimpleNamespace(
                name="Casey",
                nationality="FIN",
                team="BBB",
                goals=25,
                assists=10,
                points=35,
            ),
        ]
        self.stats = PlayerStats(StubPlayerReader(self.players))

    def test_top_scorers_by_nationality_returns_matching_players(self):
        result = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["Alex", "Casey"], [player.name for player in result])

    def test_top_scorers_by_nationality_returns_empty_list_when_no_match(self):
        result = self.stats.top_scorers_by_nationality("SWE")

        self.assertEqual([], result)

    def test_top_scorers_by_team_orders_players_by_points_descending(self):
        result = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(["Alex", "Blake"], [player.name for player in result])

    def test_top_scorers_by_team_returns_empty_list_when_team_not_found(self):
        result = self.stats.top_scorers_by_team("CCC")

        self.assertEqual([], result)

    def test_top_goal_scorers_returns_requested_number_in_descending_order(self):
        result = self.stats.top_goal_scorers(2)

        self.assertEqual(["Casey", "Blake"], [player.name for player in result])

    def test_top_goal_scorers_returns_all_players_when_limit_is_larger(self):
        result = self.stats.top_goal_scorers(10)

        self.assertEqual(["Casey", "Blake", "Alex"], [player.name for player in result])


if __name__ == "__main__":
    unittest.main()
