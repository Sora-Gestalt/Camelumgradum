# Generated by Django 5.0.2 on 2024-03-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_coffee_bags_cbp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee_bags',
            name='CBP',
            field=models.ImageField(upload_to='CAMELUMGRADUM\\CAMELUMGRADUM\\statics\\Images\\Coffee-Bags2'),
        ),
    ]