from rest_framework.test import APITestCase
from rest_framework import status
from .models import Feira
from .serializer import FeiraSerializer

class FeirasTest(APITestCase):
	URL_PREFIX = 'http://localhost:8000/'
	FORMAT = 'json'

	def setUp(self):
		self.create_feira()

	def create_feira(self):
		feira = self.mock_feira()
		feira.save()

	def test_create_feira(self):
		response = self.client.post(self.URL_PREFIX + 'feiras/feira/', FeiraSerializer(self.mock_feira()).data)
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)

	def test_update_feira(self):
		id = 1
		feira_field_to_update = {"long":'3'}
		response = self.client.put(self.URL_PREFIX + 'feiras/{0}'.format(id), feira_field_to_update, format=self.FORMAT)
		feira = Feira.objects.get(id=id)
		self.assertEquals(feira.long, feira_field_to_update['long'])
		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def test_list(self):
		response = self.client.get(self.URL_PREFIX + 'feiras/',  format=self.FORMAT)
		self.assertEquals(FeiraSerializer(self.mock_feira()).data, response.json()[0])

	def test_get_feira_by_distrito(self):
		response = self.client.get(self.URL_PREFIX + 'feiras/feira/distrito/1/', format=self.FORMAT)
		self.assertEquals(FeiraSerializer(self.mock_feira()).data, response.json()[0])

	def test_get_feira_by_regiao5(self):
		response = self.client.get(self.URL_PREFIX + 'feiras/feira/regiao5/1/', format=self.FORMAT)
		self.assertEquals(FeiraSerializer(self.mock_feira()).data, response.json()[0])

	def test_get_feira_by_nome_feira(self):
		response = self.client.get(self.URL_PREFIX + 'feiras/feira/nome_feira/1/', format=self.FORMAT)
		self.assertEquals(FeiraSerializer(self.mock_feira()).data, response.json()[0])

	def test_get_feira_by_bairro(self):
		response = self.client.get(self.URL_PREFIX + 'feiras/feira/bairro/1/', format=self.FORMAT)
		self.assertEquals(FeiraSerializer(self.mock_feira()).data, response.json()[0])

	def test_delete_feira(self):
		self.assertTrue(len(Feira.objects.filter(id=1)) > 0)
		response = self.client.delete(self.URL_PREFIX + 'feiras/1', format=self.FORMAT)
		self.assertFalse(len(Feira.objects.filter(id=1)) > 0)
		self.assertEquals(response.status_code, status.HTTP_200_OK)

	def mock_feira(self):
		return Feira(id="1",
					 long="1",
					 lat="1",
					 set_cens="1",
					 areap="1",
					 cod_dist="1",
					 distrito="1",
					 cod_sub_pref="1",
					 sub_prefe="1",
					 regiao5="1",
					 regiao8="1",
					 nome_feira="1",
					 registro="1",
					 logradouro="1",
					 numero="1",
					 bairro="1",
					 referecia="1")