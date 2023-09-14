import tweepy

# Configure suas credenciais da API do Twitter
consumer_key = 'SUA_CONSUMER_KEY'
consumer_secret = 'SUA_CONSUMER_SECRET'
access_token = 'SEU_ACCESS_TOKEN'
access_token_secret = 'SEU_ACCESS_TOKEN_SECRET'

# Autenticação na API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criar objeto da API do Twitter
api = tweepy.API(auth)

# Nome do usuário do Twitter para obter os tweets
nome_usuario = 'usuario_twitter'

try:
    # Obter os últimos tweets do usuário
    tweets = api.user_timeline(screen_name=nome_usuario, count=10)

    # Exibir os tweets
    for tweet in tweets:
        print(tweet.text)
        print('------------------')

except tweepy.TweepError as e:
    print(f"Erro ao obter os tweets: {e}")
