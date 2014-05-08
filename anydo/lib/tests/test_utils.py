# -*- coding: utf-8 -*-
import unittest
import re
import sys
from anydo.lib import utils


class UtilsTests(unittest.TestCase):
    def setUp(self):
        self.pattern = re.compile('(^([\w-]+)==$)', flags=re.U)

    def test_create_uuid(self):
        self.assertTrue(self.pattern.match(utils.create_uuid()))

    def test_encode_string(self):
        self.assertEqual(utils.encode_string('test'), 'test')
        self.assertEqual(utils.encode_string('1234'), '1234')
        self.assertEqual(utils.encode_string('test1234 Äë'), 'test1234 Äë')

        # "テスト" means "test" in Japansese.
        if sys.version_info < (3, 0):
            word = ('\xe3\x83\x86\xe3\x82\xb9\xe3\x83\x88 123eA'
                    '\xe3\x83\x86\xe3\x82\xb9\xe3\x83\x88')
        else:
            word = 'テスト 123eAテスト'
        self.assertEqual(utils.encode_string('テスト 123eAテスト'), word)
