from django.shortcuts import render
from django.http import HttpResponse
from .models import Slider, Option, SmallOption,Product
# Create your views here. 

def index(request):
	
	slides = Slider.objects.all()
	option = Option.objects.all()
	soption = SmallOption.objects.all()
	product = Product.objects.all()
	
	abc = {'slides': slides , 'option': option, 'soption': soption, 'product': product}
	return render(request, 'index.html', abc)

def about(request):
	return render(request, 'about.html')