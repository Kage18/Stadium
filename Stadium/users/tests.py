# import json
# from django.test import TestCase
# from django.test import Client
# from Stadium.schema import schema
# # Inherit from this in your test cases
# class GraphQLTestCase(TestCase):

#     def setUp(self):
#         self._client = Client()

#     def query(self, query: str, op_name: str = None, input: dict = None):
#         '''
#         Args:
#             query (string) - GraphQL query to run
#             op_name (string) - If the query is a mutation or named query, you must
#                                supply the op_name.  For annon queries ("{ ... }"),
#                                should be None (default).
#             input (dict) - If provided, the $input variable in GraphQL will be set
#                            to this value

#         Returns:
#             dict, response from graphql endpoint.  The response has the "data" key.
#                   It will have the "error" key if any error happened.
#         '''
#         body = {'query': query}
#         # if op_name:
#         #     body['operation_name'] = op_name
#         # if input:
#         #     body['variables'] = {'input': input}
#         # print(json.dumps(body))
#         print('query: ',query)
#         resp = self._client.post('/graphql/', {'query': query},
#                                  content_type='application/json')
#         jresp = resp.content.decode()
#         print('resp:',jresp)
#         return jresp

#     def assertResponseNoErrors(self, resp: dict, expected: dict):
#         '''
#         Assert that the resp (as retuened from query) has the data from
#         expected
#         '''
#         # self.assertNotIn('errors', resp, 'Response had errors')
#         self.assertEqual(resp['data'], expected, 'Response has correct data')

#     def test_login_mutation_successful(self):
#         # User.objects.create(username='test', password='hunter2')
#         resp = self.query(
#             # The mutation's graphql code
#             '''query {
#   users{
#     id
#     username
#     email
#   }
# }
#             ''',
#             # The operation name (from the 1st line of the mutation)
#             # op_name='tokenAuth',
#             # input={'username': 'test', 'password': 'hunter2'}
#         )
#         self.assertResponseNoErrors(resp,  {
#     "tokenAuth": {
#       "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImhhcnNoaXQiLCJleHAiOjE1NjkzNDQ2NjIsIm9yaWdfaWF0IjoxNTY5MzQ0MzYyfQ.YQTyfj7fXv1eCiJz8ez25dbA2-ZhtYensf7OuPQs-fI"
#     }
#   })
# from django.test import RequestFactory, TestCase
# from graphene.test import Client
# from django.test import Client
# from Stadium.schema import schema
# def execute_test_client_api_query(api_query, user=None, variable_values=None, **kwargs):
#     """
#     Returns the results of executing a graphQL query using the graphene test client.  This is a helper method for our tests
#     """
#     request_factory = RequestFactory()
#     context_value = request_factory.get('/graphql/')
#     context_value.user = user
#     client = Client(schema)
#     executed = client.execute(api_query, context_value=context_value, variable_values=variable_values, **kwargs)
#     return executed

# class APITest(TestCase):
#     def test_accounts_queries(self):
#         # This is the test method.
#         # Let's assume that there's a user object "my_test_user" that was already setup
#         query = '''query {
#   users{
#     id
#     username
#     email
#   }
# }
# '''
#         executed = execute_test_client_api_query(query)
#         data = executed.get('data')
#         print(data)
#         self.assertEqual(data, {
#     "users": [
#       {
#         "id": "1",
#         "username": "Kushal",
#         "email": "something@random.com"
#       },
#       {
#         "id": "2",
#         "username": "Kushal1",
#         "email": "something@random.com"
#       },
#       {
#         "id": "3",
#         "username": "kage",
#         "email": ""
#       },
#       {
#         "id": "4",
#         "username": "",
#         "email": ""
#       },
#       {
#         "id": "5",
#         "username": "ksge1",
#         "email": ""
#       },
#       {
#         "id": "6",
#         "username": "harshit",
#         "email": ""
#       },
#       {
#         "id": "7",
#         "username": "harshit1",
#         "email": ""
#       }
#     ]
#   })

# client = Client(schema)

# print(client.post('/graphql/',{'query':'''mutation {
#   tokenAuth(username: "harshit", password: "1234"){
#     token
#   }
# }'''}).content.decode())
# '/graphql/', json.dumps(body),
# #                                  content_type='application/json'
# header = {'HTTP_AUTHORIZATION': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImhhcnNoaXQiLCJleHAiOjE1NjkzNTMxNzMsIm9yaWdfaWF0IjoxNTY5MzUyODczfQ.XXMOI8CfIa3T73brzeq2XCTD1JxRqrkyqqDcgZPs5qA'}
# print(client.post('/graphql/',{'query':'''query{
#   me{
#     id
#     username
#   }
# }'''},Content_type='application/json',**header).content.decode())

from django.test import TestCase, Client
from django.contrib.auth.models import User

class APITest(TestCase):

  def setup(self):
    self.client = Client()
  

  def test_token(self):
    # User.objects.create(username='test', password='hunter2')
    # client = Client()
    resp = self.client.post('/graphql/',{'query':'''mutation {tokenAuth(username: "harshit", password: "1234"){token}}'''}).content.decode()
    # resp = client.post('/graphql/',{'query':'''mutation {tokenAuth(username:"test", password:"hunter2"){token}}'''}).content.decode()
    print(resp)

# client = Client()
# # resp = self.client.post('/graphql/',{'query':'''mutation {tokenAuth(username: "harshit", password: "1234"){token}}'''}).content.decode()
# resp = client.post('/graphql/',{'query':'''mutation {tokenAuth(username: "harshit", password: "1234"){token}}'''}).content.decode()
# print(resp)