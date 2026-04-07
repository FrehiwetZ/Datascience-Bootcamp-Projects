class TestStatEngine(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.engine = StatEngine(self.data)
    
    