from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        # user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(username=username)


# Create your models here.
class Users(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=300)
    email= models.CharField(max_length=300, default='', unique=True)

    USERNAME_FIELD = 'username'


    objects = UserAccountManager()

    class Meta:
        db_table = "users"

class Permissions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = "permissions"


class Roles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        db_table = "roles"


class Role_map(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=uuid.uuid4)
    permission = models.ForeignKey(Permissions, on_delete=models.CASCADE, default=uuid.uuid4)

class User_role (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Users,on_delete=models.CASCADE,default=uuid.uuid4)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=uuid.uuid4)
    multiple_role = models.BooleanField(default=False)
    class Meta:
        db_table = "user_role"


class User_request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=uuid.uuid4)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = "user_request"
