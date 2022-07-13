from crypt import methods
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.db.models.functions import Concat
from django.db.models import CharField, F, Value as V
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, F, Func, Value, CharField
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.conf import settings
import json, datetime


from django.views.decorators.csrf import csrf_exempt

class TestApiView(View):
    def get(self, request, *args, **kwargs):
        text = request.GET['text']
        return_data = {
            'text' : text,
            'test1' : 'aaa',
            'test2' : 'bbb',
            'test3' : 'ccc'
        }
        return_data = json.dumps(return_data, ensure_ascii=False)
        return HttpResponse(return_data, content_type = "application/json")

