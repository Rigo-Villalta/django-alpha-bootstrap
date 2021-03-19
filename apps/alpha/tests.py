from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import translation
from django.utils.translation import gettext_lazy as _

from .validators import digits_and_letters_validator


class DigitAndLettersValidatorTests(TestCase):
    """
    Pruebas para el validador digits_and_letters_validator
    cubriendo todos los casos límites  e intermedios.
    """

    def test_digits_and_letters_validator(self):
        with translation.override("en"):
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator(" oo45")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("oik85 ")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("ji895 kd9")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator(" jdio 78dj ")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("%6mjd&p9")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("uidj&ldo")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("dju894#")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("*^%(#@!")
            with self.assertRaisesMessage(
                ValidationError,
                "The field only accept letters and digits, blank spaces not allowed.",
            ):
                digits_and_letters_validator("kdfja-k68")
        self.assertIs(digits_and_letters_validator("difokspldk"), None)
        self.assertIs(digits_and_letters_validator("98574938"), None)
        self.assertIs(digits_and_letters_validator("DRUOKSOS"), None)
        self.assertIs(digits_and_letters_validator("DKFOsjdkDK"), None)
        self.assertIs(digits_and_letters_validator("dfoikds948"), None)
        self.assertIs(digits_and_letters_validator("DKFD948D4"), None)
        self.assertIs(digits_and_letters_validator("8dadiOkd5"), None)
        self.assertIs(digits_and_letters_validator("MKOdj56dkM"), None)
        self.assertIs(digits_and_letters_validator("MDK98kh"), None)
