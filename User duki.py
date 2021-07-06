import tweepy
import pandas as pd
import random, pickle, time

def create_api():
    consumer_key = "ls5gJffQfrYLXAwCOQ6jBt9TN"   #Claves
    consumer_secret = "TYNLaVYsEKKU1jU6yT4oBT6KCoR9ov33Ne2PFzC4IPu55dg1PS"

    apikey = "1344062997149458434-itFTaGuqwqB1ibw321399Fxsm702sc"
    apikeysecret = "EHFHAEH7nyVVDJpOVvkdrCdv2ZdgDn7G3tflmOQwXSkYW"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Conexiones
    auth.set_access_token(apikey, apikeysecret)
    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    return  api

def duko():
    lista = dp[::]
    rdo = random.choice(lista)
    return rdo

def resp():
    search = "@duki_bot"
    tuits = tweepy.Cursor(api.search, q=search).items(1)
    users_locs = [[tweet.user.screen_name, tweet.text] for tweet in tuits]
    df = pd.DataFrame(data=users_locs, columns=["Usuario", "Texto"])
    if df.Texto[0] == search:
        try:
            jj = api.update_status("@" +str(df.Usuario[0]) + "   " + str(duko()))
        except:
            jj = api.update_status("@" +str(df.Usuario[0]) + "    "+ str(duko()))
    return jj

#Abrir data.
with open("frases.pickle", "rb") as file:
        dp = pickle.load(file)

api = create_api()
while True:
    resp()
    try:
        api.update_status(duko())
    except:
        api.update_status(duko())
    time.sleep(60 * 30)
    








