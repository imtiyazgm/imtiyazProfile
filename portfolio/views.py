from django.shortcuts import render

# Create your views here.

def homePage(request):
	context ={}

	return render(request, 'portfolio/home.html', context)

def workExp(request):
	context={}
	return render(request, 'portfolio/npkmefze.html', context )

def workExpfzco(request):
	context={}
	return render(request, 'portfolio/npkmefzco.html', context )

def workExpMidco(request):
	context={}
	return render(request, 'portfolio/midco.html', context )

def workExpAlma(request):
	context={}
	return render(request, 'portfolio/alma.html', context )