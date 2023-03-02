import shutil, tempfile
import pandas as pd
from datetime import datetime

from django.test import TestCase, override_settings
from django.conf import settings
from cnpj.models import CnpjCei
from cnpj.spreedsheets.processing_rfb_v1 import ProcessingRfbV1

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class TestProcessingRfbV1(TestCase):

    @classmethod
    def tearDownClass(cls): 
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self) -> None:
        self.cnpj_cei = CnpjCei.objects.create(
            identification_number="37398631000110", type_identification=0
        )
        self.file_update = open(f"{settings.BASE_DIR}/cnpj/tests/files/Test CNPJ Update.xlsx", 'rb')
        self.file_new = open(f"{settings.BASE_DIR}/cnpj/tests/files/Test CNPJ New.xlsx", 'rb')
        self.file_less_column = open(f"{settings.BASE_DIR}/cnpj/tests/files/Test CNPJ less column.xlsx", 'rb')

    
    def test_update_existing_cnpj(self):
        processing_rfb = ProcessingRfbV1(self.file_update)
        processing_rfb.is_valid()
        processing_rfb.save()
        self.cnpj_cei.refresh_from_db()
        self.assertEquals(self.cnpj_cei.fantasy_name, "RESTAURANTE VITORIA 2")


    def test_new_cnpj(self):
        processing_rfb = ProcessingRfbV1(self.file_new)
        processing_rfb.is_valid()
        processing_rfb.save()
        df = pd.read_excel(f"{settings.BASE_DIR}/cnpj/tests/files/Test CNPJ New.xlsx", decimal=",")
        cnpj_list = df["CNPJ"].tolist()
        cnpj_to_search = [self.cnpj_cei.identification_number] + cnpj_list
        cnpj_new = CnpjCei.objects.get(identification_number=cnpj_list[0])
        self.assertEqual(CnpjCei.objects.filter(identification_number__in=cnpj_to_search).count(), 2)
        self.assertEquals(cnpj_new.identification_number, "37398631000119")
        self.assertEquals(cnpj_new.identif_m_f, 0)
        self.assertEquals(cnpj_new.name, "MARCELA ROSA DA SILVA 32337152855")
        self.assertEquals(cnpj_new.fantasy_name, "RESTAURANTE VITORIA 2")
        self.assertEquals(cnpj_new.legal_nature, 0)
        self.assertEquals(cnpj_new.company_size, 0)
        self.assertEquals(cnpj_new.social_capital, 1500.0)
        self.assertEquals(cnpj_new.registration_status, 0)
        self.assertEquals(cnpj_new.date_registration_status, datetime.strptime("2020-06-13 00:00:00", "%Y-%m-%d %H:%M:%S").date())
        self.assertEquals(cnpj_new.reason_situation, 0)
        self.assertEquals(cnpj_new.start_activities, datetime.strptime("2020-06-13 00:00:00", "%Y-%m-%d %H:%M:%S").date())
        self.assertEquals(cnpj_new.main_cnae, "5620104")
        self.assertEquals(cnpj_new.street, "PRESIDENTE GETULIO VARGAS")
        self.assertEquals(cnpj_new.street_number, "943")
        self.assertEquals(cnpj_new.complement_address, '')
        self.assertEquals(cnpj_new.neighborhood, "MOGI MODERNO")
        self.assertEquals(cnpj_new.zipcode, "08715400")
        self.assertEquals(cnpj_new.state, "SP")
        self.assertEquals(cnpj_new.phone, "97099364")
        self.assertEquals(cnpj_new.phone2, '0')
        self.assertEquals(cnpj_new.type_identification, 0)

    def test_less_column_error(self):
        processing_rfb = ProcessingRfbV1(self.file_less_column)
        self.assertFalse(processing_rfb.is_valid())

    