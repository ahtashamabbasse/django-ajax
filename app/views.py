from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import InfoForm
from .models import Info
from django.template.loader import render_to_string
import json


# Create your views here.
def index(request):
    return render(request, template_name='booksList.html')


def createBook(request):
    data = dict()
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(json.dumps({'status': "done"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps('fail'), content_type="application/json")
    else:
        form = InfoForm()
        context = {
            'form': form
        }
        data['html_form'] = render_to_string(template_name="create_books.html",request=request, context=context )
    return JsonResponse(data)