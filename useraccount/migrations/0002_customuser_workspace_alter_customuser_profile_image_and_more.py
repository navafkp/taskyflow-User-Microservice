# Generated by Django 4.1 on 2023-11-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='workspace',
            field=models.CharField(default='admin', max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='manager', max_length=100),
        ),
    ]
