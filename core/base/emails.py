from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_account_activation_email(email, email_token):
    subject = 'Activate your account'
    email_from = settings.EMAIL_HOST_USER
    domain = settings.DOMAIN
    activation_link = f'{domain}/accounts/activate/{email_token}'
    
    html_message = render_to_string('emails/account_activation_email.html', {'activation_link': activation_link})
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, email_from, [email], html_message=html_message)
