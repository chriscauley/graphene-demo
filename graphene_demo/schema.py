from graphene_django import DjangoObjectType
import graphene

from graphene_demo.models import Animal

class AnimalNode(DjangoObjectType):
  class Meta:
    model = Animal

class Query(graphene.ObjectType):
  animals = graphene.List(AnimalNode)

  @graphene.resolve_only_args
  def resolve_animals(self):
    return Animal.objects.all()

schema = graphene.Schema(query=Query)
