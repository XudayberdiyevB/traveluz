from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from cities.models import City
from cities import views
from django.urls import reverse, reverse_lazy
from trains.models import Train
from routes.utils import get_graph,dfs_paths
#
# class Simple(TestCase):
#     def setUp(self):
#         City.objects.create(name='K')
#
#     def test_home_AGE(self):
#         r=self.client.get(reverse('cities:home'))
#         # self.assertInEqual(r.status_code,[400,403,500],'Ajoyib')
#         self.assertGreater(r.status_code,1)
#         self.assertTemplateUsed(r,'cities/home.html')
from routes.forms import RouteForm


class AllTest(TestCase):

    def setUp(self) -> None:
        self.city_A =  City.objects.create(name='A')
        self.city_B =  City.objects.create(name='B')
        self.city_C = City.objects.create(name='C')
        self.city_D = City.objects.create(name='D')
        self.city_E = City.objects.create(name='E')
        lst = [
            Train(name='t1', from_city=self.city_A, to_city=self.city_B,
                  travel_time=9),
            Train(name='t2', from_city=self.city_B, to_city=self.city_D,
                  travel_time=8),
            Train(name='t3', from_city=self.city_A, to_city=self.city_C,
                  travel_time=7),
            Train(name='t4', from_city=self.city_C, to_city=self.city_B,
                  travel_time=6),
            Train(name='t5', from_city=self.city_B, to_city=self.city_E,
                  travel_time=3),
            Train(name='t6', from_city=self.city_B, to_city=self.city_A,
                  travel_time=11),
            Train(name='t7', from_city=self.city_A, to_city=self.city_C,
                  travel_time=10),
            Train(name='t8', from_city=self.city_E, to_city=self.city_D,
                  travel_time=5),
            Train(name='t9', from_city=self.city_D, to_city=self.city_E,
                  travel_time=4)
        ]
        Train.objects.bulk_create(lst)
    def test_city_Detail(self):
        response=self.client.get(reverse('cities:detail',kwargs={'pk':self.city_A.pk}))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.resolver_match.func.__name__,views.CityDetailView.as_view().__name__)
        self.assertTemplateUsed(response,'cities/detail.html')


    def test_graph(self):
        qs=Train.objects.all()
        graph=get_graph(qs)
        all_ways=list(dfs_paths(graph,self.city_A.pk,self.city_E.pk))
        self.assertEquals(len(all_ways),4)

    def test_find_route(self):
        data={
            'from_city':self.city_B.pk,
            'to_city':self.city_E.pk,
            'cities':[self.city_C.pk],
            'travelling_time':1,
        }
        form=RouteForm(data=data)
        response=self.client.post('/find_routes/',data)
        self.assertEquals(response.status_code,200)
