from django.db import models


class Peca(models.Model):
  nome = models.CharField(max_length=150)
  sku = models.CharField(max_length=50, unique=True)
  categoria = models.CharField(max_length=80, db_index=True)
  marca = models.CharField(max_length=80, db_index=True)
  modelo_veiculo = models.CharField(max_length=120)
  preco = models.DecimalField(max_digits=10, decimal_places=2)
  estoque = models.IntegerField(default=0)
  descricao = models.TextField(blank=True, null=True)
  criado_em = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'catalogo_peca'
    verbose_name = 'Peça'
    verbose_name_plural = 'Peças'

  def __str__(self):
    return f'{self.nome} ({self.sku}) - {self.marca}'