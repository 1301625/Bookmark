from django.urls import path
from .views import *

app_name='bookmark'
urlpatterns = [
    path('', BookmarkList.as_view(), name='list')
]