import json
import tweepy

from decouple import config

from google.cloud import pubsub_v1

from google.oauth2 import service_account


# GCP key
key_path = config('KEY_PATH')

credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=['https://www.googleapis.com/auth/cloud-platform'],
)

# Pub/Sub client
client = pubsub_v1.PublisherClient(credentials=credentials)
topic_path = client.topic_path('apt-mark-283207', 'tweets')

# developer.twitter.com 에서 발급 받기
twitter_api_key = config('TWITTER_API_KEY')
twitter_api_secret_key = config('TWITTER_API_SECRET_KEY')
twitter_access_token = config('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')


class SimpleStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        tweet = json.dumps(
            {
                'id': status.id,
                'created_at': status.created_at,
                'text': status.text
            },
            default=str
        )
        client.publish(topic_path, data=tweet.encode('UTF-8'))

    def on_error(self, status_code):
        print(status_code)
        # 420 Enhance Your Calm(Twitter)
        # 429 Too Many Requests(official status code)
        if status_code == 420 or status_code == 429:
            return False


stream_listener = SimpleStreamListener()

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitter_stream = tweepy.Stream(auth, stream_listener)
# 관심 주제로 필터링(예: BTS)
twitter_stream.filter(track=['BTS'])
