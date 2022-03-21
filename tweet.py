import random
import tweepy
# 各APIキー
consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

# OAuth認証
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret,
                                access_token, access_token_secret)
api = tweepy.API(auth)

# ツイート作成。同じ文言だとエラーになるので、ランダムで数字を追加
ran = random.sample(range(999), k=1)
tweet = f"This is a test from local {ran}"

# update_with_mediaメソッドはない→update_status_with_media。tweepyのバージョンに注意

api.update_status_with_media(status=tweet,
                             filename='test_data/SA001.jpeg')
