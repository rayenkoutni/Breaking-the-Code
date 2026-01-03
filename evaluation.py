def french_common_words():
    """
    Returns a list of frequent French function words.
    The presence of these words in a candidate plaintext
    is used as a positive indicator of linguistic plausibility.
    """
    return [
        " le ", " la ", " les ", " de ", " des ", " est ",
        " en ", " un ", " une ", " que ", " pour ", " dans "
    ]


def forbidden_patterns():
    """
    Returns a list of character patterns that are unlikely
    to appear in valid French text.
    These patterns are used to penalize improbable decryptions.
    """
    return ["lea ", " lae ", "l  ", "aa", "ee", "ii"]


def evaluate_text(text):
    """
    Evaluates the linguistic plausibility of a decrypted text.

    The scoring combines:
    - positive indicators (frequent French words),
    - negative indicators (unlikely character patterns),
    - penalties for invalid or unusual characters.

    The goal is not perfect linguistic correctness,
    but a relative comparison between decryption hypotheses
    in order to automatically select the most credible plaintext.
    """
    score = 0
    text = text.lower()

    # Reward the presence of common French words
    for word in french_common_words():
        score += text.count(word) * 5

    # Penalize improbable character sequences
    for bad in forbidden_patterns():
        score -= text.count(bad) * 10

    # Penalize characters that do not belong to the expected language set
    for char in text:
        if char not in "abcdefghijklmnopqrstuvwxyz éèàù,. ":
            score -= 1

    return score
