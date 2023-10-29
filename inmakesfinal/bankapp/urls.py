from django.urls import path

from bankapp import views

app_name= 'bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),
    path('branch_load',views.load_branch,name='ajax_branch')

]