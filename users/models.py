from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser):
	email = models.EmailField(max_length=100, unique=True)
	firstname = models.CharField(max_length=50, default='')
	lastname = models.CharField(max_length=50, default='')
	phonenumber_regex = RegexValidator(regex=r'[0-9]{15}', message='Max length is 15 digits.')
	phonenumber = models.CharField(max_length=15, validators=[phonenumber_regex], default='')
	rank = models.CharField(max_length=10, default='Silver')
	building = models.CharField(max_length=50, default='')
	street = models.CharField(max_length=50, default='')
	city = models.CharField(max_length=50, default='')
	state = models.CharField(max_length=50, default='')
	

	def profilepic_path(self, filename):
		return 'profilepics/user_{0}/{1}'.format(self.pk, filename)
	
	profilepic = models.ImageField(upload_to=profilepic_path, blank=True, null=True)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, object=None):
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.is_admin


