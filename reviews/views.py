from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    name = request.GET.get("name") or "world"
    return HttpResponse("Hello, {}!".format(name))


def index(request):
    name = "John"
    return render(request, "base.html", {"name": name})


def book_search(request):
    result = request.GET.get("result")
    return render(request, "search.html", {"result": result})
