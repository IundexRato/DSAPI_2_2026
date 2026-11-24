from django.db.models import Q
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Peca
from .serializers import PecaSerializer


class PecaViewSet(viewsets.ModelViewSet):
  """
    Endpoints padrão gerados automaticamente (5 endpoints):
    1. POST   /api/pecas/          -> Criar
    2. GET    /api/pecas/          -> Listar
    3. GET    /api/pecas/<id>/     -> Detalhar por ID
    4. PUT    /api/pecas/<id>/     -> Atualizar completo
    5. DELETE /api/pecas/<id>/     -> Deletar
    """

  queryset = Peca.objects.all().order_by('id')
  serializer_class = PecaSerializer

  # 6. GET /api/pecas/categoria/<categoria>/
  @action(
      detail=False,
      methods=['get'],
      url_path=r'categoria/(?P<categoria>[^/.]+)',
  )
  def por_categoria(self, request, categoria=None):
    pecas = self.get_queryset().filter(categoria__iexact=categoria)
    serializer = self.get_serializer(pecas, many=True)
    return Response(serializer.data)

  # 7. GET /api/pecas/marca/<marca>/
  @action(detail=False, methods=['get'], url_path=r'marca/(?P<marca>[^/.]+)')
  def por_marca(self, request, marca=None):
    pecas = self.get_queryset().filter(marca__iexact=marca)
    serializer = self.get_serializer(pecas, many=True)
    return Response(serializer.data)

  # 8. GET /api/pecas/preco-faixa/?min=50.00&max=250.00
  @action(detail=False, methods=['get'], url_path='preco-faixa')
  def por_faixa_preco(self, request):
    preco_min = request.query_params.get('min')
    preco_max = request.query_params.get('max')

    pecas = self.get_queryset()
    try:
      if preco_min is not None:
        pecas = pecas.filter(preco__gte=preco_min)
      if preco_max is not None:
        pecas = pecas.filter(preco__lte=preco_max)
    except Exception:
      return Response(
          {'erro': 'Parâmetros min e max devem ser valores numéricos válidos.'},
          status=status.HTTP_400_BAD_REQUEST,
      )

    serializer = self.get_serializer(pecas, many=True)
    return Response(serializer.data)

  # 9. GET /api/pecas/compatibilidade/?modelo=Gol
  @action(detail=False, methods=['get'], url_path='compatibilidade')
  def por_compatibilidade(self, request):
    modelo = request.query_params.get('modelo', '').strip()
    if not modelo:
      return Response(
          {'erro': 'Informe o parâmetro ?modelo='},
          status=status.HTTP_400_BAD_REQUEST,
      )

    pecas = self.get_queryset().filter(modelo_veiculo__icontains=modelo)
    serializer = self.get_serializer(pecas, many=True)
    return Response(serializer.data)

  # 10. GET /api/pecas/busca/?q=pastilha
  @action(detail=False, methods=['get'], url_path='busca')
  def busca_textual(self, request):
    termo = request.query_params.get('q', '').strip()
    if not termo:
      return Response(
          {'erro': 'Informe o parâmetro ?q='},
          status=status.HTTP_400_BAD_REQUEST,
      )

    pecas = self.get_queryset().filter(
        Q(nome__icontains=termo) | Q(sku__icontains=termo)
    )
    serializer = self.get_serializer(pecas, many=True)
    return Response(serializer.data)