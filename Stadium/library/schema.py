from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile
from .models import game, tags, game_owned, GameImage


class GameType(DjangoObjectType):
    class Meta:
        model = game


class GameImageType(DjangoObjectType):
    url = graphene.String()

    def resolve_url(self, info):
        return self.image.url

    class Meta:
        model = GameImage


class TagType(DjangoObjectType):
    class Meta:
        model = tags


class GameowendType(DjangoObjectType):
    class Meta:
        model = game_owned


class Query(graphene.ObjectType):
    image = graphene.Field(GameImageType, id=graphene.Int())
    images = graphene.List(GameImageType)
    games = graphene.List(GameType)
    game = graphene.Field(GameType, id=graphene.Int())
    tags = graphene.List(TagType)

    game_owned = graphene.List(GameowendType, user_id = graphene.Int(), game_id = graphene.Int())
    # game_owned_by_game = graphene.List(GameowendType, game_id = graphene.Int())

    def resolve_game_owned(self, info, **kargs):
      game_id = kargs.get('game_id')
      user_id = kargs.get('user_id')
      print(game_id and user_id)
      
      if (user_id and game_id) != None:
        return game_owned.objects.filter(game = game_id, customer = user_id)
      elif user_id == None and game_id == None:
        print("here")
        return game_owned.objects.all()
      elif user_id == None:
        return game_owned.objects.filter(game=game_id)
      elif game_id == None:
        return game_owned.objects.filter(customer=user_id)
      

    def resolve_tags(self, info):
        return tags.objects.all()

    def resolve_games(self, info):
        return game.objects.all()

    def resolve_game(self, info, **kargs):
        id = kargs.get('id')
        return game.objects.get(id=id)

    def resolve_image(self, info, **kwargs):
        idd = kwargs.get('id')
        return GameImage.objects.get(pk=idd)