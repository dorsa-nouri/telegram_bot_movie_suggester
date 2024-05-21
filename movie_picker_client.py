import requests

class MoviePicker:
    def __init__(self, headers, url) -> None:
        self.headers = headers
        self.url = url

    def get_movie_list(self) -> dict:
        return requests.get(self.url, headers=self.headers).text

    def download_image(self, url: str, path: str):
        image_res = requests.get(url)
        with open(path, "wb") as file:
            file.write(image_res.content)
