# Generated by Django 3.1.5 on 2021-03-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_readed',
            field=models.BooleanField(default=False),
        ),
    ]