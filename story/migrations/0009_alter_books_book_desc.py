# Generated by Django 3.2.7 on 2021-10-09 15:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_alter_books_book_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
