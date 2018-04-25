from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import InfoForm
from .models import Info
from django.template.loader import render_to_string
import json


# Create your views here.
def index(request):
    return render(request, template_name='booksList.html', context={'books': Info.objects.all()})


def save(request, form, t_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['books'] = render_to_string(template_name='booksRow.html', request=request, context={'books': Info.objects.all()})
            # return HttpResponse(json.dumps({'status': "done"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps('fail'), content_type="application/json")
    else:
        context = {
            'form': form,
        }
        data['html_form'] = render_to_string(template_name=t_name, request=request, context=context)
    return JsonResponse(data)


def createBook(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
    else:
        form = InfoForm()
    return save(request, form, "create_books.html")
