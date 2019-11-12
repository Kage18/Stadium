from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile
from .models import game, tags, game_owned

class GameType(DjangoObjectType):
  class Meta:
    model = game

class TagType(DjangoObjectType):
  class Meta:
    model = tags

class GameowendType(DjangoObjectType):
  class Meta:
    model = game_owned

class Query(graphene.ObjectType):
    games = graphene.List(GameType)
    game = graphene.Field(GameType, id = graphene.Int())
    tags = graphene.List(TagType)
    game_owned_by_user = graphene.List(GameowendType, user_id = graphene.Int())
    game_owned_by_game = graphene.List(GameowendType, game_id = graphene.Int())

    def resolve_game_owned_by_game(self, info, **kargs):
      game_id = kargs.get('game_id')
      return game_owned.objects.filter(game = game_id)

    def resolve_game_owned_by_user(self, info, **kargs):
      user_id = kargs.get('user_id')
      return game_owned.objects.filter(customer = user_id)

    def resolve_tags(self,info):
      return tags.objects.all()

    def resolve_games(self, info):
        return game.objects.all()

    def resolve_game(self, info, **kargs):
        id = kargs.get('id')
        return game.objects.get(id = id)


  

