from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Airplane
from .serializers import AirplaneSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_airplane(airplane_id, passengers):
        if airplane_id > 0 and passengers >= 0:
            Airplane.objects.create(airplane_id=airplane_id, passengers=passengers)

    def setUp(self):
        # add test data
        self.create_airplane(1, 1)
        self.create_airplane(2, 2)
        self.create_airplane(3, 5)
        self.create_airplane(4, 2)


class GetAllAirplanesTest(BaseViewTest):

    def test_get_all_planes(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("airplane-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Airplane.objects.all()
        serialized = AirplaneSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
