from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from subscription.models import Subscribe
from blog.models import Blog


@receiver(post_save, sender=Blog)
def send_newsletter(sender, instance, created, **kwargs):
    if (created and instance.is_published) or (instance.is_published):
        subscribers = Subscribe.objects.filter(is_active=True)
        recipient_list = [subscriber.email for subscriber in subscribers]
        # print(recipient_list)

        subject = f'New Post: {instance.title}'
        base_url = "https://blog-mdshakib007-backend.vercel.app/api/v1/subscription/unsubscribe/"

        from_email = settings.DEFAULT_FROM_EMAIL

        for recipient in recipient_list:
            unsubscribe_url = f"{base_url}{recipient}/"
            message = f"""
            A new post "{instance.title}" has been published. 
            
            Read it here: https://mdshakib007.vercel.app/posts/{instance.id}/
            
            If you wish to unsubscribe, click here: {unsubscribe_url}
            """

            send_mail(
                subject,
                message,
                from_email,
                [recipient],
                fail_silently=False
            )
