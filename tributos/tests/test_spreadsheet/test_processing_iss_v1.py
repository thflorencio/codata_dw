import shutil, tempfile
from django.test import TestCase, override_settings
from django.conf import settings

from tributos.spreadsheet.processing_iss_v1 import ProcessingIssV1
from tributos.tests.files.cnpj_fixtures import CNPJS
from tributos.models import Iss
from cnpj.models import CnpjCei


MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestProcessing_Iss_v1(TestCase):

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        CnpjCei.objects.all().delete()
        Iss.objects.all().delete()
        super().tearDownClass()

    def setUp(self) -> None:
        self.file_new = open(
            f"{settings.BASE_DIR}/tributos/tests/files/Teste ISS.xlsx", "rb"
        )
        for i in CNPJS:
            CnpjCei.objects.create(identification_number=i[0], name=i[1])
        
    
    def test_generate_df(self):
        processing_iss_v1 = ProcessingIssV1(self.file_new)
        df = processing_iss_v1.generate_df()
        self.assertTrue(len(df)==120)
        del(processing_iss_v1)

    def test_is_valid(self):
        processing_iss_v1 = ProcessingIssV1(self.file_new)
        is_valid = processing_iss_v1.is_valid()
        self.assertTrue(is_valid)
        del(processing_iss_v1)

    def test_save(self):
        processing_iss_v1 = ProcessingIssV1(self.file_new)
        processing_iss_v1.is_valid()
        self.assertIsNone(processing_iss_v1.save())
        self.assertEqual(Iss.objects.count(), 120)
        del(processing_iss_v1)