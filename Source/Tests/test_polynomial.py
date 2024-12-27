"""Test file for polynomial's classe"""

import unittest

import sys
import os

# Add the path of the parent repertory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    """Tests to check all of Polynomial's functionnality"""

    # String test
    def test_str_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(str(f), "f(x) = -3x² + 23x - 67")

    def test_str_2(self):
        g = Polynomial(x15=-1, x56=14, x0=35, name="g")

        self.assertEqual(str(g), "g(x) = 14x^56 - x^15 + 35")

    def test_str_3(self):
        coefficients = (-1, -1, 0)
        h = Polynomial(coefficients, name="h")

        self.assertEqual(str(h), "h(x) = -x² - x")

    # Representation test
    def test_repr_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(repr(f), "Polynomial(x2=-3, x=23, -67)")

    def test_repr_2(self):
        g = Polynomial(x15=-1, x56=14, x0=35, name="g")

        self.assertEqual(repr(g), "Polynomial(x56=14, x15=-1, 35)")

    def test_repr_3(self):
        coefficients = (-1, -1, 0)
        h = Polynomial(coefficients, name="h")

        self.assertEqual(repr(h), "Polynomial(x2=-1, x=-1)")

    # Attribute test
    def test_attributes_alphabetic_degree_1(self):
        coefficients = {'x5':-4, 'x4':3, 'x3':-56, 'x2':1, 'x1':26, 'x0':3}
        f = Polynomial(**coefficients)

        self.assertTupleEqual((f.a, f.b, f.c, f.d, f.e, f.f), (-4, 3, -56, 1, 26, 3))

    def test_attributes_alphabetic_degree_2(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)

        self.assertTupleEqual((f.a, f.b, f.c), coefficients)

    def test_attributes_alphabetic_degree_3(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        f.a = 34

        self.assertEqual(repr(f), "Polynomial(x2=34, x=23, -67)")

    def test_attributes_alphabetic_degree_4(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        del f.c

        self.assertEqual(repr(f), "Polynomial(x2=-3, x=23)")

    def test_attributes_x_degree_1(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)

        self.assertTupleEqual((f.x2, f.x1, f.x0), coefficients)

    def test_attributes_x_degree_2(self):
        coefficients = (45, -67, 89, 18, 0)
        f = Polynomial(coefficients)

        self.assertTupleEqual((f.x5, f.x4, f.x3, f.x2, f.x1, f.x0), (0, 45, -67, 89, 18, 0))

    def test_attributes_x_degree_3(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        f.x2 = 34

        self.assertEqual(repr(f), "Polynomial(x2=34, x=23, -67)")

    def test_attributes_x_degree_4(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        del f.x0

        self.assertEqual(repr(f), "Polynomial(x2=-3, x=23)")

    def test_attributes_index_degree_1(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)

        self.assertTupleEqual((f[2], f[1], f[0]), coefficients)

    def test_attributes_index_degree_2(self):
        coefficients = (45, -67, 89, 18, 0)
        f = Polynomial(coefficients)

        self.assertTupleEqual((f[5], f[4], f[3], f[2], f[1], f[0]), (0, 45, -67, 89, 18, 0))

    def test_attributes_index_degree_3(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        f[2] = 34

        self.assertEqual(repr(f), "Polynomial(x2=34, x=23, -67)")

    def test_attributes_index_degree_4(self):
        coefficients = (-3, 23, -67)
        f = Polynomial(coefficients)
        del f[0]

        self.assertEqual(repr(f), "Polynomial(x2=-3, x=23)")

    def test_tips_zero_1(self):
        f = Polynomial(0, 0, -3, 23, -67, 0)

        self.assertTupleEqual((f.coefficients, f.sparse), ([-3, 23, -67, 0], {'x3': -3, 'x2': 23, 'x1': -67, 'x0': 0}))

    def test_tips_iter_1(self):
        f = Polynomial(-3, 23, -67)
        x2, x1, x0 = f

        self.assertTupleEqual((x2, x1, x0), (-3, 23, -67))

    def test_tips_len_1(self):
        f = Polynomial(0, 0, 0, -3, 23, -67, 0)

        self.assertEqual(len(f), 4)

    def test_tips_list_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(list(f), [-3, 23, -67])

    def test_tips_contains_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertIn('x2', f)

    def test_tips_contains_2(self):
        f = Polynomial(-3, 23, -67)

        self.assertNotIn('x36', f)

    def test_tips_call_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(f(5), -27)

    def test_tips_call_2(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(f(0), -67)

    def test_degree_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(f.degree, 2)

    def test_degree_2(self):
        f = Polynomial(x56=0, x35=-1)

        self.assertEqual(f.degree, 35)

    def test_items_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(f.items(), [('x2', -3), ('x1', 23), ('x0', -67)])
        self.assertEqual(dict(f.items()), f.sparse)

    def test_coefficients_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertListEqual(f.coefficients, [-3, 23, -67])

        f.coefficients = (3, 56, -1, 89)

        self.assertListEqual(f.coefficients, [3, 56, -1, 89])

    def test_sparce_1(self):
        f = Polynomial(x3=3, x2=56, x1=-1, x0=89)

        self.assertDictEqual(f.sparse, {'x3': 3, 'x2': 56, 'x1': -1, 'x0': 89})

        f.sparse = {"x2":-3, "x1":23, "x0":-67}

        self.assertDictEqual(f.sparse, {'x2': -3, 'x1': 23, 'x0': -67})

    def test_derive_1(self):
        f = Polynomial(-3, 23, -67)

        self.assertEqual(f.derive(), Polynomial(x1=-134, x0=23))

    def test_copy_1(self):
        h = Polynomial(9, -30, 25, name="h")
        sh = str(h)
        
        _h = h.copy()
        _sh = str(_h)

        self.assertEqual(sh, _sh)

    def test_solve_2_roots_equation_1(self):
        f = Polynomial(1, 1, -12)

        self.assertEqual(f.delta, 49)
        self.assertTupleEqual(f.solve(), (-4.0, 3.0))

    def test_solve_1_roots_equation_1(self):
        h = Polynomial(9, -30, 25, name="h")

        self.assertEqual(h.delta, 0)
        self.assertTupleEqual(h.solve(), (1.6666666666666667,))


    def test_expression_devellopped_1(self):
        f = Polynomial(1, 1, -12)

        self.assertEqual(f.devellopped(), "1x² + x - 12")

    def test_expression_canonic_1(self):
        f = Polynomial(1, 1, -12)

        self.assertTupleEqual((f.alpha, f.beta), (-0.5, -12.25))
        self.assertEqual(f.canonic(), "(x + 0.5)² - 12.25")

    def test_expression_factorised_1(self):
        f = Polynomial(1, 1, -12)

        self.assertEqual(f.factorised(), "(x + 4.0)(x - 3.0)")

    def test_expression_factorised_2(self):
        h = Polynomial(9, -30, 25, name="h")

        self.assertEqual(h.factorised(), "9(x - 1.667)²")

    def test_manipulation_equal_1(self):
        f = Polynomial(1, 1, -12)
        h = Polynomial(9, -30, 25, name="h")

        self.assertNotEqual(f, h)

    def test_manipulation_equal_2(self):
        f = Polynomial(9, -30, 25)
        h = Polynomial(9, -30, 25, name="h")

        self.assertEqual(f, h)

    def test_manipulation_negative_1(self):
        f = Polynomial(9, -30, 25)
        h = -f
        h.name = "h"

        self.assertEqual(str(h), "h(x) = -9x² + 30x - 25")

    def test_add_1(self):
        one = Polynomial([2,4,7,3])
        two = Polynomial([5,2,4,2])

        r = one + two

        self.assertEqual(list(r.coefficients), [7, 6, 11, 5])

    def test_add_2(self):
        one = Polynomial([2,4,7,3,5,2])
        two = Polynomial([5,2,4,2])

        r = one + two

        self.assertEqual(list(r.coefficients), [2,4,12,5,9,4])

    def test_add_3(self):
        one = Polynomial([7,3,5,2])
        two = Polynomial([6,8,5,2,4,2])

        r = one + two

        self.assertEqual(list(r.coefficients), [6,8,12,5,9,4])

    def test_add_4(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = f + g
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 35x^5 + 18x² + 5x")

    def test_add_5(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = g + 1
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 21x² + 5x")

    def test_sub_1(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = f - g
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 35x^5 - 24x² - 5x + 2")

    def test_sub_2(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = f - 1
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 35x^5 - 3x^2")

    def test_mul_1(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = f * 3
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 105x^5 - 9x² + 3")

    def test_div_1(self):
        f = Polynomial(x5=35, x2=-3, x0=1)
        g = Polynomial(21, 5, -1, name="g")

        h = f / 2
        h.name = "h"

        self.assertEqual(str(h), "h(x) = 17.5x^5 - 1.5x² + 0.5")


if __name__ == '__main__':
    unittest.main()