class TvShow:
    def __init__(self, name, year):
        self.__name = name.title()
        self.__year = year
        self.__likes = 0

    def like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()


class Movie(TvShow):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.__duration = duration

    def __str__(self):
        return f"{self.name} - {self.__duration} - {self.likes}"


class Series(TvShow):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.__seasons = seasons

    def __str__(self):
        return f"{self.name} - {self.__seasons} - {self.likes}"


'''
    Python Data Model:
    Commonly used -->
        Initialization: __init__ (constructor)
            Example: obj = MyObject()
        Representation: __str__ (end user), __repr__ (logging)
            Example: print(obj), str(obj), repr(obj)
        Container, Sequence: __contains__, __iter__, __len__, __getitem__
            Example: len(obj), item in obj, for i in obj, obj[2:3]
        Numbers: __add__, __sub__, __mul__, __mod__
            Example: obj + other_obj, obj * obj
'''


class Playlist:

    def __init__(self, name, tv_shows):
        self.__name = name
        self.__tv_shows = tv_shows

    # Duck typing --> Behaves like a sequence/iterable
    def __getitem__(self, item):
        return self.__tv_shows[item]

    def __len__(self):
        return len(self.__tv_shows)

    @property
    def list(self):
        return self.__tv_shows

    @property
    def size(self):
        return len(self.__tv_shows)


if __name__ == '__main__':
    avengers = Movie("avengers - infinity war", 2018, 160)
    avengers.like()

    harry_potter_6 = Movie("harry potter and the half-blood prince", 2009, 150)
    harry_potter_6.like()

    star_wars_ep_4 = Movie("Star Wars - Episode IV – A New Hope", 1977, 180)
    star_wars_ep_4.like()

    breaking_bad = Series("breaking bad", 2008, 5)
    breaking_bad.like()

    prison_break = Series("prison break", 2005, 5)
    prison_break.like()

    tv_shows = [avengers, breaking_bad, prison_break, star_wars_ep_4, harry_potter_6]

    weekend_playlist = Playlist("Weekend", tv_shows)

    for tv_show in weekend_playlist:
        print(tv_show)
