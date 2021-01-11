import graphene
from graphene_django import DjangoObjectType

from municipios.models import Municipio

class MunicipioType(DjangoObjectType):
    class Meta:
        model = Municipio

class Query(graphene.ObjectType):
    municipios = graphene.List(MunicipioType)

    def resolve_municipios(self, info, **kwargs):
        return Municipio.objects.all()