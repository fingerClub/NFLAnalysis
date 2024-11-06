from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
#connect to yahoo api

sc  = OAuth2(None, None, from_file='keys.json')

#get game object
gm = yfa.Game()