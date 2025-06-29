import logging

from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from .models import Product


logger = logging.getLogger(__name__)
logging.basicConfig(filename='shop_app.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    if created:
        print(f'New product created: {instance.name}')
    else:
        instance.updated_at = timezone.now() + timezone.timedelta(days=2)
        print(f'Product updated: {instance.name}')


# Подключение функции-обработчика к сигналу
# post_save.connect(product_saved, sender=Product)


@receiver(post_save, sender=Product)
def notify_admin_on_new_order(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New Product Created',
            f'Product {instance.id} has been created.',
            'admin@gmail.com',
            ['admin@gmail.com'],
        )


@receiver(post_delete, sender=Product)
def log_book_deletion(sender, instance, **kwargs):
    logger.info(f'Product deleted: {instance.id}) {instance.name}')
