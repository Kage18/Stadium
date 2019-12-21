from users.models import User, CustomerProfile
from utils.graphql_test_utils import APITestCase
from .graphql_request import *


class UserTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.dummy_user = User.objects.create(
            username="dummy_user",
            password="dummy_password"
        )
        self.dummy_customerprofile = CustomerProfile.objects.create(
            DOB="1999-03-18",
            gender=1,
            phone_no="9340143387",
            Customer=self.dummy_user
        )
    # def test_create_user(self):
    #     self.snapshot_graphql_request(
    #         request_string=Create_User,
    #         variables={},
    #     )

    def test_user(self):
        self.snapshot_graphql_request(
            request_string=List_Users,
            variables={},
        )

    def test_customerprofile(self):
        self.snapshot_graphql_request(
            request_string=List_Customerprofile,
            variables={},
        )

    # def test_user_authentication(self):
    #     self.snapshot_graphql_request(
    #         request_string=user_auth,
    #         variables={"Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjE4a3VzaGFsamFpbkBnbWFpbC5jb20iLCJleHAiOjE1NzM5MjU1MDYsIm9yaWdfaWF0IjoxNTczOTI1MjA2fQ.USnwH8DiIVOusfrR2VmxN0DnEkgG5dniGi_TP5O8qQY",}
    #     )


    # def test_games(self):

    # def test_create_link_user_logged_in(self):
    #     self.snapshot_graphql_request(
    #         request_string=CREATE_LINK_MUTATION,
    #         variables={"url": "example.com", "desc": "example link"},
    #         context={
    #             "user": self.dummy_user,
    #         }
    #     )