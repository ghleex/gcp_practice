from decouple import config
import tweepy

# developer.twitter.com 에서 발급 받기
twitter_api_key = config('TWITTER_API_KEY')
twitter_api_secret_key = config('TWITTER_API_SECRET_KEY')
twitter_access_token = config('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')


class SimpleStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)


stream_listener = SimpleStreamListener()

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

twitter_stream = tweepy.Stream(auth, stream_listener)
# 관심 주제로 필터링(예: BTS)
twitter_stream.filter(track=['BTS'])
