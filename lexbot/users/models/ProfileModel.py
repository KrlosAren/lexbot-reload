from django.db import models

from lexbot.utils.models import LexbotModel


class Profile(LexbotModel):
    """[Profile Model]

    a profile holds a user's public data like biography, picture,
    and statistics.

    """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    rut = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.user)
