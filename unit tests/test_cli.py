import unittest
import cli

class TestCLI(unittest.TestCase):

    def test_get_data_default(self):
        data = cli.get_data()
        self.assertEqual(data['quote'], cli.DEFAULT_QUOTE)
        self.assertIsNone(data['image_url'])

    def test_get_data_with_grayscale(self):
        data = cli.get_data(grayscale=True)
        self.assertEqual(data['quote'], cli.DEFAULT_QUOTE)
        self.assertEqual(data['image_url'], 'http://testimage.com/test.jpg')

    def test_get_data_key_invalid(self):
        # Simulate that an invalid key does not affect the output
        data = cli.get_data(key='invalid')
        self.assertEqual(data['quote'], cli.DEFAULT_QUOTE)
        self.assertIsNone(data['image_url'])

    def test_get_data_key_too_long(self):
        # Simulate that a too-long key does not affect the output
        data = cli.get_data(key='1234567')
        self.assertEqual(data['quote'], cli.DEFAULT_QUOTE)
        self.assertIsNone(data['image_url'])

if __name__ == '__main__':
    unittest.main()
