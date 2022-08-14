from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.model.director import Director
from demostration_solution.dao.director import DirectorDAO
from demostration_solution.service.director import DirectorService

@pytest.fixture()
def director_dao():
    """
    Фикстура с данными для тестов и эмуляторами методов класса DirectorDAO.
    :return: подготовленный экземпляр класса DirectorDAO.
    """
    director_dao = DirectorDAO(None)

    pochino = Director(id=1, name='pochino')
    mochino = Director(id=2, name='mochino')
    tochino = Director(id=3, name='tochino')


    director_dao.get_one = MagicMock(return_value=pochino)
    director_dao.get_all = MagicMock(return_value=[pochino, mochino, tochino])
    director_dao.create = MagicMock(return_value=Director(id=3, name='sochino'))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    """
    Класс для тестирования методов класса DirectorService.
    Класс имеет автозапускаемую фикстуру для подмены связи тестируемого класса с DAO на фикстуру director_dao,
    а также тесты для всех методов класса DirectorService.
    """
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None
        assert director.name is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "sochino"
        }

        director = self.director_service.create(director_d)

        assert director.id == 3
        assert director.name is not None

    def test_delete(self):
        self.director_service.delete(3)


    def test_update(self):
        director_d = {
            "id": 3,
            "name": "sochino"
        }

        self.director_service.update(director_d)