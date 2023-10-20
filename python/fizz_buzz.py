def fizz_buzz(number):
    fizz = (number % 3 == 0)
    buzz = (number % 5 == 0)
    if fizz:
        if buzz:
            return 'fizz buzz'
        else:
            return 'fizz'
    else:
        if buzz:
            return 'buzz'
        else:
            return number
