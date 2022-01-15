from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.conf import settings
from core.models import TimestampedModel
from datetime import datetime, timedelta
import jwt

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, type, password=None):
        """Create and return a `User` with an email, username and password."""
        user = None
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')


        user = User.objects.create(username=username, email=self.normalize_email(email))

        if user:
            user.set_password(password)
            user.save()

        return user

    def create_superuser(self, username, email, password):
        """
      Create and return a `User` with superuser powers.
      Superuser powers means that this use is an admin that can do anything
      they want.
      """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=11, default='')
    email = models.EmailField(db_index=True, unique=True)
    password = models.CharField(max_length=255, default='')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().
        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()


    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')

        return token

class Car(models.Model):
        Petrol = "BENZYNA"
        LPG = "LPG"
        Diesel = "DIESEL"
        Electric = "ELEKTRYCZNY"
        Hybrid = "HYBRYDA"
        Fuel_Choices = (
        (Petrol, "Benzyna"), (LPG, "LPG"), (Diesel, "Diesel"), (Electric, "Elektryczny"), (Hybrid, "Hybryda"))

        Auto = "AUTOMATYCZNA"
        Manu = "MANUALNA"

        Tran_Choices = ((Manu, "Manualna"), (Auto, "Automatyczna"))
        fuel = models.TextField(max_length=25, choices=Fuel_Choices, default=Petrol)
        power = models.IntegerField()
        mileage = models.IntegerField()
        transmission = models.TextField(max_length=25, choices=Tran_Choices, default=Manu)
        mileage = models.FloatField()
        owner = models.ForeignKey(User, on_delete=models.CASCADE)












