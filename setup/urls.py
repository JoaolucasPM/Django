
from django.contrib import admin
from django.urls import path
from todos.views import home, ProductListView, ProductCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', ProductCreateView.as_view(), name='form'),
    path('list/',ProductListView.as_view(), name='list'),

]
