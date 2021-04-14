# -*- coding: utf-8 -*-
# ASSIGNMENT: Makeup 01
# PROBLEM NUMBER: 1a

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'makeup01.py'
POINTS = 8

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[0.0, [1.0, 0.0], 0.5], [0.0, [1.0, 0.0], 2.5], [2.5, [1.0, 0.0], 8.5], [0.0, [0, 1.0], 1.5], [0.0, [0.0, 1.0], 3.5], [1.5, [0.0, 1.0], 3.5]], [{}, {}, {}, {}, {}, {}], [[0, -1.0], [0, -5.0], [0, -10.75], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0]])))
def test_f_qmhosc(args, kwargs, reference):
    return _test_function("f_qmhosc",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )

