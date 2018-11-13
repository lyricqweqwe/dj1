from django.conf.urls import url
from django.contrib import admin
from demo1 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('dynamic/', views.dynamic),
    url('user/',views.test_db)
]
