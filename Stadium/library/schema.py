from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile
from .models import game, tags, game_owned, GameImage
from merch.schema import MerchImageType


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
    games = graphene.List(GameType, game_name= graphene.String())
    game = graphene.Field(GameType, id=graphene.Int())
    tags = graphene.List(TagType, tag_name= graphene.String())
    merchimage = graphene.Field(MerchImageType)
    leaderboard = graphene.List(GameowendType, game_id=graphene.Int())
    game_owned = graphene.List(GameowendType, user_id = graphene.Int(), game_id = graphene.Int())
    # game_owned_by_game = graphene.List(GameowendType, game_id = graphene.Int())


    def resolve_leaderboard(self, info, **kwargs):
        game_id = kwargs.get('game_id')
        if game_id is not None:
            gamepk = game.objects.get(pk=game_id)
            return game_owned.objects.filter(game=gamepk).order_by('-hours_played')
        return game_owned.objects.all().order_by('-hours_played')


    def resolve_game_owned(self, info, **kwargs):
      game_id = kwargs.get('game_id')
      user_id = kwargs.get('user_id')
    #   print(game_id and user_id)
      if (user_id and game_id) != None:
        return game_owned.objects.filter(game = game_id, customer = user_id)
      elif user_id == None and game_id == None:
        # print("here")
        return game_owned.objects.all()
      elif user_id == None:
        return game_owned.objects.filter(game=game_id)
      elif game_id == None:
        return game_owned.objects.filter(customer=user_id)
      

    def resolve_tags(self, info, **kwargs):
        tag_name = kwargs.get("tag_name")
        if tag_name is not None:
          return tags.objects.filter(t_name=tag_name)
        return tags.objects.all()

    def resolve_games(self, info,**kwargs):
        game_name = kwargs.get("game_name")
        if game_name is not None:
          return game.objects.filter(name=game_name)
        return game.objects.all()

    def resolve_game(self, info, **kargs):
        id = kargs.get('id')
        return game.objects.get(id=id)

    def resolve_image(self, info, **kwargs):
        idd = kwargs.get('id')
        return GameImage.objects.get(pk=idd)