from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=300)
    address = models.TextField()

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def __unicode__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    address = models.TextField()
    item = models.ManyToManyField(Item, through='StoreItem')

    def __unicode__(self):
        return self.name

class StoreItem(models.Model):
    store = models.ForeignKey(Store)
    item = models.ForeignKey(Item)

    def __unicode__(self):
        return self.item.name
