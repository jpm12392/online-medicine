# Generated by Django 4.2.3 on 2023-07-11 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_userprescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprescription',
            name='image',
            field=models.FileField(upload_to='prescription/image/'),
        ),
    ]