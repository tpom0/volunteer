from django.db import models

from decimal import Decimal

from datetime import datetime

class Volunteer(models.Model):
    first_name = models.CharField(max_length=100,)
    last_name = models.CharField(max_length=100,)

    phone_number = models.CharField(max_length=12, blank=True)

    seller_number = models.CharField(max_length=100, blank=True)

    role = models.ForeignKey('Role', related_name='volunteers')

    class Meta:
        unique_together = ("first_name", "last_name", "seller_number")
        ordering = ["last_name"]

    def get_full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    full_name = property(get_full_name)

    def get_total_hours(self):
        n = Decimal(0)
        for shift in self.shifts.all():
            n += shift.get_shift_hours()
        return n

    total_hours = property(get_total_hours)

    def __unicode__(self):
        if self.seller_number:
            return u'%s %s (%s)' % (self.first_name, self.last_name, self.seller_number)
        else:
            return u'%s %s' % (self.first_name, self.last_name)


class Role(models.Model):
    role = models.CharField(max_length=100,)
    manager = models.BooleanField(default=False)

    def __unicode__(self):
        return self.role






class Shift(models.Model):
    volunteer = models.ForeignKey('Volunteer', related_name='shifts')

    job = models.ForeignKey('Job', related_name='shifts', null=True, blank=True)

    group_shift = models.ForeignKey('GroupShift', related_name='shifts', null=True, blank=True, default=None, on_delete=models.SET_DEFAULT)

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    # need to be able to filter this to managers only
    managers_in_charge = models.ManyToManyField('Volunteer', blank=True)

    notes = models.TextField(blank=True)

    present_for_shift = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s' % (self.volunteer, self.job)

    def get_shift_hours(self):
        d1 = datetime(1, 1, 1, 0, 0, 0)

        td = datetime.combine(d1, self.end_time) - datetime.combine(d1, self.start_time)

        return Decimal(td.seconds / 60 / 60.0)

    shift_duration = property(get_shift_hours)

    class Meta:
        ordering = ['date', 'start_time', 'volunteer__last_name', 'volunteer__first_name']


class Job(models.Model):
    job = models.CharField(max_length=100,)
    heavy_lifting = models.BooleanField(default=False)

    def __unicode__(self):
        if 'heavy lifting' in self.job:
            return u'Racks'
        else:
            return self.job



class GroupShift(models.Model):
    group_shift_name = models.CharField(max_length=100,)

    def __unicode__(self):
        return self.group_shift_name
