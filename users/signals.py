from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, Location
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender = User)
def create_user_profile_and_location(sender, instance, created, **kwargs):
    if created:
            location = Location.objects.create()
            Profile.objects.create(user=instance, location=location)

            login_url = reverse('login')
            full_login_url = f'{settings.SITE_URL}{login_url}'

            subject = 'Muvoffaqqiyatli ro\'yxatdan o\'tdingiz'
            html_message = render_to_string('registration_email.html', {'username': instance.username, 'login_url': full_login_url} )
            plain_message = strip_tags(html_message)
            from_email = settings.DEFAULT_FROM_EMAIL
            to = instance.email
            send_mail(subject, plain_message, from_email, (to), html_message=html_message, fail_silently=False)




@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
