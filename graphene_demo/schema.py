from graphene_django import DjangoObjectType,DjangoConnectionField
from graphene_django.filter.fields import DjangoFilterConnectionField
import graphene

from graphene_demo.models import Animal
class AnimalNode(DjangoObjectType):
  class Meta:
    # Assume you have an Animal model defined with the following fields
    model = Animal
    filter_fields = ['name', 'genus', 'is_domesticated']
    interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
  animal = graphene.relay.Node.Field(AnimalNode)
  all_animals = DjangoFilterConnectionField(AnimalNode)

schema = graphene.Schema(query=Query)
