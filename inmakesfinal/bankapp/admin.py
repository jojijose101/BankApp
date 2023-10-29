from django.contrib import admin

from bankapp.models import Districts,Branches,BankAccount

# Register your models here.
admin.site.register(Districts)
admin.site.register(Branches)
admin.site.register(BankAccount)
