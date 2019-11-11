from django.contrib.auth import get_user_model
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Customertype(DjangoObjectType):
    class Meta:
        model = CustomerProfile

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    customer = graphene.List(Customertype)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        DOB = graphene.types.datetime.Date(required = True)
        gender = graphene.Int(required = True)
        phone_no = graphene.Int(required = True)
        bio = graphene.String(default_value = '')
        avatar = graphene.String(default_value = '')

    def mutate(self, info, username, password, email, DOB, gender, phone_no, bio, avatar):
        user = get_user_model()(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        customer = CustomerProfile.objects.get_or_create(
            Customer = user,
            DOB = DOB,
            gender = gender,
            phone_no = phone_no,
            bio = bio,
            avatar = avatar,    
        )



        return CreateUser(user=user, customer = customer)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    customer = graphene.List(Customertype)

    def resolve_users(self, info):
        return get_user_model().objects.all()

    def resolve_customer(self, info):
        return CustomerProfile.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Authentication Failure!')
        return user