import unittest

from sys import path as syspath
from os import path as ospath
from pathlib import Path

syspath.append("..")

#syspath.append(Path(ospath.abspath('')).resolve())

from kicad.pcb_tool import create_gerbers

class TestParseFiles(unittest.TestCase):

    def test_create_gerbers(self):
        create_gerbers('example/shifter/shifter.kicad_pcb', 'gerbers', 'gerbers.zip')
