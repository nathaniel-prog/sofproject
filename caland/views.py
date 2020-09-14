from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import datetime
from django.utils.safestring import mark_safe
from .models import Trip
from .forms import Calendar , TripForm


class CalendarView(generic.ListView):
    model = Trip
    template_name = 'month_cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return req_day(year, month, day=1)
    return datetime.today()
































def index(request):
    return HttpResponse("Hello word")









def mydates(request):
    if request.method == 'GET':
        form = TripForm()
        return render(request, 'mydates.htmL', {'form': form})

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()






