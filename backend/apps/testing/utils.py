from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.serializers import TestSerializer


class ItemDescription:
    def __init__(self, number, description='', group=''):
        self.number = number
        self.description = description
        self.group = group


def create_test_items(test_id, item_descriptions):
    test = Test.objects.get(id=test_id)
    items = [
        Item.objects.create(
            test=test,
            number=item.number,
            description=item.description,
            group=item.group
        ) for item in item_descriptions
    ]


def convert_to_return_value(raw_scores, results_order, test):
    score_list = [
        {'group': result, 'score': raw_scores.pop(result)}
        for result in results_order
    ]

    # Just ignore scores that do not belong to groups
    raw_scores.pop('none', None)

    if raw_scores.keys():
        # There should not be anything left in raw scores
        raise APIException(f"Extra data was in raw scores, check scoring logic. Extra data: {raw_scores.keys()}")

    serializer = TestSerializer(test)
    return {"scores": score_list, "test": serializer.data}


def calculate_raw_scores(test):
    raw_scores = {}
    for item in test.items.all():
        # First validate that score has been set
        if item.score == None:
            raise APIException(f"Unable to calculate score, item {item.number} does not have a score")

        # Some items need to be counted in multiple groups
        for group in item.groups:
            # If this is the first item in this group, initialize old_score to 0
            old_score = raw_scores.get(group, 0)
            raw_scores[group] = old_score + item.score

    return raw_scores
