# Generated by Django 5.0.2 on 2024-03-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_scraping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='execution',
            name='executon_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
