from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from backend.models import Upload
from django.views.decorators.csrf import csrf_exempt
import os


# Create your views here.
@csrf_exempt
def upload(request: HttpRequest) -> HttpResponse:
    client_number = request.POST.get(key="clientnum", default=1)
    name = request.POST.get(key="name", default=None)
    address = request.POST.get(key="address", default=None)
    mobile = request.POST.get(key="mobile", default=None)
    the_file = request.FILES["myfile"]
    dest_filename = os.path.join("uploads", the_file.name)
    with open(dest_filename, 'wb+') as destination:
            for chunk in the_file.chunks():
                destination.write(chunk)

    upload_record = Upload(client_number=client_number,name=name,
                    address=address,mobile_number=mobile, file_location=dest_filename)
    upload_record.save()
    data = {"name": name,
            "address": address,
            "mobile": mobile,
            "image_loc": "/static/" + dest_filename}

    return render(request, 'formed.html', data)


def show_contents(request: HttpRequest, client_num: int) -> HttpResponse:
    uploads = Upload.objects.filter(client_number=client_num)
    data = []
    for upld in uploads:
        obj = {"id": upld.id,
               "name": upld.name,
               "address": upld.address,
               "mobile": upld.mobile_number,
               "image_loc": "/static/" + upld.file_location}
        data.append(obj)

    return render(request, 'contents.html', {"uploads":data})


