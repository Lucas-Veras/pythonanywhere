# Generated by Django 3.2.3 on 2022-05-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='data_pub',
            field=models.DateTimeField(verbose_name='Data de publicação'),
        ),
    ]
