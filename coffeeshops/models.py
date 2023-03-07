from django.db import models
from django.conf import settings


class Coffeeshop(models.Model):
    name = models.CharField(max_length=64)
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='coffeeshops/', blank=True, null=True)  # TODO CREATE GALLERY
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='coffeeshop_owner', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Game(models.Model):
    coffeeshop = models.ForeignKey(Coffeeshop, related_name='coffeeshop_games', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)  # TODO CHOICE FIELD
    capacity = models.PositiveSmallIntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    game_time = models.DateTimeField()
    status = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    coffeeshop = models.ForeignKey(Coffeeshop, related_name='coffeeshop_comments', on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_comments', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)#for published
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
