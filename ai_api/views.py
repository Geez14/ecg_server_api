from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.


def home(request):
    return render(request, "index.html", {"output": "this is your key"})


def docs(request):
    return render(request, "documentation.html")


# must handle form related links!
def createapi(request):
    print(request.method)
    if request.method == "POST":
        print("YES ACCEPTED")
        return render(request, "api.html")
    else:
        return HttpResponseBadRequest("Bad request, access denied!")


# this view will handle the servers model request!
def handle(request):
    return HttpResponse("model is giving you output wait...")
