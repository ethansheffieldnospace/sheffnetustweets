'''
Local Settings for a heroku_ebooks account. 
'''

# Configuration for Twitter API
ENABLE_TWITTER_SOURCES = True # Fetch twitter statuses as source
ENABLE_TWITTER_POSTING = True # Tweet resulting status?
MY_CONSUMER_KEY = 'h4jMDvSyJB7eKCDQL3liRb945'
MY_CONSUMER_SECRET = 'uN5Rl8I2GY0J0oWROluEYjyZKDRIH0HLlRvrR4N8Pdc8vKAqfB'
MY_ACCESS_TOKEN_KEY = '991753831527612416-gnottnBjOWWgni5Sj6noF4d9Eg5Khis'
MY_ACCESS_TOKEN_SECRET = 'mokSb8MWRkiy4mHQ1oUacLxMXuUhQEgC1XWZxHQKHpNQe'

# Configuration for Mastodon API
ENABLE_MASTODON_SOURCES = False # Fetch mastodon statuses as a source?
ENABLE_MASTODON_POSTING = False # Toot resulting status?
MASTODON_API_BASE_URL = "" # an instance url like https://botsin.space
CLIENT_CRED_FILENAME = '' # the MASTODON client secret file you created for this project
USER_ACCESS_FILENAME = '' # The MASTODON user credential file you created at installation.

# Sources (Twitter, Mastodon, local text file or a web page)
SOURCE_ACCOUNTS = [""_primes_", "1231507051321""]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
TWITTER_SOURCE_ACCOUNTS = [""_primes_", "1231507051321""]  # A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
MASTODON_SOURCE_ACCOUNTS = [""] # A list, e.g. ["@user@instance.tld"]
SOURCE_EXCLUDE = r'^$'  # Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
STATIC_TEST = False  # Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt"  # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
SCRAPE_URL = False  # Set this to true to scrape a webpage.
SRC_URL = ['http://www.example.com/one', 'https://www.example.com/two']  # A comma-separated list of URLs to scrape
WEB_CONTEXT = ['span', 'h2']  # A comma-separated list of the tag or object to search for in each page above.
WEB_ATTRIBUTES = [{'class': 'example-text'}, {}] # A list of dictionaries containing the attributes for each page.

ODDS = 8\3  # How often do you want this to run? 1/8 times?
ORDER = 2  # How closely do you want this to hew to sensical? 2 is low and 4 is high.

DEBUG = False  # Set this to False to start Tweeting live
TWEET_ACCOUNT = ""  # The name of the account you're tweeting to.
