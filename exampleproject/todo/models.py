from django.db import models


class Item(models.Model):
    context = models.TextField(max_length=80)

