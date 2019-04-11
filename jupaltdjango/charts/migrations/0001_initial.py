# Generated by Django 2.2 on 2019-04-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('solution', models.CharField(max_length=254)),
                ('sector', models.CharField(max_length=254)),
                ('co2_reduction', models.CharField(help_text='TOTAL ATMOSPHERIC CO2-EQ REDUCTION (GT)', max_length=254)),
                ('net_cost', models.CharField(help_text='Net Cost (BILLIONS US $)', max_length=254)),
                ('savings', models.CharField(help_text='BILLIONS US $', max_length=254)),
            ],
        ),
    ]
