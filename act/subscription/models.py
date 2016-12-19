# act_project/act/subscription/models.py
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError

from .services import CheckoutHash


class Subscriber(models.Model):
    CheckoutHash = CheckoutHash()

    email = models.EmailField('E-mail', max_length=254)
    is_active = models.BooleanField('Активний', default=False)
    subscribed_at = models.DateTimeField(
        'Дата та час підписки', auto_now_add=True)
    checkout_at = models.DateTimeField(
        'Дата та час запиту', null=True, blank=True, default=None)

    checkout_hash = models.CharField(
        max_length=40, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Підписник'
        verbose_name_plural = 'Підписники'

    def __str__(self):
        return str(self.email) or self.__class__.__name__

    def prepare_checkout_hash(self):
        self.checkout_hash = self.CheckoutHash.generate()
        self.checkout_at = timezone.now()

        return self.checkout_hash

    def validate_checkout(self, checkout_hash):
        if not self.checkout_hash:
            raise ValidationError(None)

        if not self.CheckoutHash.compare(self.checkout_hash, checkout_hash):
            raise ValidationError(None)

    def complete_checkout(self, checkout_hash):
        if self.is_active:
            self.subscribe()
        else:
            self.unsubscribe()

        self.checkout_at = None

    def subscribe(self):
        self.checkout_hash = self.CheckoutHash.generate()
        self.is_active = True

    def unsubscribe(self):
        self.is_active = False