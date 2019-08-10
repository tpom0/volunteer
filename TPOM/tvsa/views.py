from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import View

from django.http import HttpResponse

from .models import Shift

from datetime import datetime

import json

from django.shortcuts import render

class ShiftList(View):
    def get(self, request, *args, **kwargs):

        date_selection = request.GET.get('date_selection', None)

        if date_selection:
            date = datetime.strptime(date_selection, '%Y-%m-%d').date()
            queryset = Shift.objects.filter(date=date)
        else:
            queryset = Shift.objects.all()

        def build_json_string_from_queryset(qs):

            qs_list = list()
            for x in qs:
                qs_dict = dict()
                qs_dict['id'] = str(x.pk)
                qs_dict['volunteer'] = x.volunteer.__unicode__()
                qs_dict['resource'] = x.job.__unicode__()
                qs_dict['start_time'] = datetime.combine(x.date, x.start_time).isoformat()
                qs_dict['end_time'] = datetime.combine(x.date, x.end_time).isoformat()
                qs_list.append(qs_dict)

            return json.dumps(qs_list, sort_keys=True)

        json_response = build_json_string_from_queryset(queryset)

        return HttpResponse(json_response, content_type="application/json")


class ShiftSignInView(View):
    def get(self, request, *args, **kwargs):

        date_selection = request.GET.get('date_selection', None)

        if date_selection:
            date = datetime.strptime(date_selection, '%Y-%m-%d').date()
            object_list = Shift.objects.filter(date=date)
        else:
            object_list = Shift.objects.all()

        #paginator = Paginator(object_list, 15) # Show 15 objects per page

        #page = request.GET.get('page')
        #try:
        #    paginated_object_list = paginator.page(page)
        #except PageNotAnInteger:
            # If page is not an integer, deliver first page.
        #    paginated_object_list = paginator.page(1)
        #except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
        #    paginated_object_list = paginator.page(paginator.num_pages)

        #return render(request, 'sign-in-sheet.html', {'object_list': paginated_object_list})
        return render(request, 'sign-in-sheet.html', {'object_list': object_list})


class ShiftDateList(View):
    def get(self, request, *args, **kwargs):

        shifts = Shift.objects.all()
        date_set = set()
        for shift in shifts:
            date_set.add(shift.date.isoformat())

        date_list = list(date_set)

        json_response = json.dumps(date_list, sort_keys=True)

        return HttpResponse(json_response, content_type="application/json")
