# Generated by Django 2.1.15 on 2022-04-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldID', models.CharField(max_length=20)),
                ('fieldName', models.CharField(max_length=10)),
                ('fieldlocation', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
    ]
