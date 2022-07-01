#########################################################################################################
########## helpers #################################################################################
#########################################################################################################
from elasticsearch import Elasticsearch
import random
import string
from datetime import datetime

SITE_URL = 'https:app.salesmix.com/'
SITE_TITLE = 'SalesMix'
SITE_TAG_LINE = ''
SITE_KEYWORDS = ''
SITE_LOGO = 'logo.png'
SITE_FAVICON = 'favicon.png'
SITE_PUBLIC_PATH = '/var/www/public'

db = Elasticsearch(
    [
        'http://elastic:zpuuCuE3saPFjlQbVwUd@15.235.40.200:8200',
    ]
)

def timestamp():
    return int(datetime.timestamp(datetime.now()))


def randomString(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

