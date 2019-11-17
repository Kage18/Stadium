from users.models import User, CustomerProfile
from utils.graphql_test_utils import APITestCase
from .graphql_request import *
from library.models import *
from merch.models import Merchandise,MerchUser
from transactions.models import Transaction

class MerchTestCase(APITestCase):
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

        self.dummy_transaction = Transaction.objects.create(
          user_id = 1,
          amount = 15,
        )

        self.dummy_gameowend = game_owned.objects.create(
          customer_id = 1,
          game_id = 1

        )

        self.dummy_merch = Merchandise.objects.create(
          game_id = 1,
          name = "Dummy_name",
          desc = "Dummy_desc",
          price = 15,
        )

        self.dummy_merchuser = MerchUser.objects.create(
          user_id = 1,
          merch_id = 1,
          transaction_id = 1
        )
    def test_list_merch(self):
        self.snapshot_graphql_request(
            request_string=List_merch,
            variables={},
        )

    def test_merchowned(self):
      self.snapshot_graphql_request(
        request_string=Merchowned,
        variables={},
      )
    
