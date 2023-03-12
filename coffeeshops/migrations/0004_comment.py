# Generated by Django 4.1.7 on 2023-03-07 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeeshops', '0003_remove_game_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('coffeeshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffeeshop_comments', to='coffeeshops.coffeeshop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]