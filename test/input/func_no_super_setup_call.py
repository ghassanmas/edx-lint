"""A TestCase class that doesn't call super setUp."""

import unittest

# pylint: disable=too-few-public-methods, missing-docstring

class BadTestCase(unittest.TestCase):
    def setUp(self):
        self.i_am_bad = True
