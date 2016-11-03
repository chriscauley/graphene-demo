from django.contrib.auth import get_user_model
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
  @classmethod
  def get_node(cls,id,context,info):
    if context.user.is_authenticated():
      try:
        return Animal.objects.get(user=context.user,id=id)
      except Animal.DoesNotExist:
        pass
    return None
"""
class CurrentUserNode(DjangoObjectType):
  #@classmethod
  #def get_node(cls,id,context,info):
  #  if context.user.is_authenticated():
  #    return context.user
  #  return None
  class Meta:
    model = get_user_model()
    interfaces = (graphene.relay.Node, )
class UserNode(DjangoObjectType):
  class Meta:
    model = get_user_model()
    interfaces = (graphene.relay.Node, )
#"""

class Query(graphene.ObjectType):
  #current_user = graphene.relay.Node.Field(CurrentUserNode)
  animal = graphene.relay.Node.Field(AnimalNode)
  #user = graphene.relay.Node.Field(UserNode)
  all_animals = graphene.List(AnimalNode)
  my_animals = DjangoFilterConnectionField(AnimalNode)
  def resolve_my_animals(self,args,context,info):
    if context.user.is_authenticated():
      return Animal.objects.filter(user=context.user)
    return Animal.objects.none()
  def resolve_all_animals(self,args,context,info):
    return Animal.objects.all()

schema = graphene.Schema(query=Query)
