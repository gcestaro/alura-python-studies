class Movie:
    def __init__(self, title, director):
        self.__title = title
        self.__director = director

    @property
    def title(self):
        return self.__title

    @property
    def director(self):
        return self.__director

    def __str__(self):
        return f"{self.__title} - {self.director}"

    '''
        Python's rich comparison:
        __eq__(), called using the operator ==
        __ne__(), called using the operator !=
        __gt__(), called using the operator >
        __lt__(), called using the operator <
        __ge__(), called using the operator >=
        __le__(), called using the operator <=
    '''

    def __eq__(self, other_movie):
        return self.title == other_movie.title


def get_all_movies():
    return [
        Movie("Batman Begins", "Christopher Nolan"),
        Movie("Joker", "Todd Phillips"),
        Movie("Oppenheimer", "Christopher Nolan")
    ]


def has_movie_with_double_equal(movie_to_search):
    all_movies = get_all_movies()

    for movie in all_movies:
        if movie_to_search == movie:  # always False for different objects, unless overridden with __eq__
            return True
    return False


if __name__ == '__main__':
    x = 200
    y = 200
    print(x == y)  # True

    a = 'Gabriel'
    b = "Gabriel"
    print(a == b)  # True

    movies = get_all_movies()
    for movie in movies:
        print(movie)

    movie_to_search = Movie("Batman Begins", "Christopher Nolan")

    print(has_movie_with_double_equal(movie_to_search))
    print(movie_to_search in movies)
