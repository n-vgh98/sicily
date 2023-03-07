# Generated by Django 4.1.7 on 2023-03-07 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffeeshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='coffeeshops/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='coffeeshop_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('capacity', models.PositiveSmallIntegerField(default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('game_time', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('coffeeshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffeeshop_games', to='coffeeshops.coffeeshop')),
                ('user', models.ManyToManyField(related_name='users_games', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
