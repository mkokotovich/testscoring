from rest_framework.exceptions import APIException


class ItemDescription:
    def __init__(self, number, description='', group=''):
        self.number = number
        self.description = description
        self.group = group


def calculate_raw_scores(test):
    raw_scores = {}
    for item in test.items.all():
        # First validate that score has been set
        if item.score == None:
            raise APIException(f"Unable to calculate score, item {item.number} does not have a score")

        # If this is the first item in this group, initialize old_score to 0
        old_score = raw_scores.get(item.group, 0)
        raw_scores[item.group] = old_score + item.score
    return raw_scores
