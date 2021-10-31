import unittest

from sys import path as syspath
from os import path as ospath
from pathlib import Path

syspath.append("..")

#syspath.append(Path(ospath.abspath('')).resolve())

import kicad
from kicad import parse_kibot

class TestParseBom(unittest.TestCase):

    def test_parse(self):
        self.assertEqual( parse_kibot.bom_parser('test/files/produkt.xml'), '/foo/bar.sch')
