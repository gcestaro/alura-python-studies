class URLExtractor:
    url_parameter_separator = "&"

    def __init__(self, url=""):
        self.__url = self.__sanityze(url)
        self.validate_url()
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

    def validate_url(self):
        if not self.__url:
            raise ValueError("Empty URL")

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


if __name__ == '__main__':
    url = "https://bytebank.com/exchange?sourceCoin=BRL&targetCoin=USD&quantity=100"

    url_extractor = URLExtractor(url)
    sourceCoin = url_extractor.get_parameter_value("sourceCoin")
    targetCoin = url_extractor.get_parameter_value("targetCoin")
    quantity = url_extractor.get_parameter_value("quantity")

    print(sourceCoin, targetCoin, quantity)
