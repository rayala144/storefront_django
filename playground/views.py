from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request -> response


def calc():
    a = 3
    b = 5
    return a

def say_hello(request):
    a = calc()
    # b = 8
    return render(request, 'hello.html', {'name': 'Kabali'})
