from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from helpers import SITE_TITLE, SITE_TAG_LINE, SITE_KEYWORDS, SITE_URL, SITE_LOGO, SITE_FAVICON
import json


def postDataIn(request):
    dataIn = {}
    try:
        dataIn = json.loads(request.body)
    except:
        dataIn = request.POST.copy()
    return dataIn


