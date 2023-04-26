# Generated by Django 4.2 on 2023-04-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_fertilizer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizer',
            name='type',
            field=models.CharField(choices=[('G', 'General'), ('N', 'High Nitrogen'), ('P', 'High Phosphorous'), ('K', 'High Potassium'), ('W', 'Worm Castings'), ('S', 'Seaweed Extract')]),
        ),
    ]
