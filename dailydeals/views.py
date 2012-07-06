import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from dailydeals.models import DailyDeals

def deals(request, city):
    today_datetime = datetime.datetime.today()
    today = str(today_datetime)[0:10]
    deals = DailyDeals.objects.filter(created_date=today, city__iexact=city).order_by('-source_website_url')
    return render_to_response('index.html', {'deals': deals, 'today_datetime': today_datetime}, context_instance=RequestContext(request))
