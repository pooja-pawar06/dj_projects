from django.test import TestCase

# Create your tests here.

from helpers.emailfunctionality import send_email
from django.db.models.signals import pre_save,post_save,pre_init,post_init,pre_delete,post_delete,pre_migrate,post_migrate,m2m_changed
from django.dispatch import receiver
from p_signals.models import Account

@receiver(post_save, sender=Account)
def account_m4(sender, instance, created, raw, using, update_fields,*args, **kwargs):
    print('inside post_save m3', sender, instance, created, raw, using, update_fields,args, kwargs)
    print(instance.__dict__) #all fields
    print(instance.customer.email) #email adddress -->
    send_email(instance.customer.email,'body','subject')
    print('--------------------------------------------\n')