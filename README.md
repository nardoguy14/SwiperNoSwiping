# SwiperNoSwiping

## Requirements
1. chrome driver. It's a driver for automation on chrome that does the leg work of the automation.. with the correct version, 
assuming you have mac, you need to download chrome driver  which can be found here https://chromedriver.chromium.org/downloads. Be sure you download the correct version with the 
version of chrome that you have.  You then need to place it in your local bin by
placing it int he following MAC directory: `/usr/local/bin` For windows ive ready online that it needs to be placed in
`C:\Windows` but I havent tested it on windows so do your own DD.

2. python3 https://www.python.org/downloads/release/python-3613/

## Install

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Running it

`python swiper_no_swiping.py`

I made the script super simple. It opens a browser on tinder.com and I leave the logging in info to you.

I used to make the bot just log in for me but this no longer works since they incorporated a robot check feature.

I'm no tabout to add AI to figure out which two pictures look the same. So the bot will wait about 2 minutes for you to
log in which ever way you want. Be sure to allow location for hte app to work or else you wont get any potential people 
and the bot will just stay stuck there. Once you're there and the bot is running it just swipes right most of the time
but on any multiple of 5, it swipes left to not be caught as the bot. 

Hope it works out for ya king.
