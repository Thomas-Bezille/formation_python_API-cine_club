import json
import logging
from pathlib import Path


logging.basicConfig(level=logging.DEBUG)

CUR_DIR = Path(__file__).resolve().parent
DATA_FILE = CUR_DIR / "data" / "movies.json"

class Movie():
    def __init__(self, title: str):
        self.title = title.title()
    
    def __str__(self):
        return f"{self.title}"
    
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)
    
    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà présent dans la liste.")
            return False
    
    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'a pas été trouvé. Impossible de le supprimer")
            return False
    
    def get_all_movies(self):
        movies = self._get_movies()
        if movies:
            instances_movies = [Movie(movie) for movie in movies]
            return instances_movies
        else:
            logging.warning("Votre liste de film est actuellement vide")
            return []



if __name__ == "__main__":
    pass