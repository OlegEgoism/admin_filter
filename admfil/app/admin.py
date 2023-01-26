from django.contrib import admin
from .models import PC, Person, Address
from django_reverse_admin import ReverseModelAdmin


@admin.register(PC)
class PCAdmin(admin.ModelAdmin):
    list_display = 'name', 'price',
    list_filter = 'price',


@admin.register(Person)
class PersonAdmin(ReverseModelAdmin):
    inline_type = 'tabular'
    inline_reverse = ['business_addr', ('home_addr', {'fields': ['street', 'zipcode', 'city', 'state']}), ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = 'street', 'zipcode', 'city', 'state'
    list_filter = 'city',
