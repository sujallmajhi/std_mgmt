from django.urls import path
from .views import *
urlpatterns = [
    path('form/',form_list,name="form_list"),
    path('formpage/',form_page,name='add_std'),
    path('form/delete/<int:pk>/',delete_form,name="delete_form"),
    path('form/edit/<int:pk>/',edit_form,name="edit_form")
]
