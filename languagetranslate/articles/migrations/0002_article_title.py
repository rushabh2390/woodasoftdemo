# Generated by Django 3.2.13 on 2022-12-04 08:40

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]