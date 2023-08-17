from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Union
from backend.models import User
from django.views.decorators.csrf import csrf_exempt
import os


# Create your views here.
@csrf_exempt
def upload(request: HttpRequest) -> HttpResponse:
    name = request.POST.get(key="name",default=None)
    address = request.POST.get(key="address", default=None)
    mobile = request.POST.get(key="mobile", default=None)
    the_file = request.FILES["myfile"]
    dest_filename = os.path.join("uploads", the_file.name)
    with open(dest_filename, 'wb+') as destination:
            for chunk in the_file.chunks():
                destination.write(chunk)

    user = User(name=name, address=address,mobile_number=mobile, file_location=dest_filename )
    user.save()
    data = {"name": name,
            "address": address,
            "mobile": mobile,
            "image_loc": "/static/" + dest_filename}

    return render(request, 'formed.html', data)
