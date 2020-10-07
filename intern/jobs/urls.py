from django.urls import path
from.import views
urlpatterns=[
   path('get_comp_name/',views.get_comp_name,name='get_comp_name'),
]
