import os, sys

from datetime import datetime

proj_path = "."
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TPOM.settings")
sys.path.append(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from tvsa.models import (Volunteer, Role, Shift, GroupShift, Job)

for v in Volunteer.objects.all():
    shifts = v.shifts.all()
    for s in shifts:
        try:
            # this is where it might throw Model.DoesNotExist
            s2 = shifts.get(date=s.date, end_time=s.start_time, job=s.job)

            # if you made it this far, then a shift exists with an end time equal to the
            #  current shift's start time.  That means it's a consecutive shift...
            s2.end_time = s.end_time
            s2.save()
            print 'Appended shift: ', s, s.date, s.start_time, s.end_time, s.job
            print '... to this shift: ', s2, s2.date, s2.start_time, s2.end_time, s2.job
            s.delete()
        except Shift.DoesNotExist:
            pass


