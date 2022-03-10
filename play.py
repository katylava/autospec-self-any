from dog import Dog


def get_dog():
    return Dog('Daisy')


def play(dog):
    dog.add_trick('sit')
    print(dog.tricks)
