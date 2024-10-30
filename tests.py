import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name, genre', [
        ('Солярис', 'Фантастика'),
        ('Крик', 'Ужасы'),
        ('След', 'Детективы')
    ])
    def test_set_book_genre(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre', [
        ('Солярис', 'Фантастика'),
        ('1984', 'Фантастика'),
    ])
    def test_get_books_with_specific_genre(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book_name in books

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.add_new_book('Крик')
        collector.set_book_genre('Крик', 'Ужасы')

        books_genre = collector.get_books_genre()
        assert len(books_genre) == 2
        assert books_genre['Солярис'] == 'Фантастика'
        assert books_genre['Крик'] == 'Ужасы'

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Маугли')
        collector.set_book_genre('Маугли', 'Мультфильмы')
        collector.add_new_book('Монстры')
        collector.set_book_genre('Монстры', 'Ужасы')

        children_books = collector.get_books_for_children()
        assert len(children_books) == 1
        assert 'Маугли' in children_books

    @pytest.mark.parametrize('book_name', [
        'Два капитана',
        'Солярис'
    ])
    def test_add_book_in_favorites(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book_name', [
        'Два капитана',
        'Солярис'
    ])
    def test_delete_book_from_favorites(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorite_books(self):
        collector = BooksCollector()

        collector.add_new_book('Два капитана')
        collector.add_book_in_favorites('Два капитана')
        collector.add_new_book('Солярис')
        collector.add_book_in_favorites('Солярис')

        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Два капитана' in favorites
        assert 'Солярис' in favorites
