import graphene

import estados.schema
import municipios.schema

class Query(estados.schema.Query, municipios.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)