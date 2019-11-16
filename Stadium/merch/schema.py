import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import *


class MerchandiseType(DjangoObjectType):
    class Meta:
        model = Merchandise


class MerchImageType(DjangoObjectType):
    url = graphene.String()

    def resolve_url(self, info):
        return self.image.url

    class Meta:
        model = MerchImage


class MerchUserType(DjangoObjectType):
    class Meta:
        model = MerchUser


class Query(ObjectType):
    image = graphene.Field(MerchImageType, id=graphene.Int())
    merch = graphene.Field(MerchandiseType, id=graphene.Int())
    images = graphene.List(MerchImageType)
    merchs = graphene.List(MerchandiseType, name=graphene.String(), game_name=graphene.String())

    def resolve_merchs(self, info, **kwargs):
        name = kwargs.get('name')
        game_name = kwargs.get('game_name')
        if name is not None:
            return Merchandise.objects.filter(name=name)
        if game_name is not None:
            return Merchandise.objects.filter(game=game.objects.filter(name=game_name)[0])

        return Merchandise.objects.all()

    def resolve_image(self, info, **kwargs):
        idd = kwargs.get('id')
        return MerchImage.objects.get(pk=idd)

    def resolve_merch(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Merchandise.objects.get(pk=id)
        return None
