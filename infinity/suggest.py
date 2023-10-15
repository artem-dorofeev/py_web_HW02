
import spacy
import Levenshtein

nlp = spacy.load("en_core_web_md")

COMMANDS = [
    'add record',
    "change phone", "add phone",
    'exit',
    'help', "delete phone",
    "del phone", "add birthday",
    'show all',
    'search', 'hello',
    "add email",
    "delete email",
    "change email",
    "delete record", "remove",
    "days to birthday", "sort"
]


def suggest_command(user_input):
    user_input = user_input.lower()
    min_distance = float("inf")
    closest_keyword = None

    for keyword in COMMANDS:
        keyword_lower = keyword.lower()
        distance = Levenshtein.distance(user_input, keyword_lower)

        if distance < min_distance:
            min_distance = distance
            closest_keyword = keyword

    return closest_keyword



