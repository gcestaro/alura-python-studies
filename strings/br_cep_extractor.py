import re  # Regular Expression or RegEx

if __name__ == '__main__':
    address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

    pattern = re.compile("[0-9]{5}-?[0-9]{3}")
    search = pattern.search(address)

    if search:
        print(search.group())
