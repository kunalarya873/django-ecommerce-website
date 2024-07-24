from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse
def send_account_activation_email(email , email_token):
    subject = 'Your account needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject , message , email_from , [email])

def send_prod_smtp_email(email , email_token):
    subject = "SMTP TESTING USING MAILTRAP"
    body = f'Hi, click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    from_email = 'mailtrap@demomailtrap.com'

    email_smtp = EmailMessage(subject=subject,
                 body=body,
                 from_email=from_email,
                 to=[email])
    email_smtp.send()
