from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from subscription.models import Subscribe
from blog.models import Blog


@receiver(post_save, sender=Blog)
def send_newsletter(sender, instance, created, **kwargs):
    if (created and instance.is_published) or (instance.is_published and (instance.updated_at == instance.created_at)):
        subscribers = Subscribe.objects.filter(is_active=True)
        recipient_list = [subscriber.email for subscriber in subscribers]

        subject = f'New Post: {instance.title}'
        from_email = settings.DEFAULT_FROM_EMAIL
        base_url = "https://blog-mdshakib007-backend.vercel.app/api/v1/subscription/unsubscribe/"
        blog_url = f"https://mdshakib007.vercel.app/posts/{instance.id}"

        for recipient in recipient_list:
            unsubscribe_url = f"{base_url}{recipient}/"

            context = {
                'title': instance.title,
                'tags': instance.tags.all(),
                'post_url': blog_url,
                'unsubscribe_url': unsubscribe_url,
            }
            html_content = render_to_string("send_blog_notification.html", context)

            email = EmailMultiAlternatives(subject, from_email, [recipient])
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)