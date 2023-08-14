if __name__ == '__main__':
    url = "https://bytebank.com/exchange?sourceCoin=BRL&targetCoin=USD&amount=100"

    base_url = url[0:29]
    print(base_url)  # https://bytebank.com/exchange

    parameters_url = url[30:70]
    print(parameters_url)  # sourceCoin=BRL&targetCoin=USD&amount=100

    question_mark_index = url.find("?")  # https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=find#str.find
    print(question_mark_index)  # 29

    print(url[0:question_mark_index])  # https://bytebank.com/exchange
    print(url[:question_mark_index])  # https://bytebank.com/exchange

    print(url[question_mark_index + 1:])  # sourceCoin=BRL&targetCoin=USD&amount=100
    print(url[question_mark_index + 1:len(url)])  # sourceCoin=BRL&targetCoin=USD&amount=100

    source_coin_parameter_name = "sourceCoin"
    source_coin_parameter_value_index = parameters_url.find(source_coin_parameter_name) + len(
        source_coin_parameter_name) + 1

    parameter_separator = "&"
    next_parameter_separator_index = parameters_url.find(parameter_separator, source_coin_parameter_value_index)

    if next_parameter_separator_index == -1:
        source_coin_parameter_value = parameters_url[source_coin_parameter_value_index:]
    else:
        source_coin_parameter_value = \
            parameters_url[source_coin_parameter_value_index:next_parameter_separator_index]

    print(source_coin_parameter_value)
