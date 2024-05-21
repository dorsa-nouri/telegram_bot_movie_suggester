from movie_picker_poster import poster
import time
import os
from dotenv import load_dotenv
from asyncio import run

load_dotenv(".env")


async def main(bot_token: str, chat_id: int, headers: dict, sleep_time: int):
    while True:
        try:
            await poster(
                bot_token=bot_token,
                chat_id=chat_id,
                headers=headers,
            )
        except:
            pass
        finally:
            time.sleep(sleep_time)


if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHANNEL_CHAT_ID = os.getenv("CHANNEL_CHAT_ID")
    HEADERS = os.getenv("HEADERS")
    # SLEEP_TIME = 10 * 60  # seconds
    SLEEP_TIME = 10  # seconds
    run(
        main(
            bot_token=BOT_TOKEN,
            chat_id=CHANNEL_CHAT_ID,
            headers=HEADERS,
            sleep_time=SLEEP_TIME,
        )
    )
