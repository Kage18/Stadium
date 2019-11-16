from users.models import User
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile, VendorProfile
from .models import Transaction
from library.schema import GameowendType
from library.models import game_owned, game
from merch.schema import MerchUserType
from merch.models import Merchandise, MerchUser
class TransactionType(DjangoObjectType):
    class Meta:
        model = Transaction


class BuyGame(graphene.Mutation):
    transaction = graphene.Field(TransactionType)
    gameowned = graphene.Field(GameowendType)
    
    class Arguments:
        # amount = graphene.Decimal(required=True)
        game_id = graphene.Int(required=True)

    def mutate(self, info, game_id):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        
        customer = CustomerProfile.objects.get(Customer=user)
        thegame = game.objects.get(id=game_id)
        transaction = Transaction(
            amount = int(thegame.price),
            user=customer,
        )   
        transaction.save()
        
        gameowned = game_owned(
            customer=customer,
            game=thegame,
            transaction=transaction,
        )
        gameowned.save()
        
        return BuyGame(transaction=transaction, gameowned=gameowned)
        

class BuyMerch(graphene.Mutation):
    transaction = graphene.Field(TransactionType)
    merchuser = graphene.Field(MerchUserType)
    
    class Arguments:
        # amount = graphene.Decimal(required=True)
        merch_id = graphene.Int(required=True)

    def mutate(self, info, merch_id):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        
        customer = CustomerProfile.objects.get(Customer=user)
        themerch = Merchandise.objects.get(id=merch_id)
        transaction = Transaction(
            amount = int(themerch.price),
            user=customer,
        )   
        transaction.save()
        
        merchuser = MerchUser(
            user=customer,
            merch=themerch,
            transaction=transaction,
        )
        merchuser.save()
        
        return BuyMerch(transaction=transaction, merchuser=merchuser)
        
        # def mutate(self, info, amount, game_id):
        



# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserType)
#     customer = graphene.List(Customertype)
#     vendor = graphene.Field(Vendortype)

#     class Arguments:
#         username = graphene.String(required=True)
#         password = graphene.String(required=True)
#         email = graphene.String(required=True)
#         DOB = graphene.types.datetime.Date(required = True)
#         gender = graphene.Int(required = True)
#         phone_no = graphene.Int(required = True)
#         bio = graphene.String(default_value = '')
#         avatar = graphene.String(default_value = '')

#     def mutate(self, info, username, password, email, DOB, gender, phone_no, bio, avatar):
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#         )
#         user.set_password(password)
#         user.save()

#         customer = CustomerProfile.objects.get_or_create(
#             Customer = user,
#             DOB = DOB,
#             gender = gender,
#             phone_no = phone_no,
#             bio = bio,
#             avatar = avatar,    
#         )
#         send_confirmation_email(email=user.email, username=user.username)
#         return CreateUser(user=user, customer = customer)


class Mutation(graphene.ObjectType):
    buy_game = BuyGame.Field()
    buy_merch = BuyMerch.Field()

# class Query(graphene.ObjectType):
#     me = graphene.Field(UserType)
#     users = graphene.List(UserType)
#     customer = graphene.List(Customertype)

#     def resolve_users(self, info):
#         return get_user_model().objects.all()

#     def resolve_customer(self, info):
#         return CustomerProfile.objects.all()

#     def resolve_me(self, info):
#         user = info.context.user
#         if user.is_anonymous:
#             raise Exception('Authentication Failure!')
#         return user