# Generated by Django 2.2.7 on 2019-11-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0003_entry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='mood',
            field=models.CharField(choices=[('VH', 'Very Happy'), ('H', 'Happy'), ('N', 'Neutral'), ('S', 'Sad'), ('VS', 'Very Sad'), ('A', 'Angry')], default='Neutral', max_length=12),
        ),
    ]
