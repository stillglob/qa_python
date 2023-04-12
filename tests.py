import pytest as pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        return collector

    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_the_same_book_twice(self, collector):


        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_for_non_existent_book_shows_none(self, collector):

        collector.set_book_rating('Лабиринт отражений', 7)
        assert collector.books_rating.get('Лабиринт отражений') == None

    def test_set_book_rating_less_than_one_shows_default_rating(self, collector):

        collector.add_new_book('Лабиринт отражений')
        collector.set_book_rating('Лабиринт отражений', 0)
        assert collector.books_rating.get('Лабиринт отражений') == 1

    def test_set_book_rating_more_than_10_shows_default_rating(self, collector):

        collector.add_new_book('Лабиринт отражений')
        collector.set_book_rating('Лабиринт отражений', 11)
        assert collector.books_rating.get('Лабиринт отражений') == 1

    def test_non_existent_book_have_no_rating(self, collector):

        assert collector.books_rating.get('Преступление и наказание') == None

    def test_add_book_in_favorites(self, collector):

        collector.add_new_book('Мертвые души')
        collector.add_book_in_favorites('Мертвые души')
        assert 'Мертвые души' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_if_book_not_in_books_rating(self, collector):

        collector.add_book_in_favorites('Мертвые души')
        assert not 'Мертвые души' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):

        collector.add_new_book('Мертвые души')
        collector.add_book_in_favorites('Мертвые души')
        collector.delete_book_from_favorites('Мертвые души')
        assert not 'Мертвые души' in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_rating(self, collector):

        collector.add_new_book('Мертвые души')
        collector.add_new_book('Лабиринт отражений')
        collector.set_book_rating('Лабиринт отражений', 7)
        collector.set_book_rating('Мертвые души', 7)
        assert collector.get_books_with_specific_rating(7) == ['Мертвые души', 'Лабиринт отражений']

    def test_get_list_of_favorites_books(self, collector):

        collector.add_new_book('Мертвые души')
        collector.add_new_book('Лабиринт отражений')
        collector.add_book_in_favorites('Мертвые души')
        collector.add_book_in_favorites('Лабиринт отражений')
        assert collector.get_list_of_favorites_books() == ['Мертвые души', 'Лабиринт отражений']

    def test_init_books_rating_equals_dict(self, collector):

        assert collector.books_rating == {}

    def test_init_favorites_equals_dict(self, collector):

        assert collector.favorites == []
