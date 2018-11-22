from django.shortcuts import render
from django.views import generic
from .models import Bookmark

# Create your views here.

#--- ListView
class BookmarkLV(generic.ListView):
    model = Bookmark

#--- DetailView
class BookmarkDV(generic.DetailView):
    model = Bookmark