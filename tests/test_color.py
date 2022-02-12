import unittest
from requests import post


BACKEND_URL = 'http://localhost:8000/'


class TestColor(unittest.TestCase):
    def test_no_hex(self):
        url = BACKEND_URL + 'color'
        request = post(url, json={'color': '#FF0000'})
        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.json(), {'detail': 'didnt receive hex color'})

    def test_good_hex(self):
        url = BACKEND_URL + 'color'
        request = post(url, json={'hex': '#FF0000'})
        if request.status_code == 500:
            # pixel not working
            self.assertEqual(request.json(), {'detail': 'pixel problem'})
        else:
            self.assertEqual(request.status_code, 200)
            self.assertEqual(request.json(), {'detail': 'success'})
            
    def test_bad_hex(self):
        url = BACKEND_URL + 'color'
        request = post(url, json={'hex': '#FFF0000V'})
        self.assertEqual(request.status_code, 400)
        self.assertEqual(request.json(), {'detail': 'wrong hex color'})


if __name__ == '__main__':
    unittest.main()
