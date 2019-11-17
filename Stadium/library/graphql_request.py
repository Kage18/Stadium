List_games="""
{
  games{
    id
    name
    description
    price
    tags{
      tName
    }
    gameOwnedSet{
      customer{Customer{username}}
      id
    }
  }  
}
"""

List_tags="""
query{
  tags{
    id
    tName
    gameSet{
      id
      name
    }
  }
}
"""

Gameowned="""
query Gameowned($userId:Int!,$gameId:Int!){
  gameOwned(userId:$userId,gameId:$gameId){
          game{
            id  
            name
            images{
              url
            }
            }
            hoursPlayed
            rating
          customer{
            id
            Customer{
              username
              id
            }
          }
        }
}
"""

# Buy_game="""
# mutation{
#   buyGame(gameId:1){
#     transaction{
#       id
#       amount
#       time
#     }
#     gameowned{
#       id
#       customer{Customer{username}}
#     }
    
#   }
# }
# """