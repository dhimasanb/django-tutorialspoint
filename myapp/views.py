from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def hello(request):
   today = datetime.datetime.now().date()

   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek})
