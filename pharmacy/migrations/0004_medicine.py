# Generated by Django 4.2.3 on 2023-07-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_rename_opt_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='medicine/image/')),
                ('price', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'medicines',
                'indexes': [models.Index(fields=['name'], name='medicines_name_017048_idx')],
            },
        ),
    ]
