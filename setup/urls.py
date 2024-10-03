
from django.contrib import admin
from django.urls import path
from todos.views import home,form, ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('list/',ProductListView.as_view(), name='list'),

]
