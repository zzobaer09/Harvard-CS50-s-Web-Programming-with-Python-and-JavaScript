from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

# * this function here is to say "yes" or "no" if it is new year
def isNewYear(request):
    val = "Not New Year"

    now = datetime.now()
    month = now.month
    day = now.day

    if month == 1 and day == 1: val = "New Year"
    return render(request , "newyear/index.html" , {"isNewYear":val})


def NowDate(request):

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    time = now.timetz
    return render(request , "newyear/nowdate.html" , {"year":year , "month":month , "day":day , "time":time})