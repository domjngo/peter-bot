from nltk.chat.util import Chat, reflections
import tweepy
import pairs


def reply(auth, tweet):
    api = tweepy.API(auth)
    try:
        tweetId = tweet.id
        username = tweet.user.screen_name
        text = tweet.text
        text = text.replace('@starlord_p ', '')
        phrase = Chat(pairs.eliza(), reflections).respond(text)
        api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
        print("Tweet : " + text)
        print("Replied with : " + phrase)
    except tweepy.TweepError as e:
        print(e.reason)

