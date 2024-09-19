from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        unmessage = request.POST['unmessage']

        try:
            send_mail(
                message_subject,  # Subject of the email
                unmessage,        # Body of the message
                message_email,    # From email
                ['chikkiammu941@gmail.com'],  # To email
            )
            return render(request, 'contact.html', {'message_name': message_name, 'success': True})
        except Exception as e:
            return render(request, 'contact.html', {'message_name': message_name, 'error': str(e)})

    else:
        return render(request, 'contact.html', {})
