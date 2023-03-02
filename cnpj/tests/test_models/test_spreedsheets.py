import shutil, tempfile
import pandas as pd

from django.test import TestCase, override_settings
from django.core.files.base import File
from django.conf import settings

from cnpj.models import Spreedsheets, CnpjCei

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestSpreedsheets(TestCase):

    @classmethod
    def tearDownClass(cls): 
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.file = open(f"{settings.BASE_DIR}/cnpj/tests/files/CNPJ DE MOGI- DEZEMBRO 2022 - RFB SMF.xlsx", 'rb')
        self.spreedsheets = Spreedsheets.objects.create(spreedsheet=File(self.file))
        CnpjCei.objects.all().delete()

    def test_process(self):
        self.spreedsheets.process()
        df = pd.read_excel(f"{settings.BASE_DIR}/cnpj/tests/files/CNPJ DE MOGI- DEZEMBRO 2022 - RFB SMF.xlsx", decimal=",")
        self.assertEqual(CnpjCei.objects.filter(identification_number__in=df["CNPJ"].tolist()).count(), 170)