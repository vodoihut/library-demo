# Generated by Django 2.2 on 2022-05-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sach', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sach',
            name='book_img',
            field=models.CharField(default='', max_length=255),
        ),
    ]
