from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Feira
from .serializer import FeiraSerializer
import logging

logger = logging.getLogger(__name__)

class FeiraViewSet(viewsets.ViewSet):

    def create_feira(self, request):
        new_feira = FeiraSerializer(data=request.data)
        if new_feira.is_valid():
            new_feira.save()
            return Response(new_feira.data,status=status.HTTP_201_CREATED)
        return Response(new_feira.errors, status=status.HTTP_400_BAD_REQUEST)

    def update_feira(self, request, id):
        response = Feira.objects.filter(id=id).update(**request.data)
        if response == 1:
            return Response({'data': 'Updated'},status=status.HTTP_200_OK)
        elif response == 0:
            return Response({'data': 'Not Updated'}, status=status.HTTP_400_BAD_REQUEST)

    def get_all_feira(self, request):
        feiras = Feira.objects.all()
        return Response(self.serialize(feiras).data)

    def get_feira_by_distrito(self, request, distrito):
        feira = Feira.objects.filter(distrito=distrito)
        return Response(self.serialize(feira).data, status=status.HTTP_200_OK)

    def get_feira_by_regiao5(self, request, regiao5):
        feira = Feira.objects.filter(regiao5=regiao5)
        return Response(self.serialize(feira).data, status=status.HTTP_200_OK)

    def get_feira_by_nome_feira(self, request, nome_feira):
        feira = Feira.objects.filter(nome_feira=nome_feira)
        return Response(self.serialize(feira).data, status=status.HTTP_200_OK)

    def get_feira_by_bairro(self, request, bairro):
        feira = Feira.objects.filter(bairro=bairro)
        return Response(self.serialize(feira).data, status=status.HTTP_200_OK)

    def delete_feira(self, request, id):
        feira_to_delete = Feira.objects.filter(id=id)
        if feira_to_delete.exists():
            feira_to_delete.delete()
            return Response(FeiraSerializer(feira_to_delete).data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def serialize(self, queryset):
        return FeiraSerializer(queryset, many=True)