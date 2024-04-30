from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from .form import ContactForm


# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            email = EmailMessage('Message from Black Store',
                                 f'The user {name} with the direction {email}'
                                 f' writes the following'
                                 f' \n\n {content}', '',
                                 ['gonzalezreyesadriano2507@gmail.com'], reply_to=[email])

            try:
                email.send()
                return redirect('/contact/?success=1')
            except:
                return redirect('/contact/?success=0')

    return render(request, 'contact.html', {'contact_form': contact_form})
