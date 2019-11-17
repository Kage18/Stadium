List_Users = """
query {
  users{
    id
    username
    email
    isVerified
    cus{
      DOB
      gender
      phoneNo
      joined
    }
  }
}
"""
List_Customerprofile = """
query{
  customer{
        Customer{username}
        id
        DOB
        gender
        phoneNo
        bio
        joined
        avatar
      }
}
"""

Create_User ="""
mutation {
  createUser(
      username:"kushal",
      email:"18kushaljain@gmail.com",
      password:"1234",
      DOB:"1999-03-18",
      phoneNo:"9340143387",
      gender: 1,
  ){
    user{username}
  }
}
"""

user_auth="""
query{
  me{
    Customer{username}
        id
        DOB
        gender
        phoneNo
        bio
        joined
        avatar
        friends{
          Customer{
            username
          }
        }
  }
}
"""