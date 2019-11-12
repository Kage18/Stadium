import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import *


class MerchandiseType(DjangoObjectType):
    class Meta:
        model = Merchandise


class MerchImageType(DjangoObjectType):
    class Meta:
        model = MerchImage


class MerchUserType(DjangoObjectType):
    class Meta:
        model = MerchUser


class Query(ObjectType):
    merch = graphene.Field(MerchandiseType, id=graphene.Int())
    images = graphene.List(MerchImageType)
    merchs = graphene.List(MerchandiseType, name=graphene.String())

    def resolve_merchs(self, info, **kwargs):
        name = kwargs.get('name')
        if name is not None:
            return Merchandise.objects.filter(name=name)
        return Merchandise.objects.all()

    def resolve_merch(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Merchandise.objects.get(pk=id)
        return None