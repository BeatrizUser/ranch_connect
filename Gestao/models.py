from django.db import models

class Animal(models.Model):
    RACA_CHOICES = (
        ('Angus', 'Angus'),
        ('Brangus', 'Brangus'),
        ('Brahman', 'Brahman'),
        ('Caracu', 'Caracu'),
        ('Charolês', 'Charolês'),
        ('Chianina', 'Chianina'),
        ('Devon', 'Devon'),
        ('Gir', 'Gir'),
        ('Guzerá', 'Guzerá'),
        ('Hereford', 'Hereford'),
        ('Indubrasil', 'Indubrasil'),
        ('Limousin', 'Limousin'),
        ('Marchigiana', 'Marchigiana'),
        ('Montbeliarde', 'Montbeliarde'),
        ('Murray Grey', 'Murray Grey'),
        ('Nelore', 'Nelore'),
        ('Pardo-Suíço', 'Pardo-Suíço'),
        ('Piemontês', 'Piemontês'),
        ('Red Angus', 'Red Angus'),
        ('Santa Gertrudis', 'Santa Gertrudis'),
        ('Senepol', 'Senepol'),
        ('Sindi', 'Sindi'),
        ('Tabapuã', 'Tabapuã'),
        ('Wagyu', 'Wagyu'),
        ('Zebu', 'Zebu'),
    # Adicione outras raças aqui
    )
    PEDIGREE_CHOICES = (
        ('Bisavô Paterno', 'Bisavô Paterno'),
        ('Bisavó Paterna', 'Bisavó Paterna'),
        ('Bisavô Materno', 'Bisavô Materno'),
        ('Bisavó Materna', 'Bisavó Materna'),
        ('Avô Paterno', 'Avô Paterno'),
        ('Avó Paterna', 'Avó Paterna'),
        ('Avô Materno', 'Avô Materno'),
        ('Avó Materna', 'Avó Materna'),
        ('Pai', 'Pai'),
        ('Mãe', 'Mãe'),
        ('Animal', 'Animal'),
    )
    SEXO_CHOICES = (
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
        ('Indefinido', 'Indefinido'),
    )
    numero_identificacao = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    raca = models.CharField(max_length=50, choices=RACA_CHOICES)
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    pedigree = models.CharField(max_length=50, choices=PEDIGREE_CHOICES)
    historico_genetico = models.TextField()
    pai = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='filhos_pai')
    mae = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='filhos_mae')

    def __str__(self):
        return self.numero_identificacao

class Saude(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='saude')
    historico_vacinacao = models.TextField()
    tratamentos = models.TextField()
    exames = models.TextField()

class Reproducao(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='reproducao')
    mae = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True, related_name='filhos')
    pai = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True, blank=True, related_name='descendentes')
    data_cobertura = models.DateField(null=True, blank=True)
    data_inseminacao = models.DateField(null=True, blank=True)
    data_parto = models.DateField(null=True, blank=True)

class Peso(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='pesos')
    data_pesagem = models.DateField()
    peso = models.FloatField()

class Alimentacao(models.Model):
    ALIMENTO_CHOICES = (
    ('Feno', 'Feno'),
    ('Silagem', 'Silagem'),
    ('Grãos', 'Grãos'),
    ('Ração', 'Ração'),
    ('Pastagem', 'Pastagem'),
    ('Sal mineral', 'Sal mineral'),
    ('Suplemento proteico', 'Suplemento proteico'),
    ('Outro', 'Outro'),
)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='alimentacao')
    data_alimentacao = models.DateField()
    tipo_alimento = models.CharField(max_length=50, choices=ALIMENTO_CHOICES)
    quantidade = models.FloatField()

class Movimentacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='movimentacoes')
    data_movimentacao = models.DateField()
    local_origem = models.CharField(max_length=100)
    local_destino = models.CharField(max_length=100)

class Economia(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='economia')
    custo_aquisicao = models.DecimalField(max_digits=10, decimal_places=2)
    custo_alimentacao = models.DecimalField(max_digits=10, decimal_places=2)
    custo_tratamentos = models.DecimalField(max_digits=10, decimal_places=2)
    receita_venda = models.DecimalField(max_digits=10, decimal_places=2)

class Abate(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='abate')
    data_abate = models.DateField()
    peso_carcaca = models.FloatField()
    valor_carcaca = models.DecimalField(max_digits=10, decimal_places=2)
    classificacao_carne = models.CharField(max_length=100)

class Observacao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='observacoes')
    data_observacao = models.DateField()
    texto_observacao = models.TextField()

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
