from rest_framework import serializers
from .models import Peca


class PecaSerializer(serializers.ModelSerializer):

  class Meta:
    model = Peca
    fields = [
        'id',
        'nome',
        'sku',
        'categoria',
        'marca',
        'modelo_veiculo',
        'preco',
        'estoque',
        'descricao',
        'criado_em',
    ]
    read_only_fields = ['id', 'criado_em']