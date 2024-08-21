from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from threading import Thread 
from .models import Doctor,User
from project.smtp import send_email

@receiver(post_save,sender=Doctor)
def send_notification_on_new_event(sender, created, instance, **kwargs):
    print('heloo')
    if created:
        doctor = instance
        subject = 'New doctor Added: {}'.format(doctor.name)
        message = 'A new event has been added. Check it out!'
        users = User.objects.all()

        for user in users:
            email_thread = Thread(
                target=send_email, args=(subject, message, settings.EMAIL_HOST, [user.email])
            )
            email_thread.start()
        