def cezar(wiadomosc, klucz, alphabet = ['a', 'b', 'c', 'd', 'e',
                                        'f', 'g', 'h', 'i', 'j',
                                        'k', 'l', 'm', 'n', 'o',
                                        'p', 'q', 'r', 's', 't',
                                        'u', 'v', 'w', 'x', 'y',
                                        'z']):

    nowaWiadomosc = ""

    for letter in wiadomosc:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + klucz) % len(alphabet)
            nowaWiadomosc += alphabet[new_position]
        else:
            nowaWiadomosc += letter

    print(nowaWiadomosc)