import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.base import Model
from rest_framework.exceptions import ValidationError

from auth_.models import MainUser
from utils.constants import rating_numbers, subscription_type, status_choices


def is_valid_date(value):
    if datetime.date.today() >= value:
        raise ValidationError("You can not make subscription for past date")


def is_valid_number(value):
    if value < 0:
        raise ValidationError("The cost can not be negative number")


def is_valid_account_number(value):
    value = len(value)
    if 8 > value > 12:
        raise ValidationError("Please enter valid account number")


def is_valid_comment(value):
    value = len(value)
    if value <= 1:
        raise ValidationError("Please add some words!")


class SubscriptionManager(models.Manager):
    use_in_migrations = True

    def subscription_details_by_gym(self, rk, pk):
        return self.filter(id=pk, gym=rk)


class GymManager(models.Manager):
    use_in_migrations = True

    def subscription_details_by_gym(self, pk, rk):
        return self.filter(id=pk).filter(gym=rk)


class AbonementManager(models.Manager):
    use_in_migrations = True

    def abonements_by_gym(self, pk):
        return self.filter(gym=pk)


class CommentManager(models.Manager):
    use_in_migrations = True

    def comment_detail_by_gym(self, hk, pk):
        return self.filter(id=pk).filter(gym=hk)


class Gym(models.Model):
    name = models.CharField("Name", max_length=20)
    staff = models.ForeignKey(MainUser, verbose_name="Staff", on_delete=models.CASCADE, null=True)
    rating = models.FloatField("rating", default=0)
    account_number = models.IntegerField("Account Number", blank=False)
    address = models.CharField("Address", max_length=200, blank=False)
    city = models.CharField("City", max_length=20)
    phone_number = models.CharField("Phone Number", max_length=11)

    objects = GymManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Gym"
        verbose_name_plural = "Gyms"


class Subscription(models.Model):
    gym = models.ForeignKey(Gym, verbose_name="Gym", on_delete=models.CASCADE, null=True)
    type = models.CharField("Type", choices=subscription_type, max_length=20)
    cost = models.IntegerField("Cost", validators=[is_valid_number])

    objects = SubscriptionManager()


    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return '%s: %s' % (self.id, self.type)

class Photos(models.Model):
    photo = models.ImageField()

    class Meta:
        abstract = True


class GymPhoto(Photos):
    photo = models.ImageField(upload_to='gym_photos', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    gym = models.ForeignKey(Gym, verbose_name="Gym", on_delete=models.CASCADE, null=True,
                            related_name="gym_photos")

    def __str__(self):
        return '%s, %s' % (self.id, self.gym.name)


class Abon(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True)
    subscription = models.ForeignKey(Subscription, verbose_name="Subscription", on_delete=models.CASCADE, null=True)
    gym = models.ForeignKey(Gym, verbose_name="Gym", on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField("Purchase date", auto_now=True)
    expired_date = models.DateField("Expired date", validators=[is_valid_date])
    total_cost = models.IntegerField("Total Cost", validators=[is_valid_number])
    payment_status = models.IntegerField("Payment status", choices=status_choices)

    objects = AbonementManager()


    class Meta:
        verbose_name = "Abonement"
        verbose_name_plural = "Abonements"

    def __str__(self):
        return '%s' % (self.id)


class Transaction(models.Model):
    abonement = models.ForeignKey(Abon, verbose_name="Abonement", on_delete=models.CASCADE, null=True)
    reference_number = models.IntegerField("Reference number")

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return '%s' % (self.reference_number)


class Comment(models.Model):
    customer = models.ForeignKey(MainUser, verbose_name="Customer", on_delete=models.CASCADE, null=True,
                                 related_name="customer_comments")
    gym = models.ForeignKey(Gym, verbose_name="Gym", on_delete=models.CASCADE, null=True,
                            related_name="gym_comments")
    text = models.TextField("Comment Text", validators=[is_valid_comment])
    rating = models.IntegerField("Number of stars", choices=rating_numbers)

    objects = CommentManager()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return '%s: %s' % (self.customer.first_name, self.text)
