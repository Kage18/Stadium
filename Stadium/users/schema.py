from django.contrib.auth import get_user_model
from users.models import User
import graphene
from graphene_django import DjangoObjectType
from users.models import CustomerProfile, VendorProfile, FriendRequest
from users.send_emails import send_confirmation_email


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Customertype(DjangoObjectType):
    class Meta:
        model = CustomerProfile


class Vendortype(DjangoObjectType):
    class Meta:
        model = VendorProfile


class FriendRequestType(DjangoObjectType):
    class Meta:
        model = FriendRequest


class CreateFriendRequest(graphene.Mutation):
    from_user = graphene.Field(Customertype)
    to_user = graphene.Field(Customertype)

    class Arguments:
        to_user_email = graphene.String(required=True)

    def mutate(self, info, to_user_email):
        if info.context.user.is_anonymous:
            raise Exception("Auth nai baya")
        from_user = CustomerProfile.objects.get(Customer=info.context.user)
        to_user = CustomerProfile.objects.get(Customer=User.objects.filter(email=to_user_email)[0])
        search_if_existing = FriendRequest.objects.filter(from_user=to_user, to_user=from_user)
        if len(search_if_existing) != 0:
            f = search_if_existing[0]
            f.from_user.friends.add(to_user)
            f_copy = f
            f.delete()
            return f_copy
        else:
            f_req = FriendRequest.objects.create(from_user=from_user, to_user=to_user)
            f_req.save()
            return f_req


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    customer = graphene.List(Customertype)
    vendor = graphene.Field(Vendortype)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
        DOB = graphene.types.datetime.Date(required=True)
        gender = graphene.Int(required=True)
        phone_no = graphene.String(required=True)
        bio = graphene.String(default_value='')
        avatar = graphene.String(default_value='')

    def mutate(self, info, username, password, email, DOB, gender, phone_no, bio, avatar):
        user = User.objects.create_user(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        customer = CustomerProfile.objects.get_or_create(
            Customer=user,
            DOB=DOB,
            gender=gender,
            phone_no=phone_no,
            bio=bio,
            avatar=avatar,
        )
        send_confirmation_email(email=user.email, username=user.username)
        return CreateUser(user=user, customer=customer)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    send_friend_request = CreateFriendRequest.Field()


class Query(graphene.ObjectType):
    me = graphene.Field(Customertype)
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

        return CustomerProfile.objects.get(Customer=user)
