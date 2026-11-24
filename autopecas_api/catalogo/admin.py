from django.contrib import admin
from .models import Peca


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
  list_display = (
      'id',
      'sku',
      'nome',
      'categoria',
      'marca',
      'modelo_veiculo',
      'preco',
      'estoque',
  )
  list_filter = ('categoria', 'marca')
  search_fields = ('nome', 'sku', 'modelo_veiculo')
  ordering = ('id',)