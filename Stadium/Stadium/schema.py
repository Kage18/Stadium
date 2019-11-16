import graphene
import graphql_jwt

import users.schema, library.schema, merch.schema, transactions.schema

class Query(users.schema.Query, library.schema.Query, merch.schema.Query, graphene.ObjectType):
    pass

class Mutation(transactions.schema.Mutation, users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation) 