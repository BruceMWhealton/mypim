from django.db import models


class Relationship(models.Model):
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.category

class Resource(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    organization = models.CharField(max_length=100, null=True, blank=True)
    phone1 = models.CharField(max_length=30, null=True, blank=True)
    phone2 = models.CharField(max_length=30, null=True, blank=True)
    street_line1 = models.CharField(max_length=30, null=True, blank=True)
    street_line2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    email1 = models.EmailField(max_length=254, null=True, blank=True)
    email2 = models.EmailField(max_length=254, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    relationship = models.ManyToManyField(Relationship)

    class Meta:
        ordering = ['last_name',]

    def __str__(self):
        return self.first_name +  " " + self.last_name
