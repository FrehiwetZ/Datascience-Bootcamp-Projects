class TestStatEngine( unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.engine = StatEngine(self.data)
    
    def test_mean(self):
        self.assertEqual(self.engine.get_mean(), 3)

    def test_median(self):
        self.assertEqual(self.engine.get_median(), 3)

    def test_mode(self):
        self.assertEqual(self.engine.get_mode(), "No mode")
    
    def test_variance(self):
        self.assertAlmostEqual(self.engine.get_varience(), 2.5)

