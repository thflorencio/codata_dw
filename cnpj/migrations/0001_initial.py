# Generated by Django 3.2.18 on 2023-03-02 20:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CnpjCei",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ccm",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="CCM"
                    ),
                ),
                (
                    "identification_number",
                    models.CharField(
                        max_length=14, verbose_name="Número de Identificação"
                    ),
                ),
                (
                    "identif_m_f",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "MATRIZ"), (1, "FILIAL")],
                        null=True,
                        verbose_name="Identificacao M/F",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Nome")),
                (
                    "fantasy_name",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Nome Fantasia",
                    ),
                ),
                (
                    "legal_nature",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "Empresário (Individual)"),
                            (1, "Sociedade Empresária Limitada"),
                            (2, "Produtor Rural (Pessoa Física)"),
                            (3, "Associação Privada"),
                            (4, "Candidato a Cargo Político Eletivo"),
                            (5, "Sociedade Unipessoal de Advocacia"),
                            (6, "Sociedade em Conta de Participação"),
                            (7, "Sociedade Anônima Fechada"),
                            (8, "Sociedade Simples Limitada"),
                            (9, "Cooperativa"),
                            (10, "Organização Religiosa"),
                            (11, "Sociedade Simples Pura"),
                            (
                                12,
                                "Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)",
                            ),
                            (13, "Sociedade Anônima Aberta"),
                            (14, "Condomínio Edilício"),
                            (15, "Sociedade de Economia Mista"),
                            (16, "Empresa Individual Imobiliária"),
                            (17, "Empresa Pública"),
                            (18, "Órgão Público do Poder Judiciário Estadual"),
                            (19, "Fundação Privada"),
                            (
                                20,
                                "Órgão Público do Poder Executivo Estadual ou do Distrito Federal",
                            ),
                            (21, "Sociedade Empresária em Nome Coletivo"),
                            (22, "Município"),
                            (23, "Serviço Notarial e Registral (Cartório)"),
                            (24, "Entidade Sindical"),
                            (25, "Fundo Público da Administração Direta Municipal"),
                            (
                                26,
                                "Estabelecimento, no Brasil, de Sociedade Estrangeira",
                            ),
                            (27, "Órgão de Direção Local de Partido Político"),
                            (28, "Autarquia Estadual ou do Distrito Federal"),
                            (29, "Consórcio de Sociedades"),
                            (30, "Serviço Social Autônomo"),
                            (31, "Órgão Público do Poder Executivo Municipal"),
                            (32, "Autarquia Federal"),
                            (33, "Sociedade Empresária em Comandita por Ações"),
                            (34, "Órgão Público do Poder Executivo Federal"),
                            (
                                35,
                                "Empresa Individual de Responsabilidade Limitada (de Natureza Simples)",
                            ),
                            (36, "Grupo de Sociedades"),
                            (37, "Autarquia Municipal"),
                            (38, "Fundação Pública de Direito Privado Municipal"),
                            (
                                39,
                                "Estabelecimento, no Brasil, de Fundação ou Associação Estrangeiras",
                            ),
                            (40, "Sociedade Mercantil de Capital e Indústria"),
                            (41, "Empresa Simples de Inovação"),
                            (42, "Organização Social (OS)"),
                            (43, "Órgão Público do Poder Legislativo Municipal"),
                            (44, "Entidade de Mediação e Arbitragem"),
                            (45, "Natureza Jurídica não informada"),
                            (
                                46,
                                "Consórcio Público de Direito Público (Associação Pública)",
                            ),
                        ],
                        null=True,
                        verbose_name="Natureza Juridica",
                    ),
                ),
                (
                    "company_size",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "ME"), (1, "EPP"), (2, "OUTROS")],
                        null=True,
                        verbose_name="Porte",
                    ),
                ),
                (
                    "social_capital",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                (
                    "registration_status",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "ATIVA"),
                            (1, "BAIXADA"),
                            (2, "INAPTA"),
                            (3, "SUSPENSA"),
                            (4, "NULA"),
                        ],
                        null=True,
                        verbose_name="Situação Cadastral",
                    ),
                ),
                (
                    "date_registration_status",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data do Status do Registro"
                    ),
                ),
                (
                    "reason_situation",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "SEM MOTIVO"),
                            (1, "EXTINCAO POR ENCERRAMENTO LIQUIDACAO VOLUNTARIA"),
                            (2, "OMISSAO DE DECLARACOES"),
                            (3, "INTERRUPCAO TEMPORARIA DAS ATIVIDADES"),
                            (4, "BAIXA DE PRODUTOR RURAL"),
                            (5, "PEDIDO DE BAIXA INDEFERIDA"),
                            (6, "INAPTIDAO (LEI 11.941/2009 ART.54)"),
                            (
                                7,
                                "EXTINCAO - TRATAMENTO DIFERENCIADO DADO AS ME E EPP (LEI COMPLEMENTAR NUMERO 123/2006)",
                            ),
                            (8, "OMISSAO CONTUMAZ"),
                            (9, "ENCERRAMENTO DA FALENCIA"),
                            (
                                10,
                                "BAIXA DEFERIDA PELA RFB AGUARDANDO ANALISE DO CONVENENTE",
                            ),
                            (11, "INCORPORACAO"),
                            (12, "NAO INICIO DE ATIVIDADE"),
                            (13, "FUSAO"),
                            (14, "ELEVACAO A MATRIZ"),
                            (15, "ANULACAO POR MULTICIPLIDADE"),
                            (16, "REGISTRO CANCELADO"),
                            (17, "ANULACAO DE INSCRICAO INDEVIDA"),
                            (18, "CISAO TOTAL"),
                            (19, "INEXISTENCIA DE FATO"),
                            (
                                20,
                                "ANULACAO POR NAO CONFIRMADO ATO DE REGISTRO DO MEI NA JUNTA COMERCIAL",
                            ),
                            (21, "OBITO DO MEI - TITULAR FALECIDO"),
                            (22, "LOCALIZACAO DESCONHECIDA"),
                            (23, "ANULACAO POR VICIOS"),
                            (24, "BAIXA INICIADA EM ANALISE"),
                            (25, "TRANSPASSE"),
                            (
                                26,
                                "BAIXA INDEFERIDA PELA RFB E AGUARDANDO ANALISE DO CONVENENTE",
                            ),
                            (27, "INAPTIDAO"),
                            (28, "DETERMINACAO JUDICIAL"),
                            (29, "EXTINCAO-UNIFICACAO DA FILIAL"),
                            (30, "INCONSISTENCIA CADASTRAL"),
                            (
                                31,
                                "BAIXA DEFERIDA PELA RFB E INDEFERIDA PELO CONVENENTE",
                            ),
                            (32, "PRATICA IRREGULAR DE OPERACAO DE COMERCIO EXTERIOR"),
                            (33, "EXTINCAO PELO ENCERRAMENTO DA LIQUIDACAO JUDICIAL"),
                            (34, "ENCERRAMENTO DA LIQUIDACAO"),
                        ],
                        null=True,
                        verbose_name="Motivo Situação Cadastral",
                    ),
                ),
                (
                    "start_activities",
                    models.DateField(
                        blank=True, null=True, verbose_name="Inicio das Atividades"
                    ),
                ),
                (
                    "main_cnae",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Principal CNAE",
                    ),
                ),
                (
                    "type_street",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (0, "AVENIDA"),
                            (1, "RUA"),
                            (2, "ESTRADA"),
                            (3, "VIELA"),
                            (4, "RODOVIA"),
                            (5, "ALAMEDA"),
                            (6, "ENTRADA"),
                            (7, "TRAVESSA"),
                            (8, "PRACA"),
                            (9, "ACESSO"),
                            (10, "RESIDENCIAL"),
                            (11, "ESTRADA MUNICIPAL"),
                            (12, "ESTRADA PARTICULAR"),
                            (13, ""),
                            (14, "VEREDA"),
                            (15, "VIA"),
                            (16, "FAZENDA"),
                            (17, "TREVO"),
                            (18, "LARGO"),
                            (19, "SETOR"),
                            (20, "SITIO"),
                            (21, "PASSARELA"),
                            (22, "PRAÇA"),
                            (23, "ACAMPAMENTO"),
                            (24, "RUA PRINCIPAL"),
                            (25, "LOTEAMENTO"),
                            (26, "3O ALTO"),
                            (27, "ANTIGA ESTRADA"),
                            (28, "5A RUA"),
                            (29, "ESTRADA VELHA"),
                            (30, "RUA PARTICULAR"),
                            (31, "AREA"),
                            (32, "10A RUA"),
                            (33, "CONDOMINIO"),
                            (34, "1A RUA"),
                            (35, "CHACARA"),
                            (36, "OUTROS"),
                            (37, "COLÔNIA"),
                            (38, "RUA PROJETADA"),
                            (39, "VILA"),
                            (40, "1A AVENIDA"),
                            (41, "DISTRITO"),
                            (42, "CAMINHO"),
                            (43, "ACESSO LOCAL"),
                            (44, "RAMAL"),
                            (45, "11A RUA"),
                            (46, "1A TRAV. DA RODOVIA"),
                            (47, "5A TRAVESSA"),
                            (48, "9A RUA"),
                            (49, "COND. RESIDENCIAL"),
                            (50, "ES. PROJETADA"),
                            (51, "6A AVENIDA"),
                            (52, "ESTACAO"),
                            (53, "SÍTIO"),
                            (54, "CONJUNTO"),
                            (55, "12A RUA"),
                            (56, "3A RUA"),
                            (57, "ESTRADA INTERMUNICIP"),
                            (58, "ENTRADA PARTICULAR"),
                            (59, "ÁREA"),
                            (60, "EST. VIC. MUNICIPAL"),
                            (61, "ESTRADA ANTIGA"),
                            (62, "PATIO"),
                            (63, "CONJUNTO HABITACIONA"),
                        ],
                        null=True,
                        verbose_name="Tipo de Logradouro",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True, max_length=250, null=True, verbose_name="Logradouro"
                    ),
                ),
                (
                    "street_number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Numero"
                    ),
                ),
                (
                    "complement_address",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Complemento",
                    ),
                ),
                (
                    "neighborhood",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Bairro"
                    ),
                ),
                (
                    "zipcode",
                    models.CharField(
                        blank=True,
                        max_length=8,
                        null=True,
                        verbose_name="Código Postal",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True, max_length=2, null=True, verbose_name="Estado"
                    ),
                ),
                (
                    "ddd_phone",
                    models.CharField(
                        blank=True, max_length=3, null=True, verbose_name="DDD Telefone"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "ddd_phone2",
                    models.CharField(
                        blank=True,
                        max_length=3,
                        null=True,
                        verbose_name="DDD Telefone 2",
                    ),
                ),
                (
                    "phone2",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Telefone 2"
                    ),
                ),
                (
                    "type_identification",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "CNPJ"), (1, "CEI"), (2, "CAEPF")],
                        null=True,
                        verbose_name="Tipo",
                    ),
                ),
            ],
            options={
                "verbose_name": "CnpjCei",
                "verbose_name_plural": "CnpjCeis",
                "managed": True,
            },
        ),
        migrations.AddIndex(
            model_name="cnpjcei",
            index=models.Index(
                fields=["identification_number"], name="cnpj_cnpjce_identif_27f497_idx"
            ),
        ),
    ]
