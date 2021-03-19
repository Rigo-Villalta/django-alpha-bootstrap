import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def digits_and_letters_validator(str):
    """
    Validador que permite ingresar únicamente
    letras y/o dígitos sin espacios vacíos.
    """
    if re.match(r"^[0-9A-Za-z]+$", str) is None:
        raise ValidationError(
            _("The field only accept letters and digits, blank spaces not allowed.")
        )
