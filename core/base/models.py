from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# create models
from base.emails import send_account_activation_email

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

@receiver(post_save, sender = User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str = uuid.uuid4()
            email = instance.email
            send_account_activation_email(email, email_token)
    except Exception as e:
        print(e)
