from django.test import TestCase
from cnpj.models import CnpjCei


class TestCnpjCei(TestCase):
    def setUp(self):
        self.cnpj = CnpjCei.objects.create(
            identification_number="57571275002227", type_identification="CNPJ"
        )
        self.cei = CnpjCei.objects.create(
            identification_number="213070034183", type_identification=1
        )
        self.caepf = CnpjCei.objects.create(
            identification_number="31749019800118", type_identification=2
        )

    def test_identification_number_raiz(self):
        self.assertEqual(self.cnpj.identification_number_raiz, "57571275")
        self.assertEqual(self.cei.identification_number_raiz, "0")
        self.assertEqual(self.caepf.identification_number_raiz, "0")
