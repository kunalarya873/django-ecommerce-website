from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from base.emails import send_account_activation_email
import uuid
import logging
from .models import *
logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    if created:
        try:
            # Ensure profile exists
            profile, profile_created = Profile.objects.get_or_create(user=instance)
            if not profile_created:
                # If profile already exists, update token
                profile.email_token = uuid.uuid4()
                profile.save()
            # Send activation email
            send_account_activation_email(instance.email, str(profile.email_token))
        except Exception as e:
            logger.error(f"Error sending email token: {e}")
