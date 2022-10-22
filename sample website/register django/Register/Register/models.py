from inspect import classify_class_attrs
from django.db import models

class Registration(models.Model):
    name=models.CharField(max_length=100)
    moodle_id=models.IntegerField(max_length=100)
    email_id=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    class Meta:
        db_table="registeredusers"