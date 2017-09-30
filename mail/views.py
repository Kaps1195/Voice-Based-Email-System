from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


from .forms import MailForm

# Create your views here.

def mail_create(request):
	if request.method == 'POST':
		form = MailForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			send_mail(instance.subject, instance.content,'kramnani95@gmail.com', [instance.to])
			#instance.save() 
			return HttpResponseRedirect('/')

	else:
		form = MailForm()

	context = {
		'form': form,
	}

	return render(request, 'mail/create.html', context)

    

