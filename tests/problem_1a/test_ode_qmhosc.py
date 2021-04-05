import pytest
import itertools
import numpy as np
import scipy

from numpy.testing import assert_almost_equal, assert_equal

from ..tst import get_attribute

FILENAME = "makeup01.py"

N_VALUES = (0, 2, 8)

@pytest.fixture
def parameters():
    p = dict(xmin=0, xmax=6, dx=0.01,
             y0=np.array([1., 0.]), n_values=N_VALUES)
    p['x'] = np.arange(p['xmin'], p['xmax'], p['dx'])
    return p

@pytest.fixture(scope="module")
def ode_qmhosc(module=FILENAME):
    return get_attribute("ode_qmhosc", module)

class TestODE:
    def test_integration_returnvalue(self, ode_qmhosc, parameters):
        y = ode_qmhosc(parameters['x'], parameters['y0'][0], parameters['y0'][1], 0)
        assert_equal(len(y), 2,
                     err_msg="ode_qmhosc() function should return (2, len(x)) array")

    def test_integration_range(self, ode_qmhosc, parameters):
        y = ode_qmhosc(parameters['x'], parameters['y0'][0], parameters['y0'][1], 0)
        assert_equal(len(y[0]), len(parameters['x']),
                     err_msg="different number of x values (0 <= x < 6, dx=0.01)")

    @pytest.mark.parametrize("n", N_VALUES)
    def test_ode_qmhosc_x0_behavior(self, ode_qmhosc, parameters, n, ix=0, decimal=6):
        y = ode_qmhosc(parameters['x'], parameters['y0'][0], parameters['y0'][1], n)
        assert_almost_equal(y[:, ix], parameters['y0'], decimal=decimal)

    @pytest.mark.parametrize("n,ix",
                             [(n, ix) for n, ix in
                              itertools.zip_longest(N_VALUES, (-200, -100),
                                                    fillvalue=-1)])
    def test_ode_qmhosc_large_x_behavior(self, ode_qmhosc, parameters, n, ix, decimal=2):
        y = ode_qmhosc(parameters['x'], parameters['y0'][0], parameters['y0'][1], n)
        assert_almost_equal(y[:, ix], [0, 0], decimal=2)

    @pytest.mark.parametrize("n,value,ix",
                             [(n, value, ix) for n, value, ix in
                              zip(N_VALUES,
                                  (0.44311342242174678, 0.8862267907458522, 1.6205289343075246),
                                  (-150, -100, -1))])
    def test_ode_qmhosc_integral(self, ode_qmhosc, parameters, n, value, ix, decimal=5):
        y = ode_qmhosc(parameters['x'], parameters['y0'][0], parameters['y0'][1], n)
        psi = y[0, :ix]
        norm = 0.5 * scipy.integrate.simps(psi**2, x=parameters['x'][:ix])
        assert_almost_equal(norm, value, decimal=decimal)
