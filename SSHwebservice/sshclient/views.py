from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import dataparser, sshconn
import os
from django.conf import settings
import json


# Create your views here.

def interfaces(request):
    data = sshconn.connect()
    output = dataparser.returnparsed(data)
    return HttpResponse(output)


def interface_detail(request, interface, option):
    data = sshconn.connect()
    output = dataparser.returnparsed(data)
    r = {}
    for i in output:
        if i["interface"] == interface+'/'+option:
            r = i
            break
    return HttpResponse(json.dumps(r))
