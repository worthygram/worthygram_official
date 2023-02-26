from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect

# Create your views here.

def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			message = "Your Message/Feedback is sent, manager@worthygram will contact you soon. Thank You.Keep exploring"
			return render(request,'footer/contact.html',{'message':message})
	else:
		form = ContactForm()
		context = {'form':form}
		return render(request,'footer/contact.html',context)

def contribute(request):
	return render(request,'footer/contribute.html')

def sponsor(request):
	return render(request,'footer/sponsor.html')

def guidelines(request):
	return render(request,'footer/guidelines.html')

def about(request):
	return render(request,'footer/about.html')


	

def error_404_view(request,exception=None):
	return redirect('/en')
	# return render(request,'footer/404.html')