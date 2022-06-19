from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train name')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set')
    start_train_day = models.DateField(null=True, blank=True)
    start_train_time = models.TimeField(null=True, blank=True)
    end_train_day = models.DateField(null=True, blank=True)
    place = models.IntegerField(default=0)

    def __str__(self):
        return f'Train N{self.name} and city {self.from_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Cities name must be diffirent !!!')
        qs = Train.objects.filter(name=self.name,
                                  from_city=self.from_city,
                                  to_city=self.to_city,
                                  start_train_day=self.start_train_day,
                                  start_train_time=self.start_train_time,
                                  end_train_day=self.end_train_day)
        if qs.exists():
            raise ValidationError("Information didn't change or this train exists!")

    def save(self, *args, **kwargs):
        self.clean()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'


class TrainTest(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train number')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_shaxar')
