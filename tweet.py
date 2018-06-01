from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords
import tweepy
import pairs
import search
import re


def remove_stop_words(text):
    stop_words = stopwords.words("english")
    return ' '.join([word for word in text.split() if word not in stop_words])


def reply(auth, tweet):
    api = tweepy.API(auth)
    pattern = re.compile('(.*) (would like to know|would like find|trying to find) (.*)')
    try:
        tweetId = tweet.id
        username = tweet.user.screen_name
        if pattern.match(tweet):
            tweet = remove_stop_words(tweet)
            result = search.search_guides(tweet)
            api.update_status("@" + username + " " + result, in_reply_to_status_id=tweetId)
        else:
            text = tweet.text
            text = text.replace('@starlord_p ', '')
            phrase = Chat(pairs.eliza(), reflections).respond(text)
            api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
            print("Tweet : " + text)
            print("Replied with : " + phrase)
    except tweepy.TweepError as e:
        print(e.reason)

