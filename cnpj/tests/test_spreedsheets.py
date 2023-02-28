from django.test import TestCase
from django.core.files.base import File
from django.conf import settings

from cnpj.models.spreedsheets import Spreedsheets

class TestSpreedsheets(TestCase):

    def setUp(self):
        file = open(f"{settings.BASE_DIR}/cnpj/tests/files/CNPJ DE MOGI- DEZEMBRO 2022 - RFB SMF.xlsx", 'rb')
        self.spreedsheets = Spreedsheets.objects.create(spreedsheet=File(file))

    def test_process(self):
        self.spreedsheets.process()
        #TODO: Criar testes