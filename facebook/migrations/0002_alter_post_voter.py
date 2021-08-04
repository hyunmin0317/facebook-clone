# Generated by Django 3.2.6 on 2021-08-04 04:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='voter',
            field=models.ManyToManyField(blank=True, null=True, related_name='voter_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
