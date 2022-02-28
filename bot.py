import time
from collections import deque
from itertools import chain

from config import *
from messages import TelegramBot
from medium_api import Medium


def run(
        rapidapi_key=RAPIDAPI_KEY, 
        telegram_chat_id=TELEGRAM_CHAT_ID,
        telegram_bot_token=TELEGRAM_BOT_TOKEN,
        tags = TAGS,
        target_words = WORDLIST
    ):
    medium = Medium(rapidapi_key=rapidapi_key)
    existing_articles = deque(maxlen=1000)

    while True:
        top_articles = [medium.topfeeds(tag, 'NEW').ids for tag in tags]
        top_articles = set(chain(*top_articles))

        new_articles = top_articles - set(existing_articles)

        existing_articles.extend(new_articles)
        
        if len(new_articles) >  0:
            for new_article_id in new_articles:
                msg = f'New Article found - https://medium.com/p/{new_article_id}'
                new_article = medium.article(new_article_id, save_info=False)
                print(f'[BOT]: {msg}')

                if any(ele.lower() in new_article.content.lower() for ele in target_words):
                    t = TelegramBot(
                        auth=telegram_bot_token,
                        chat_id=telegram_chat_id,
                        body=msg
                    )
                    t.send()
                    print(f'[BOT]: Message sent to telegram chat - {telegram_chat_id}')

        time.sleep(FREQUENCY)

if __name__ == '__main__':
    run()