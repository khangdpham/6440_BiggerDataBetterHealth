# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Meds(models.Model):
    id = models.IntegerField(primary_key=True)
    med_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    mean = models.FloatField(blank=True, null=True)
    std_dev = models.FloatField(blank=True, null=True)
    name = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'meds'

class MedsCorr(models.Model):
    id = models.IntegerField(primary_key=True)
    condition_id = models.BigIntegerField(blank=True, null=True)
    obs_count = models.IntegerField(blank=True, null=True)
    suggest_med_1 = models.IntegerField(blank=True, null=True)
    suggest_med_1_prob = models.FloatField(blank=True, null=True)
    suggest_med_2 = models.IntegerField(blank=True, null=True)
    suggest_med_2_prob = models.FloatField(blank=True, null=True)
    suggest_med_3 = models.IntegerField(blank=True, null=True)
    suggest_med_3_prob = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'meds_corr'

