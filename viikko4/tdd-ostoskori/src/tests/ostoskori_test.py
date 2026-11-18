import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.kananmuna = Tuote("Kananmuna", 5)

    def lisaa_maito(self):
        self.kori.lisaa_tuote(self.maito)

    def lisaa_kaksi_samaa_tuotetta(self):
        self.lisaa_maito()
        self.lisaa_maito()

    def lisaa_kaksi_eri_tuotetta(self):
        self.lisaa_maito()
        self.kori.lisaa_tuote(self.kananmuna)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.lisaa_maito()
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_ostos_korin_hinta_on_yhden_lisatyn_tuotteen_hinta(self):
        self.lisaa_maito()
        self.assertEqual(self.kori.hinta(), 3)

    def test_ostoskorissa_tavaroita_kaksi_kahden_lisäyksen_jalkeen(self):
        self.lisaa_kaksi_eri_tuotetta()
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_ostoskorin_hinta_on_tuotteiden_hintojen_summa(self):
        self.lisaa_kaksi_eri_tuotetta()
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_tavaroita_korissa_kaksi(self):
        self.lisaa_kaksi_samaa_tuotetta()
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisayksen_jalkeen_korin_hinta_kaksi_kertaa_tuotteen_hinta(self):
        self.lisaa_kaksi_samaa_tuotetta()
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        self.lisaa_maito()
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_ostosta(self):
        self.lisaa_kaksi_eri_tuotetta()
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tasan_yksi_ostos(self):
        self.lisaa_kaksi_samaa_tuotetta()
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_ostos_samalla_nimella_ja_lukumaara_yksi(self):
        self.lisaa_maito()
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_tasan_ostos_samalla_nimella_ja_lukumaara_kaksi(self):
        self.lisaa_kaksi_samaa_tuotetta()
        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kahdesta_samasta_tuotteesta_yhden_poistamisen_jalkeen_koriin_jaa_yksi_kappale(self):
        self.lisaa_kaksi_samaa_tuotetta()
        self.kori.poista_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), self.maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_tuotteen_poistamisen_jalkeen_ostoskorissa_ei_ole_tuotteita(self):
        self.lisaa_maito()
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.ostokset(), [])
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        self.lisaa_kaksi_eri_tuotetta()
        self.kori.tyhjenna()
        self.assertEqual(self.kori.ostokset(), [])
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
