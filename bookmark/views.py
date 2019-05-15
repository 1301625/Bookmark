from django.shortcuts import render
from django.views import generic

from .models import Bookmark
# Create your views here.


class BookmarkList(generic.ListView):
    model = Bookmark
    template_name = 'bookmark/index.html'