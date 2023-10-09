import string
import random


def generate_password(length, lowercase=True, uppercase=True, digits=True, punctuation=True):
    """Returns a random password.

    Args:
        length: The length of the password
        lowercase: Boolean indicating whether or not to include lowercase letters
        uppercase: Boolean indicating whether or not to include uppercase letters
        digits: Boolean indicating whether or not to include digits
        punctuation: Boolean indicating whether or not to include punctuations

    Returns:
        A random password with the specified length
    """
    characters = ''
    characters += string.ascii_lowercase if lowercase   else ''
    characters += string.ascii_uppercase if uppercase   else ''
    characters += string.digits          if digits      else ''
    characters += string.punctuation     if punctuation else ''
    characters = list(characters)

    return ''.join(random.choice(characters) for _ in range(length))
