from django.test import TestCase
from calculations.business_layer.calculator import Calculator
from calculations.business_layer.caesar_cipher import CaesarCipher

# Create your tests here.
class test_suite(TestCase):
    def test_calculator_divide_should_divide_a_b(self):
        # assign
        calc = Calculator()

        # act
        result = calc.divide(10, 5)

        # assert
        self.assertEqual(result, 2)

    def test_calculator_divide_should_divide_a_0(self):
        # assign
        calc = Calculator()

        # act
        result = calc.divide(10, 0)

        # assert
        self.assertEqual(result, 0)

    def test_caesar_cipher_encode(self):
        # assign
        cipher = CaesarCipher()

        # act
        result = cipher.encrypt("super slaptas tekstas", "abc")
        # assert
        self.assertEqual(result, "Ô×ÓÆÔÔÎÄÑÖÄÔ×ÆÍÖÕÃÖ")

    def test_caesar_cipher_decode(self):
        # assign
        cipher = CaesarCipher()

        # act
        result = cipher.decode("Ô×ÓÆÔÔÎÄÑÖÄÔ×ÆÍÖÕÃÖ", "abc")
        # assert
        self.assertEqual(result, "super slaptas tekstas")