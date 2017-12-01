# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class FluExpOnly(models.Model):
    claim_num = models.CharField(primary_key=True,max_length=8)
    member_id = models.CharField(max_length=10, blank=True, null=True)
    claim_date = models.DateField(blank=True, null=True)
    fiscal_year = models.CharField(max_length=4, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    paid_amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    l_d_code = models.CharField(max_length=50, blank=True, null=True)
    l_d_desc = models.CharField(max_length=500, blank=True, null=True)
    exptype = models.CharField(db_column='expType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=3, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city_county = models.CharField(max_length=50, blank=True, null=True)
    fips = models.CharField(max_length=5, blank=True, null=True)
    place = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.claim_num + " " + self.fiscal_year + " " + self.member_id + " " + str(self.paid_amt)

    class Meta:
        managed = True
        db_table = 'flu_exp_only'


class FluRelatedExp(models.Model):
    claim_num = models.CharField(primary_key=True,max_length=8)
    member_id = models.CharField(max_length=10, blank=True, null=True)
    claim_date = models.DateField(blank=True, null=True)
    fiscal_year = models.CharField(max_length=4, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    paid_amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    cat = models.CharField(max_length=20, blank=True, null=True)
    cat2 = models.CharField(max_length=40, blank=True, null=True)
    cat3 = models.CharField(max_length=40, blank=True, null=True)
    age = models.CharField(max_length=3, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city_county = models.CharField(max_length=50, blank=True, null=True)
    fips = models.CharField(max_length=5, blank=True, null=True)
    place = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.claim_num + " " + self.fiscal_year + " " + self.member_id + " " + str(self.paid_amt)


    class Meta:
        managed = True
        db_table = 'flu_related_exp'


class FluShotData(models.Model):
    claim_num = models.CharField(primary_key=True,max_length=8)
    member_id = models.CharField(max_length=10, blank=True, null=True)
    claim_date = models.DateField(blank=True, null=True)
    fiscal_year = models.CharField(max_length=4, blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    paid_amt = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    l_d_code = models.CharField(max_length=50, blank=True, null=True)
    l_d_desc = models.CharField(max_length=500, blank=True, null=True)
    exptype = models.CharField(db_column='expType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=3, blank=True, null=True)
    plan = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city_county = models.CharField(max_length=50, blank=True, null=True)
    fips = models.CharField(max_length=5, blank=True, null=True)
    place = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.claim_num + " " + self.fiscal_year + " " + self.member_id + " " + str(self.paid_amt)


    class Meta:
        managed = True
        db_table = 'flu_shot_data'
