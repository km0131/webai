# webimage/urls.py

from django.urls import path
from . import views # 同じディレクトリ内のviews.pyをインポート

urlpatterns = [
    path('', views.index, name='index'), 
]