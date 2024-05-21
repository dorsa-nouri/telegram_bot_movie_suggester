from telegram import Bot
import movie_picker_client
import json
import random


async def poster(bot_token: str, chat_id: int, headers: dict) -> bool:
    bot = Bot(token=bot_token)
    movie_client = movie_picker_client.MoviePicker(
        headers=headers,
        url="https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc",
    )
    movie_data = movie_client.get_movie_list()
    movie_data = json.loads(movie_data)
    all_movie_list = movie_data["results"]
    get_random_movie = random.choice(all_movie_list)
    title = get_random_movie["original_title"]
    release_date = get_random_movie["release_date"]
    overview = get_random_movie["overview"]
    caption = f"<b>{title}</b></a>\n{release_date}\n\n{overview}\n\n<a href='https://t.me/movieSuggesterFromMe'>@Movie Suggester</a>"
    await bot.send_message(chat_id=chat_id, text=caption, parse_mode="HTML")
