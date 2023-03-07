from django.db import models
from django.conf import settings


class Coffeeshop(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField()
    description = models.TextField()
    main_image = models.ImageField(upload_to='coffeeshops/', blank=True, null=True)  # TODO CREATE GALLERY
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='coffeeshop_owner', on_delete=models.DO_NOTHING)


class Game(models.Model):
    coffeeshop = models.ForeignKey(Coffeeshop, related_name='coffeeshop_games', on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='users_games')
    title = models.CharField(max_length=64)  # TODO CHOICE FIELD
    capacity = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    game_time = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
