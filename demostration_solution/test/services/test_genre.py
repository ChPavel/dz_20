from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.genre import GenreDAO
from demostration_solution.service.genre import GenreService

@pytest.fixture()
def genre_dao():
    """
    Фикстура с данными для тестов и эмуляторами методов класса GenreDAO.
    :return: подготовленный экземпляр класса GenreDAO.
    """
    genre_dao = GenreDAO(None)

    comedy = Genre(id=1, name='comedy')
    tregedy = Genre(id=2, name='tregedy')
    fuuuuu = Genre(id=3, name='fuuuuu')


    genre_dao.get_one = MagicMock(return_value=fuuuuu)
    genre_dao.get_all = MagicMock(return_value=[comedy, tregedy, fuuuuu])
    genre_dao.create = MagicMock(return_value=Genre(id=3, name='fuuuuu'))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


class TestGenreService:
    """
    Класс для тестирования методов класса GenreService.
    Класс имеет автозапускаемую фикстуру для подмены связи тестируемого класса с DAO на фикстуру genre_dao,
    а также тесты для всех методов класса GenreService.
    """
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None
        assert genre.name is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_create(self):
        genre_d = {
            "name": "sochino"
        }

        genre = self.genre_service.create(genre_d)

        assert genre.id == 3
        assert genre.name is not None

    def test_delete(self):
        self.genre_service.delete(3)


    def test_update(self):
        genre_d = {
            "id": 3,
            "name": "sochino"
        }

        self.genre_service.update(genre_d)