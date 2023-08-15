import re


class URLValidator:
    url_pattern = "(http(s)?://)?(www.)?bytebank[.]com(.br)?[/]exchange[?]"

    def __init__(self):
        self.pattern = re.compile(URLValidator.url_pattern)

    def validate(self, url):
        if not url:
            raise ValueError("Empty URL")

        match = self.pattern.match(url)
        if not match:
            raise ValueError("Invalid URL")


if __name__ == '__main__':
    url_list = [
        "http://bytebank.com/exchange?quantity=100&sourceCoin=BRL&targetCoin=EUR",
        "https://bytebank.com/exchange?quantity=100&sourceCoin=BRL&targetCoin=EUR",
        "http://www.bytebank.com/exchange?",
        "https://www.bytebank.com/exchange?",
        "https://www.bank.com/exchange?",
    ]
    for url in url_list:
        url_validator = URLValidator().validate(url)
