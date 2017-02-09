from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    create_date = models.DateField()
    slug = models.SlugField(max_length=40, default='ERROR_SLUGIFY')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.pk :
            self.create_date = timezone.now().date()
        super(Room, self).save(*args, **kwargs)
