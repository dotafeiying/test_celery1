from django.db import models
from datetime import datetime

class Add(models.Model):
    task_id = models.CharField(max_length=128)
    first = models.IntegerField()
    second = models.IntegerField()
    log_date = models.DateTimeField(default=datetime.now)

class LayuiDemo1(models.Model):
    f1 = models.AutoField(primary_key=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    sign = models.CharField(max_length=255, blank=True, null=True)
    classify = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    wealth = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layui_demo1'

    def __str__(self):
        return self.username