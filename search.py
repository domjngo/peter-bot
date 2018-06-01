import feedparser


# Just some sample keywords to search for in the title
key_words = 'army suffragette'


def contains_wanted(query, in_str):
    # returns true if the in_str contains a keyword
    # we are interested in. Case-insensitive
    query = query.split()
    for wrd in query:
        if wrd.lower() in in_str:
            return True
    return False


def search_guides(query):
    rss = 'http://www.nationalarchives.gov.uk/category/records-2/feed/'
    feed = feedparser.parse(rss)

    for key in feed["entries"]:
        url = key['link'].replace('livelb', 'www')
        title = key['title']
        content = key['content'][0]['value']

        if contains_wanted(query, content.lower()):
            print('{} - {}'.format(title, url))

            # msgtitle = title
            # msg = '{}\n{}'.format(title, url)

            # send_pb_msg(msgtitle, msg)


search_guides(key_words)