import graphene
from graphene_django import DjangoObjectType

from estados.models import Estado

class EstadoType(DjangoObjectType):
    class Meta:
        model = Estado

class Query(graphene.ObjectType):
    estados = graphene.List(EstadoType)

    def resolve_estados(self, info, **kwargs):
        return Estado.objects.all()