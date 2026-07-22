# Internet Speed Complaint Bot

Day 51 of 100 Days of Code. This one checks my actual internet speed against what my provider promised, and if they're not delivering, it automatically posts a complaint for me.

## What it does

1. Opens a speed test site in Chrome and runs the test.
2. Grabs the download/upload numbers once the test finishes.
3. Compares them to the speeds I'm supposedly paying for.
4. If either one falls short, it logs into a Twitter-like site, opens the compose modal, and posts a complaint with the actual vs. promised numbers.
5. If the speeds are fine, it just prints a message to the console and does nothing else.

## Setup

Install dependencies:

```
pip install selenium python-dotenv
```

You'll also need [ChromeDriver](https://chromedriver.chromium.org/) matching your installed Chrome version, or `webdriver-manager` if you'd rather not manage that by hand.

Create a `.env` file in this folder with:

```
INTERNET_SPEED_URL=
Y_LOGIN_URL=
EMAIL=
PASSWORD=
PROMISED_DOWN=
PROMISED_UP=
```

- `INTERNET_SPEED_URL` — the speed test site to use
- `Y_LOGIN_URL` — login page for the social site the complaint gets posted to
- `EMAIL` / `PASSWORD` — login credentials for that account
- `PROMISED_DOWN` / `PROMISED_UP` — the download/upload speeds (Mbps) your provider promised you

## Running it

```
python main.py
```

Two Chrome windows will open — one runs the speed test, the other (only if needed) handles the login and posts the complaint.

## Notes to self

- The speed test page occasionally throws its own "upload test error" if a firewall/VPN is interfering with the WebSocket connection it uses — that's the site's issue, not the script's.
- The compose modal and the inline compose box on the login site share the same CSS classes, so the code targets the modal by its `id` specifically to avoid clicking the wrong one.
