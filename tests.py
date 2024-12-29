import pytest

class TestBooksCollector:

    # 1 Проверка на слишком длинное название книги для add_new_book

    def test_add_new_book_too_long_title_add_negative(self, collector):
        book_name = "a" * 41
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    # 2 Проверка на подходящее название add_new_book

    def test_add_new_book_normal_title(self, collector):
        book_name = "a" * 40
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    # 3 Установка несущевствующего жанра для set_book_genre

    def test_set_book_genre_invalid_genre_negative(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "slop")
        assert collector.get_book_genre("Книга") == ""

    # 4 Проверка полученя жанра для книги с жанром для get_book_genre
    def test_get_book_genre_book_in_list(self, collector):
        book_name = "Книга"
        genre = "Ужасы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # 5 Проверка получения списка жанров, если книги с выбранным жанром нет для get_books_with_specific_genre

    def test_get_books_with_specific_genre_not_in_list(self, collector):
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_with_specific_genre("Детективы") == []

    # 6 Проверка успешного смены жанра книги для get_books_genre

    def test_get_books_genre_after_genre_change(self, collector):
        collector.add_new_book("Холмс")
        collector.set_book_genre("Холмс", "Фантастика")
        collector.set_book_genre("Холмс", "Детективы")
        expected_books_genre = {"Холмс": "Детективы"}
        assert collector.get_books_genre() == expected_books_genre

   # 7 Проверка выдачи только детских книг (без рейтинга) для get_books_for_children

    @pytest.mark.parametrize(
        "books, expected_children_books",
        [
            # Книги разных рейтингов.
            ({"Книга 1": "Мультфильмы", "Книга 2": "Ужасы", "Книга 3": "Комедии"}, ["Книга 1", "Книга 3"]),  # Смешанные книги
        ],
    )
    def test_get_books_for_children_mixed_genre(self, collector, books, expected_children_books):
        for book, genre in books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        actual_children_books = collector.get_books_for_children()
        assert actual_children_books == expected_children_books

    # 8 Повторное добавлние книги в избранное  для add_book_in_favorites

    def test_add_book_in_favorites_add_samebook(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books().count("Книга 1") == 1

    # 9 Удаление книги из избранного

    def test_delete_book_from_favorites_existing_book(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.delete_book_from_favorites("Книга 1")
        assert "Книга 1" not in collector.get_list_of_favorites_books()

    # 10 Получение пустого списка избранное для get_list_of_favorites
    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
