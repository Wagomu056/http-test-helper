# -*- coding: utf-8 -*-

import unittest
import time
import threading
import httptesthelper
import json

bodyJson = None

def http_callback(requestBody):
    global bodyJson
    bodyJson = json.loads(requestBody)
    print(bodyJson)

class UnitTest(unittest.TestCase):
    def setUp(self):
        global bodyJson
        bodyJson = None

    def test1(self):
        print("start test1")
        while (bodyJson == None):
            time.sleep(0.5)

        # curl -i 'http://localhost:8000' -d '{"NAME":"TAKUYA","SIZE":"M","AGE":35}'
        self.assertTrue("NAME" in bodyJson)
        self.assertEqual(bodyJson["NAME"], "TAKUYA")

        self.assertTrue("SIZE" in bodyJson)
        self.assertEqual(bodyJson["SIZE"], "M")

        self.assertTrue("AGE" in bodyJson)
        self.assertEqual(bodyJson["AGE"], 35)

def start_test():
    unittest.main()

if __name__ == '__main__':
    thread2 = threading.Thread(target=start_test)
    thread2.start()

    port = 8000
    httptesthelper.start_server(port, http_callback)
