# Generated by Django 3.2.18 on 2023-02-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cnpj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cnpjcei',
            name='address',
        ),
        migrations.RemoveField(
            model_name='cnpjcei',
            name='cnae',
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='complement_address',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='fantasy_name',
            field=models.CharField(default=0, max_length=250, verbose_name='Nome Fantasia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='identif_m_f',
            field=models.IntegerField(choices=[(0, 'MATRIZ'), (1, 'FILIAL')], default=0, verbose_name='Identificacao M/F'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='main_cnae',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='motivo_situacao',
            field=models.IntegerField(choices=[(0, 'SEM MOTIVO'), (1, 'EXTINCAO POR ENCERRAMENTO LIQUIDACAO VOLUNTARIA'), (2, 'OMISSAO DE DECLARACOES'), (3, 'INTERRUPCAO TEMPORARIA DAS ATIVIDADES'), (4, 'BAIXA DE PRODUTOR RURAL'), (5, 'PEDIDO DE BAIXA INDEFERIDA'), (6, 'INAPTIDAO (LEI 11.941/2009 ART.54)'), (7, 'EXTINCAO - TRATAMENTO DIFERENCIADO DADO AS ME E EPP (LEI COMPLEMENTAR NUMERO 123/2006)'), (8, 'OMISSAO CONTUMAZ'), (9, 'ENCERRAMENTO DA FALENCIA'), (10, 'BAIXA DEFERIDA PELA RFB AGUARDANDO ANALISE DO CONVENENTE'), (11, 'INCORPORACAO'), (12, 'NAO INICIO DE ATIVIDADE'), (13, 'FUSAO'), (14, 'ELEVACAO A MATRIZ'), (15, 'ANULACAO POR MULTICIPLIDADE'), (16, 'REGISTRO CANCELADO'), (17, 'ANULACAO DE INSCRICAO INDEVIDA'), (18, 'CISAO TOTAL'), (19, 'INEXISTENCIA DE FATO'), (20, 'ANULACAO POR NAO CONFIRMADO ATO DE REGISTRO DO MEI NA JUNTA COMERCIAL'), (21, 'OBITO DO MEI - TITULAR FALECIDO'), (22, 'LOCALIZACAO DESCONHECIDA'), (23, 'ANULACAO POR VICIOS'), (24, 'BAIXA INICIADA EM ANALISE'), (25, 'TRANSPASSE'), (26, 'BAIXA INDEFERIDA PELA RFB E AGUARDANDO ANALISE DO CONVENENTE'), (27, 'INAPTIDAO'), (28, 'DETERMINACAO JUDICIAL'), (29, 'EXTINCAO-UNIFICACAO DA FILIAL'), (30, 'INCONSISTENCIA CADASTRAL'), (31, 'BAIXA DEFERIDA PELA RFB E INDEFERIDA PELO CONVENENTE'), (32, 'PRATICA IRREGULAR DE OPERACAO DE COMERCIO EXTERIOR'), (33, 'EXTINCAO PELO ENCERRAMENTO DA LIQUIDACAO JUDICIAL'), (34, 'ENCERRAMENTO DA LIQUIDACAO')], default=0, verbose_name='Motivo Situação Cadastral'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='natureza_juridica',
            field=models.IntegerField(choices=[(0, 'Empresário (Individual)'), (1, 'Sociedade Empresária Limitada'), (2, 'Produtor Rural (Pessoa Física)'), (3, 'Associação Privada'), (4, 'Candidato a Cargo Político Eletivo'), (5, 'Sociedade Unipessoal de Advocacia'), (6, 'Sociedade em Conta de Participação'), (7, 'Sociedade Anônima Fechada'), (8, 'Sociedade Simples Limitada'), (9, 'Cooperativa'), (10, 'Organização Religiosa'), (11, 'Sociedade Simples Pura'), (12, 'Empresa Individual de Responsabilidade Limitada (de Natureza Empresária)'), (13, 'Sociedade Anônima Aberta'), (14, 'Condomínio Edilício'), (15, 'Sociedade de Economia Mista'), (16, 'Empresa Individual Imobiliária'), (17, 'Empresa Pública'), (18, 'Órgão Público do Poder Judiciário Estadual'), (19, 'Fundação Privada'), (20, 'Órgão Público do Poder Executivo Estadual ou do Distrito Federal'), (21, 'Sociedade Empresária em Nome Coletivo'), (22, 'Município'), (23, 'Serviço Notarial e Registral (Cartório)'), (24, 'Entidade Sindical'), (25, 'Fundo Público da Administração Direta Municipal'), (26, 'Estabelecimento, no Brasil, de Sociedade Estrangeira'), (27, 'Órgão de Direção Local de Partido Político'), (28, 'Autarquia Estadual ou do Distrito Federal'), (29, 'Consórcio de Sociedades'), (30, 'Serviço Social Autônomo'), (31, 'Órgão Público do Poder Executivo Municipal'), (32, 'Autarquia Federal'), (33, 'Sociedade Empresária em Comandita por Ações'), (34, 'Órgão Público do Poder Executivo Federal'), (35, 'Empresa Individual de Responsabilidade Limitada (de Natureza Simples)'), (36, 'Grupo de Sociedades'), (37, 'Autarquia Municipal'), (38, 'Fundação Pública de Direito Privado Municipal'), (39, 'Estabelecimento, no Brasil, de Fundação ou Associação Estrangeiras'), (40, 'Sociedade Mercantil de Capital e Indústria'), (41, 'Empresa Simples de Inovação'), (42, 'Organização Social (OS)'), (43, 'Órgão Público do Poder Legislativo Municipal'), (44, 'Entidade de Mediação e Arbitragem'), (45, 'Natureza Jurídica não informada'), (46, 'Consórcio Público de Direito Público (Associação Pública)')], default=0, verbose_name='Natureza Juridica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='neighborhood',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='porte',
            field=models.IntegerField(choices=[(0, 'ME'), (1, 'EPP'), (2, 'OUTROS')], default=0, verbose_name='Porte'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='situacao_cadastral',
            field=models.IntegerField(choices=[(0, 'ATIVA'), (1, 'BAIXADA'), (2, 'INAPTA'), (3, 'SUSPENSA'), (4, 'NULA')], default=0, verbose_name='Situação Cadastral'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='state',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='street',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='street_number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cnpjcei',
            name='zipcode',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='ccm',
            field=models.CharField(max_length=10, verbose_name='CCM'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cnpjcei',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='Telefone'),
        ),
    ]
