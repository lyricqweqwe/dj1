from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)
    class Meta:
        db_table='users'
