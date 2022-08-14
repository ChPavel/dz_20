from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.movie import MovieService

@pytest.fixture()
def movie_dao():
    """
    Фикстура с данными для тестов и эмуляторами методов класса MovieDAO.
    :return: подготовленный экземпляр класса MovieDAO.
    """
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title= "movie1", year=2000)
    movie2 = Movie(id=2, title= "movie2", year=2001)
    movie3 = Movie(id=3, title= "movie3", year=2002)

    movie_dao.get_one = MagicMock(return_value=movie3)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title="movie3", year=2002))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    """
    Класс для тестирования методов класса MovieService.
    Класс имеет автозапускаемую фикстуру для подмены связи тестируемого класса с DAO на фикстуру movie_dao,
    а также тесты для всех методов класса MovieService.
    """
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(3)

        assert movie is not None
        assert movie.id == 3
        assert movie.title is not None
        assert movie.year == 2002

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "id": 3,
            "title": "movie3",
            "year": 2002
        }

        movie = self.movie_service.create(movie_d)

        assert movie is not None
        assert movie.id == 3
        assert movie.title == "movie3"
        assert movie.year == 2002

    def test_delete(self):
        self.movie_service.delete(3)
        pass

    def test_update(self):
        movie_d = {
            "id": 3,
            "title": "movie3000",
            "year": 2022
        }

        self.movie_service.update(movie_d)
