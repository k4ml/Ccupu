from django.contrib import admin
from ccupu.models import Customer
from ccupu.models import Store
from ccupu.models import Item
from ccupu.models import StoreItem

admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(StoreItem)
