import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_vaarin_palauttaa_none(self):
        tulos = self.stats.search("Petteri")
        self.assertEqual(tulos, None)

    def test_search_oikein_palauttaa_statsit(self):
        tulos = self.stats.search("Semenko")
        self.assertEqual(str(tulos), "Semenko EDM 4 + 12 = 16")

    def test_tiimin_pelaajat(self):
        tulos = [str(player) for player in self.stats.team("PIT")]
        self.assertEqual(tulos, ["Lemieux PIT 45 + 54 = 99"])

    def test_top_pelaajien_haku(self):
        tulos = [str(player) for player in self.stats.top(0)]
        print(tulos)
        self.assertEqual(tulos, ["Gretzky EDM 35 + 89 = 124"])