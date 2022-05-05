from django.contrib import admin
from .models import Gym, Subscription, Abon, Transaction, AbstractUser,\
    GymPhoto, Comment

# Register your models here.

admin.site.register(Gym)
admin.site.register(GymPhoto)
admin.site.register(Subscription)
admin.site.register(Abon)
admin.site.register(Transaction)
admin.site.register(Comment)
