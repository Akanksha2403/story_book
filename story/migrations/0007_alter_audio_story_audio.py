# Generated by Django 3.2.7 on 2021-10-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0006_remove_books_imgall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='story_audio',
            field=models.FileField(default='', upload_to='audio'),
        ),
    ]
