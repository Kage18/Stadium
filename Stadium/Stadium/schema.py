import graphene
import graphql_jwt

import library.schema
import merch.schema
import users.schema


class Query(users.schema.Query, library.schema.Query, merch.schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
