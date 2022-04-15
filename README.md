# Crypto Medium Bot

Script to monitor Medium Articles for given `tags` (like _ethereum, blockchain, tokenomics, etc..._) containing `target_keywords` such as _'introducing', 'launching', 'discover', etc..._ and getting their notifications on Telegram bot.

By doing so, you can find crypto opportunities to invest or trade ahead of the market. 

So what are you waiting for, leverage this **information arbitrage** to make a fortune in cryptospace!

For more details, read [How to Leverage Medium for CryptoTrading](https://medium.com/p/deedea890da1)

## Usage

1. Clone this repository

```bash
 $ git clone "https://github.com/weeping-angel/crypto-medium-bot.git"
 $ cd crypto-medium-bot
```

2. Install the requirements

```bash
$ pip install -r requirements.txt
```

3. Open `config.py` and replace the following variables:

    - RAPIDAPI_KEY
    - TELEGRAM_BOT_TOKEN
    - TELEGRAM_CHAT_ID

4. (Optional) Change `TAGS` and `WORDLIST` to customize your monitoring algorithm.

5. Run the bot using following command:

```bash
$ python bot.py
```

## How to get your RapidAPI Key

<p align="center">
    <a href="https://www.youtube.com/watch?v=-MM1C6mb-mc">
        <img src="https://img.youtube.com/vi/-MM1C6mb-mc/0.jpg" alt="How to get your RapidAPI Key">Watch Video</img>
    </a>
</p>

Steps:

1. Sign up on [RapidAPI Platform](https://rapidapi.com/auth/sign-up)

2. Subscribe to [Medium API](http://hub.mediumapi.com/pricing)

3. Go to the API's **Endpoints** tab on the [RapidAPI Hub listing](http://hub.mediumapi.com) and select the API key from the **X-RapidAPI-Key** dropdown under **Header Parameters** section.

For more details, see the following links:

 - https://rapidapi.com/blog/api-glossary/api-key/
        
 - https://docs.rapidapi.com/docs/keys



## References

[How to create a Telegram Bot and get its Token?](https://core.telegram.org/bots#6-botfather)

[How to get your Telegram Bot Chat ID](https://github.com/HomeMadePy/messages/wiki/TelegramBot#telegram-api)

```python
>>> from messages import TelegramBot
>>> t = TelegramBot(auth='ABCD:1234')    
>>> t.get_chat_id('@yourUserName')
1234567
```

[Medium REST API](http://hub.mediumapi.com)

[Medium API - Python Package](https://github.com/weeping-angel/medium-api)

```bash
$ pip install medium-api
```