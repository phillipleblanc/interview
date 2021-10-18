import unittest
import requests
from requests.models import Response


class MainTestCase(unittest.TestCase):
    def setUp(self):
        try:
            requests.get("http://localhost:5000/health")
            requests.post("http://localhost:5000/clear")
        except:
            print("Unable to connect to the API, is it running?")
            raise Exception("Unable to connect to the API, is it running?")

    def test_send_json_data(self):
        response = send_data("./tests/data.json", "application/json")
        self.assertEqual(200, response.status_code)

    def test_get_empty_data(self):
        headers = {"Accept": "application/json"}
        r = requests.get("http://localhost:5000/data", headers=headers)
        self.assertEqual(200, r.status_code)

        json_data = r.json()
        self.assertTrue(len(json_data) == 0)

    def test_send_and_get_json_data(self):
        response = send_data("./tests/data.json", "application/json")
        self.assertEqual(200, response.status_code)

        headers = {"Accept": "application/json"}
        r = requests.get("http://localhost:5000/data", headers=headers)
        self.assertEqual(200, r.status_code)

        json_data = r.json()
        self.assertTrue(len(json_data) == 32)
        firstRecord = json_data[0]
        self.assertEqual("1972-07-12T16:57:49.935Z", firstRecord["time"])
        self.assertEqual("Garnet", firstRecord["city"])
        self.assertEqual(8367726, firstRecord["population"])
        self.assertEqual(-47.97173, firstRecord["latitude"])
        self.assertEqual(77.69925, firstRecord["longitude"])

        if "country" in firstRecord:
            self.fail("unexpected field 'country' in record")

def send_data(filename, contentType) -> Response:
    with open(filename, "r") as f:
        data = f.read()
        headers = {"Content-Type": contentType}
        response = requests.post("http://localhost:5000/data", data, headers=headers)
        return response


if __name__ == "__main__":
    unittest.main()
