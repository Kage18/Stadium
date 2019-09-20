endpoint: /graphql/

##registration

mutation {
  createUser(username:"", email:"" ,password:""){
    user{
      username
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

