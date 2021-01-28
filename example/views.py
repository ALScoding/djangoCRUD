import os
import json
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render
from django.urls.resolvers import URLPattern

# relative import of forms
from .models import FlashcardsModel
from .forms import FlashcardsForm
from django.urls import path
# from .views import detail_view

# urlpatterns = [
#     path('<id>', detail_view),
# ]


def index(request):
    # index
    return render(request, "index.html")


def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = FlashcardsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = FlashcardsModel.objects.all()

    return render(request, "list_view.html", context)


# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = FlashcardsModel.objects.get(id=id)

    return render(request, "detail_view.html", context)


# after updating it will redirect to detail_View

# update view for details

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(FlashcardsModel, id=id)

    # pass the object as instance in form
    form = FlashcardsForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(FlashcardsModel, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

def load_view(request):
    context = {}

    with open("flashcards.json", "r", encoding="utf-8") as file:
        data = file.read()
        json_data = json.loads(data)
        context["data"] = "Flash Cards Loaded Successfully"

        for flashcard in json_data.get("cards"):
            FlashcardsModel.objects.create(
                backside=flashcard.get("backside"),
                frontside=flashcard.get("frontside"),
                answer=flashcard.get("answer")
            )

    return render(request, "load_view.html", context) 