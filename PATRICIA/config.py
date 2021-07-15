
import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCDmAFj8LGx51aNhU2gpRX0jaTjKYTSYrvKodBYeviH7g0iB1VBsPCOMAO5lpP8gLny8pA00HVikIvVg_cmOeQUUHu4H8ka-pKAg87xKdRZtFzjd7AcbPLBUTKqy3M02OtvYBtiNQNA5jEtEA-K5rd_nC4iCW6ZDJIbThvNOg-cXkAg6_V8pUZh5V1ZZkVhZesz5HVAhyUpQ5VQQtnrHXfWK34DNEXivLrWm36qrHY3EkzghXd4DYvgIuet2J4KEOFMmJ5tLJZddPBD9fshXr6qPr6xYhMw2wQHpIXdB6wr6MMx0T36Gc9S5b2M37a6SWe0Gg8LxsuOWVNYFKBWMuf1X9XNvAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1888191908:AAHcaQcOiXQdXJIyv80d6SVVgVq2IV7f2Zo")
BOT_NAME = getenv("BOT_NAME", "ERAGANGMUSICBOT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "patricia_updates")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/0ab6e6b29d05f0fb70ce8.jpg")
admins = {}
API_ID = int(getenv("API_ID", "3898418"))
API_HASH = getenv("API_HASH", "5a82313211da04d63297bd4de436228c")
BOT_USERNAME = getenv("BOT_USERNAME", "ERAGANGMUSICBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ERA_OWNER")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "PATRICIA_SUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "PATRICIAXMUSIC")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TEAM-PATRICIA/PATRICIA-MUSIC")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1832447570").split()))
