# Generated by Django 4.0.5 on 2022-06-19 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trains', '0001_initial'),
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route number')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Route time travel')),
                ('ticket_number', models.IntegerField(default=0)),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='Qaysi shaxardan')),
                ('passenger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='Qaysi shaxarga')),
                ('trains', models.ManyToManyField(to='trains.train', verbose_name='Train list')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
                'ordering': ['travel_times'],
            },
        ),
    ]
