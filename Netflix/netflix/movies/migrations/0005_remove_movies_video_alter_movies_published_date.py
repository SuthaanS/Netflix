# Generated by Django 5.0.6 on 2024-08-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movies_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='video',
        ),
        migrations.AlterField(
            model_name='movies',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
