from newton import InterpoladorNewton
from scipy.interpolate import interp1d
import unittest
import numpy as np

class TestInterpoladorNewton(unittest.TestCase):
    def test_basic_interpolation(self):
        # Test basic interpolation with known data
        x = [1, 4, 5, 6]
        y = [0, 1.386294, 1.609438, 1.791759]
        interpolator = InterpoladorNewton(x, y)
        interpolator.calculaParametros()
        result = interpolator.estimar(2)

        # Create an interpolation function using Newton interpolation
        newton_interpolator = interp1d(x, y, kind='cubic')  # 'cubic' indicates Newton interpolation

        # Evaluate the interpolation function at a specific point
        result2 = newton_interpolator(2)

        self.assertAlmostEqual(result, result2, places=5)  # Adjust the expected value based on your specific data

    def test_different_data(self):
        # Test interpolation with different data
        x = [4, 1, 5, 6]
        y = [1.386294, 0, 1.609438, 1.791759]
        interpolator = InterpoladorNewton(x, y)
        interpolator.calculaParametros()
        result = interpolator.estimar(2)
        # Create an interpolation function using Newton interpolation
        newton_interpolator = interp1d(x, y, kind='cubic')  # 'cubic' indicates Newton interpolation

        # Evaluate the interpolation function at a specific point
        result2 = newton_interpolator(2)

        self.assertAlmostEqual(result, result2, places=5)  # Adjust the expected value based on your specific data

    def test_basic_interpolation(self):
        # Test basic interpolation with known data
        x = [24, 25, 27, 28]
        y = [89, 124, 154, 165]
        interpolator = InterpoladorNewton(x, y)
        interpolator.calculaParametros()
        result = interpolator.estimar(25.8)

        # Create an interpolation function using Newton interpolation
        newton_interpolator = interp1d(x, y, kind='cubic')  # 'cubic' indicates Newton interpolation

        # Evaluate the interpolation function at a specific point
        result2 = newton_interpolator(25.8)

        self.assertAlmostEqual(result, result2, places=5)  # Adjust the expected value based on your specific data

    def test_large_input(self):
        # Test interpolation with a large dataset
        tam = 100
        x = list(range(1, tam))
        y = np.log(x)
        interpolator = InterpoladorNewton(x, y)
        interpolator.calculaParametros()
        result = interpolator.estimar(tam/2)

        # Create an interpolation function using Newton interpolation
        newton_interpolator = interp1d(x, y, kind='cubic')  # 'cubic' indicates Newton interpolation

        # Evaluate the interpolation function at a specific point
        result2 = newton_interpolator(tam/2)

        self.assertAlmostEqual(result, result2, places=5)  # Adjust the expected value based on your specific data


if __name__ == '__main__':
    unittest.main()
