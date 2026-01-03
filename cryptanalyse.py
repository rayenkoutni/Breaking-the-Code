def alphabet():
    """
    Returns the reference alphabet used for mono-alphabetic substitution.
    This fixed alphabet defines the Caesar cipher domain.
    """
    return "abcdefghijklmnopqrstuvwxyz"


def position_of_letter(letter):
    """
    Returns the index of a given letter in the alphabet.
    If the letter is not found, -1 is returned.
    This function allows the algorithm to convert letters into numerical positions.
    """
    return alphabet().find(letter)


def letter_at_position(position):
    """
    Returns the letter corresponding to a given position in the alphabet.
    The modulo operation ensures circular wrapping (Caesar shift behavior).
    """
    return alphabet()[position % 26]


def caesar_decrypt(text, key):
    """
    Generates a plaintext hypothesis by applying a Caesar shift
    with the given key to the input ciphertext.

    This function does NOT assume the key is correct.
    It is used to test one decryption hypothesis among many
    during the cryptanalysis process.
    """
    decrypted = ""

    for char in text.lower():
        # Only alphabetic characters are shifted;
        # all other characters (spaces, punctuation) are preserved.
        if char.isalpha():
            pos = position_of_letter(char)
            decrypted += letter_at_position(pos - key)
        else:
            decrypted += char

    return decrypted


def generate_all_hypotheses(ciphertext):
    """
    Generates all possible decryption hypotheses for a Caesar cipher
    by testing every possible key from 0 to 25.

    Each hypothesis consists of:
    - the tested key
    - the corresponding decrypted text

    This exhaustive approach is required in cryptanalysis when the key
    is unknown and must be inferred from the data.
    """
    return [(key, caesar_decrypt(ciphertext, key)) for key in range(26)]
