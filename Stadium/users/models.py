from django.db import models
# from django.contrib.auth.models import User
import django.utils.timezone as timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
import django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractUser):
   email = models.EmailField(max_length=100, unique=True)
   password = models.CharField(max_length=100)
   is_verified = models.BooleanField(default=False)
#    username = models.CharField(blank=True,error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
#    EXCLUDE_FIELDS = 'username'
   objects = UserManager()


class CustomerProfile(models.Model):
    Customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cus')
    DOB = models.DateField()
    gender = models.IntegerField()
    phone_no = models.IntegerField()
    bio = models.TextField(null=True)
    joined = models.DateField(auto_now_add=True)
    avatar = models.TextField(null=True)
    friends = models.ManyToManyField("CustomerProfile")

    def __str__(self):
        return self.Customer.username


class FriendRequest(models.Model):
    from_user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='to_user')
    time = models.DateTimeField(auto_now_add=True)


# class game_session(models.Model):
#     Customer = models.models.ManyToManyField(CustomerProfile)
#     game = models.ManyToManyField(game)
#     session_start =


class VendorProfile(models.Model):
    Vendor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='ven')
    api_key = models.TextField(null=True)
    active = models.BooleanField(default=True)
    joined = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Vendor.username