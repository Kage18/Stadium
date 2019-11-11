endpoint: /graphql/

##registration

mutation {
  createUser(
      username:"",
      email:"xy@z.com",
      password:"",
      DOB:"yyyy-mm-dd",
      phoneNo:xxxxxxxxxxxxxxx,
      gender: 0/1/2,
  ){
      user{username},
      customer{
        id
        DOB
        gender
        phoneNo
        bio
        joined
        avatar
      }
  }
}

#Get all users in database

query {
  users{
    id
    username
    email
  }
}

#Get all Customers in database

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


#Get token

mutation {
  tokenAuth(username: "", password: ""){
    token
  }
}

#token verification

mutation{
  verifyToken(
  token: ""
  ) {
    payload
  }
}

#add Authorization header with value "JWT $token" and get current user with

query{
  me{
    id
    username
  }
}

