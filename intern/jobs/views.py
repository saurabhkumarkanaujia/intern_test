from django.shortcuts import render
from college.models import Job
import datetime
from django.contrib.auth.models import User, auth
import json
# Create your views here.
def get_comp_name(request):
    if datetime.now() < expiry_date_time:
        users = User.objects.all().values('company_name')  
        users_list = list(users)
        return JsonResponse(users_list, safe=False)