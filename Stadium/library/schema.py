from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile
from .models import game, tags

class GameType(DjangoObjectType):
  class Meta:
    model = game

class TagType(DjangoObjectType):
  class Meta:
    model = tags

class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    game = graphene.Field(GameType, id = graphene.Int())
    tags = graphene.List(TagType)
    def resolve_games(self, info):
        return game.objects.all()

    def resolve_game(self, info, **kargs):
        id = kargs.get('id')
        return game.objects.get(id = id)