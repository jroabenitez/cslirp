from django.shortcuts import render
from django.utils import timezone
from  .models import *

# Create your views here.
def strrhh_list(request):
	strrhh=Strrhh.objects.all().order_by('strh_papell','strh_sapell','strh_pnombre','strh_snombre',)
	return render(request, 'irp/strrhh_list.html', {'strrhh':strrhh})