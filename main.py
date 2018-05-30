# Peter Quill Twitter bot @starlord_p
# https://twitter.com/starlord_p/

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import keys
import tweet


class Listener(StreamListener):

    def on_status(self, data):
        print(data)
        tweet.reply(auth, data)
        return (True)

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    cfg = keys.cfg_keys()
    auth = OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])

    twitterStream = Stream(auth, Listener())
    twitterStream.filter(track=["@starlord_p"])
