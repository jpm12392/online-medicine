# Generated by Django 4.2.3 on 2023-07-07 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_user_opt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='opt',
            new_name='otp',
        ),
    ]
