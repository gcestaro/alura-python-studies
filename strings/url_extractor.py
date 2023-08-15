from url_validator import URLValidator


class URLExtractor:
    url_parameter_separator = "&"

    def __init__(self, url=""):
        self.__url = self.__sanityze(url)
        URLValidator().validate(self.__url)
        self.__base_url = self.__get_base_url()
        self.__url_parameters = self.__get_url_parameters()

    def get_parameter_value(self, name):
        parameter_start_index = self.__url_parameters.find(name)

        if parameter_start_index == -1:
            raise ValueError(f"Parameter {name} not found")

        parameter_value_start_index = parameter_start_index + len(name) + 1

        next_parameter_separator_index = self.__url_parameters.find(self.url_parameter_separator,
                                                                    parameter_value_start_index)

        if next_parameter_separator_index == -1:
            return self.__url_parameters[parameter_value_start_index:]

        return self.__url_parameters[parameter_value_start_index:next_parameter_separator_index]

    def __sanityze(self, url):
        if type(url) == str:
            return url.strip()
        return ""

    def __get_base_url(self):
        question_mark_index = self.__url.find("?")

        if question_mark_index == -1:
            return self.__url

        return self.__url[:question_mark_index]

    def __get_url_parameters(self):
        question_mark_index = self.__url.find("?")

        if question_mark_index == -1:
            return ""

        return self.__url[question_mark_index + 1:]

    @property
    def url(self):
        return self.__url

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return f"URL: {self.__url}\nBase: {self.__base_url}\nParameters: {self.__url_parameters}"

    def __eq__(self, other):
        return self.__url == other.url


if __name__ == '__main__':
    url = "https://bytebank.com/exchange?sourceCoin=BRL&targetCoin=EUR&quantity=100"

    url_extractor = URLExtractor(url)
    url_extractor2 = URLExtractor(url)
    print(url_extractor)
    print(id(url_extractor))
    print(id(url_extractor2))

    # Verify identity equality --> id(obj)
    print(url_extractor2 is url_extractor)  # False

    # Verify __eq__ implementation, by default compare memory reference with id()
    print(url_extractor2 == url_extractor)  # True, implementation of __eq__ above, url == url

    sourceCoin = url_extractor.get_parameter_value("sourceCoin")
    targetCoin = url_extractor.get_parameter_value("targetCoin")
    quantity = url_extractor.get_parameter_value("quantity")

    print(sourceCoin, targetCoin, quantity)

'''
    Python String docs: https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods
'''
