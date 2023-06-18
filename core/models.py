from django.db import models


class Doador(models.Model):
    ANONIMO_CHOICES = (
        (0, 'Não'),
        (1, 'Sim'),
    )
    TIPO_DOADOR_CHOICES = (
        (0, 'Pessoa Física'),
        (1, 'Pessoa Jurídica de Direito Privado'),
        (2, 'Pessoa Jurídica de Direito Público'),
    )
    LGPD_CHOICES = (
        (0, 'Não Consentido'),
        (1, 'Consentido'),
    )

    anonimo = models.IntegerField(choices=ANONIMO_CHOICES, default=0)
    tipo_doador = models.IntegerField(choices=TIPO_DOADOR_CHOICES, default=0)
    pf_nome = models.CharField(max_length=200, null=True)
    pf_cpf = models.IntegerField(null=True)
    pf_dtnascimento = models.DateTimeField(null=True)
    pf_telefone = models.CharField(max_length=20, null=True)
    pj_desc = models.TextField(max_length=200, null=True)
    pj_cnpj = models.CharField(max_length=200, null=True)
    pj_email = models.EmailField(max_length=200, null=True)
    pj_telefone = models.CharField(max_length=20, null=True)
    pj_cidade = models.CharField(max_length=100, null=True)
    lgpd = models.IntegerField(choices=LGPD_CHOICES, default=0)
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.pf_nome if self.tipo_doador == 0 else self.pj_desc


class Doacao(models.Model):
    FINALIDADE_CHOICES = (
        (0, 'Saúde'),
        (1, 'Educação'),
        (2, 'Santuário'),
        (3, 'Ensino e Pesquisa'),
        (4, 'Sem preferência'),
    )

    TIPO_CHOICES = (
        (0, 'Financeiro'),
        (1, 'Bens Móveis ou Imóveis'),
        (2, 'Serviços'),
        (3, 'Produtos'),
        # Adicione as opções de tipo desejadas
    )

    finalidade = models.IntegerField(choices=FINALIDADE_CHOICES, default=0)
    data = models.DateTimeField(null=True)
    tipo = models.IntegerField(choices=TIPO_CHOICES, default=0)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'Doacao {self.pk}' if self.pk is not None else 'Doacao'


class DoacaoItem(models.Model):
    PAGAMENTO_CHOICES = (
        (0, 'Especie'),
        (1, 'PIX'),
        (2, 'Cartão de Crédito'),
        (3, 'Cartão de Débito'),
        (4, 'Boleto'),
        (5, 'Transferência'),
        (6, 'Depósito'),
        (7, 'Conta de Energia'),
        (8, 'Incentivo'),
    )

    doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE, default=None)
    pagamento = models.IntegerField(choices=PAGAMENTO_CHOICES, default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'DoacaoItem {self.pk}'
