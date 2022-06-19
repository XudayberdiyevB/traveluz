from django.db import models
from django.core.exceptions import ValidationError
from cities.models import City
from django.contrib.auth.models import User

class Route(models.Model):
    passenger=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,unique=True,verbose_name='Route number')
    travel_times=models.PositiveSmallIntegerField(verbose_name='Route time travel')
    from_city=models.ForeignKey(City,on_delete=models.CASCADE,
                                related_name='route_from_city_set',verbose_name='Qaysi shaxardan')
    to_city=models.ForeignKey(City,on_delete=models.CASCADE,
                                related_name='route_to_city_set',verbose_name='Qaysi shaxarga')
    trains=models.ManyToManyField('trains.Train',verbose_name='Train list')
    ticket_number=models.IntegerField(default=0)

    def __str__(self):
        return f'Route {self.name}'

    class Meta:
        verbose_name='Route'
        verbose_name_plural='Routes'
        ordering=['travel_times']


