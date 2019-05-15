# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views import generic

from .models import Bookmark

from django.urls import reverse_lazy
# Create your views here.


class BookmarkList(generic.ListView):
    model = Bookmark
    template_name = 'bookmark/index.html'


class BookmarkCreateView(generic.CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    '''
    reverse_lazy는 reverse와 같은 기능인데 generic view에서 주로 사용한다. 
    타이밍 로딩 문제로 generic view에서는 reverse는 사용할 수 없고 reverse_lazy를 사용해야한다.
    '''
    success_url = reverse_lazy('bookmark:list') #성공하면 설정한 곳으로 이동
    template_name_suffix = "_create"  #사용할 접미사만 변경하는 설정값
    """
    GET 요청에 표시되는 UpdateView 페이지는 '_form'의 template_name_suffix를 사용한다. 
    예를 들어, 작성자 모델의 개체를 업데이트하는 보기에 대해 이 속성을 '_update_form'으로 변경하면 기본 template_name이 
    'myap/auter_update_form.html'이 될 수 있다.
    """


class BookmarkDetailView(generic.DetailView):
    model = Bookmark


class BookmarkUpdateView(generic.UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = "_update"
    success_url = reverse_lazy('bookmark:list')


class BookmarkDeleteView(generic.DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')
