import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Create your views here.
# -----------------------Buisness Logic--------------------
def __generate_api_key(username):
    pass


def __save_data(username, email, phonenumber):
    pass


# ---------------------------------------------------------


def home(request):
    return render(request, "index.html", {"output": "this is your key"})


def docs(request):
    return render(request, "documentation.html")


# must handle form related links!
def createapi(request):
    if request.method == "POST":
        # username = request.POST["username"]
        # email = request.POST["mail"]
        # phonenumber = request.POST["phone"]
        # if (username == None or email == None or phonenumber == None):
        #     pass
        # else:
        #     __save_data(username, email, phonenumber)
        return render(request, "api.html")
    else:
        return HttpResponseBadRequest("Bad request, access denied!")


# this view will handle the servers model request!
def handle(request):
    if request.method == "GET":
        fakedata = json.dumps(
            {
                "data1": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data2": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data3": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data4": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data5": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data6": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data7": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data8": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data9": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data10": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data11": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data12": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data13": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data14": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data15": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data16": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data17": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data18": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data19": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data20": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data21": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
                "data22": [
                    "clean data and it is very large data",
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                ],
            }
        )
        return HttpResponse(fakedata)
    else:
        return HttpResponseBadRequest("Bad request method!")


def debugHeader(request):
    print("---------------------------------------------------------------------")
    print("scheme: ", request.scheme)
    print("---------------------------------------------------------------------")
    print("body", request.body)
    print("---------------------------------------------------------------------")
    print("path", request.path)
    print("---------------------------------------------------------------------")
    print("path_infor", request.path_info)
    print("---------------------------------------------------------------------")
    print("method", request.method)
    print("---------------------------------------------------------------------")
    print("encoding", request.encoding)
    print("---------------------------------------------------------------------")
    print("content_type", request.content_type)
    print("---------------------------------------------------------------------")
    print("GET", request.GET)
    print("---------------------------------------------------------------------")
    print("POST", request.POST)
    print("---------------------------------------------------------------------")
    print("COOKIES", request.COOKIES)
    print("---------------------------------------------------------------------")
    print("FILES", request.FILES)
    print("---------------------------------------------------------------------")
    print("META", request.META)
    print("---------------------------------------------------------------------")
    print("resolver_match", request.resolver_match)
    print(request.META.get("api-key"))
    # with open(f"static/json/data{current_time}.json",'wb') as f:
    #     f.write((request.body))
    return HttpResponse("DEBUG SUCCESSFUL!")


def debugHeaderPOST(request):
    if request.method == "POST":
        return HttpResponse("GOOD REQUEST, SEND AS MANY As YOU Want")
    return HttpResponseBadRequest("CRSF TOKEN SHIT")
