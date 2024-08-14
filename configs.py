# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID", "23323912")
    API_HASH = os.environ.get("API_HASH", "5b7decd292e78a57d631ea1849b7098a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7212133770:AAE-mJVuPD6Cz59wcLthQWfIDIFMmFgRZEM")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Dear_Batman_bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "moviesandwebserieshubOrzz")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002207296876")
    DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
    TIME_GAP = int(os.environ.get("TIME_GAP", 5))
    MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 10))
    STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME")
    STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS")
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://dasaripardhasaradhi141:X5SstfxEbJORxOTh@cluster0.fvgzzwq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 2036125193))

    START_TEXT = """
Hi 👋, I am a Video Merge Bot!
I can Merge Multiple Videos in One Video. Video Formats should be same.
"""
    CAPTION = "Video Merged by @{}\n\nMade by @moviesandwebserieshubOrzz"
    PROGRESS = """
Percentage : {0}%
Done: {1}
Total: {2}
Speed: {3}/s
ETA: {4}
"""
