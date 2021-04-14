# -*- coding: utf-8 -*-
# ASSIGNMENT: Makeup 01
# PROBLEM NUMBER: 1a

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_imagefile

FILENAME = 'qmhosc.png'
POINTS = 6

def test_plot_even_n():
    return _test_imagefile(FILENAME)


