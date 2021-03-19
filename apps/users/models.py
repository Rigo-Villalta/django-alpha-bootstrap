from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from alpha.validators import digits_and_letters_validator


class User(AbstractUser):
    """
    User model, without first_name and last_name fields
    """

    first_name = None
    last_name = None
    username = models.CharField(
        _("username"),
        max_length=20,
        unique=True,
        help_text=_("Required. 20 characters or fewer. Letters and digits only. No blank spaces"),
        validators=[digits_and_letters_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("user")
