import unittest
import json
from json_operator import *

funs = {
    "intersection": intersection,
    "subtract": subtract,
    "union": union
}


def read_file(fn):
    with open(fn, "rb") as f:
        data = f.read()
    return data.decode("UTF-8")


class OperatorTest(unittest.TestCase):
    def check_equal(self, fn):
        d = json.loads(read_file(fn))
        left = d["left"]
        right = d["right"]
        self.assertEqual(d["result"], equal(left, right))

    def test_equal(self):
        cases = ["./data/eq1.json",
                 "./data/eq2.json",
                 "./data/eq3.json",
                 "./data/neq1.json",
                 "./data/neq2.json",
                 "./data/neq3.json"]
        for c in cases:
            self.check_equal(c)

    def check_res(self, fn):
        d = json.loads(read_file(fn))
        left = d["left"]
        right = d["right"]
        res = funs[d["op"]](left, right)
        self.assertTrue(equal(res, d["result"]))

    def test_other(self):
        cases = ["./data/inter1.json",
                 "./data/inter2.json",
                 "./data/sub1.json",
                 "./data/uni1.json"]
        for c in cases:
            self.check_res(c)

