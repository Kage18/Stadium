from users.models import User, CustomerProfile
from utils.graphql_test_utils import APITestCase
from .graphql_request import *
from library.models import *

class LibraryTestCase(APITestCase):
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
            Customer_id=1
        )
        self.dummy_tag = tags.objects.create(
          t_name="Dummy_tag"
        )
        self.dummy_game = game.objects.create(
          name="Dummy",
          description="DummyDes.",
          price=85,
        ).tags.add(self.dummy_tag)

        self.dummy_gameowend = game_owned.objects.create(
          customer_id = 1,
          game_id = 1

        )

    def test_list_games(self):
        self.snapshot_graphql_request(
            request_string=List_games,
            variables={},
        )

    def test_list_tags(self):
        self.snapshot_graphql_request(
            request_string=List_tags,
            variables={},
        )
    
    def test_gameowed(self):
      self.snapshot_graphql_request(
        request_string= Gameowned,
        variables={"userId":1,"gameId":1}
      )
