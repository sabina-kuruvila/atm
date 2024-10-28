from django.contrib import admin
from . models import ATM, transaction

admin.site.register(ATM)
admin.site.register(transaction)

# Register your models here.
