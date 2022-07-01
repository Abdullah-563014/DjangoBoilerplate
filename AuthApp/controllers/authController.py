from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from helpers import db, SITE_TITLE, SITE_TAG_LINE, SITE_KEYWORDS, SITE_URL, SITE_LOGO, SITE_FAVICON, randomString, timestamp
import time
from django.contrib.auth import logout, login
import uuid
import json
# from AuthApp.models import User
import random
import string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.hashers import make_password


def postDataIn(request):
    dataIn = {}
    try:
        dataIn = json.loads(request.body)
    except:
        dataIn = request.POST.copy()
    return dataIn


def index(request):
    if request.user.is_authenticated:
        return redirect('userDashboard')

    data = {}
    data['title'] = 'Login - ' + SITE_TITLE
    data['SITE_TITLE'] = SITE_TITLE
    data['description'] = SITE_TAG_LINE
    data['keywords'] = SITE_KEYWORDS
    data['image'] = SITE_LOGO
    data['imageType'] = 'image/png'
    data['logo'] = SITE_LOGO
    data['favicon'] = SITE_FAVICON
    data['url'] = SITE_URL
    data['updated_time'] = time.time()

    # print(db)
    # //dict
    # insertData = {}
    # insertData["created_at"] = insertData["updated_at"] = timestamp()
    # insertData["name"] = "salimH"
    # insertData["email"] = "salim@polyuno.com"
    # insertData["password"] = make_password("abcd")

    # makeId = randomString(32)


    return render(request, 'login.html', context=data)
