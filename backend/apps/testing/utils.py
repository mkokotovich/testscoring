from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.serializers import TestSerializer


class ItemDescription:
    def __init__(self, number, description='', group='', reverse_scoring=False):
        self.number = number
        self.description = description
        self.group = group
        self.reverse_scoring = reverse_scoring


class BaseAssessment():
    # You will need to provide test_type, items and results_order
    test_type = ''
    items = []
    results_order = []

    # This will only be required if the test needs to account for reverse scores
    def reverse_score(self, score):
        pass

    # You will need to override this method
    def score_test(self, test):
        pass

    # This method will likely be fine left as is
    def create_test(self, test_id):
        self._create_test_items(test_id, self.items)

    def _create_test_items(self, test_id, item_descriptions):
        test = Test.objects.get(id=test_id)
        [
            Item.objects.create(
                test=test,
                number=item.number,
                description=item.description,
                group=item.group,
                reverse_scoring=item.reverse_scoring,
            ) for item in item_descriptions
        ]

    def _convert_to_return_value(self, raw_scores, results_order, test):
        score_list = [
            {'group': result, 'score': raw_scores.pop(result, None)}
            for result in results_order
        ]

        # Just ignore scores that do not belong to groups
        raw_scores.pop('none', None)

        if raw_scores.keys():
            # There should not be anything left in raw scores
            raise APIException(f"Extra data was in raw scores, check scoring logic. Extra data: {raw_scores.keys()}")

        serializer = TestSerializer(test)
        return {"scores": score_list, "test": serializer.data}

    def _calculate_raw_scores(self, test):
        raw_scores = {}
        for item in test.items.all():
            # First validate that score has been set
            if item.score is None:
                raise APIException(f"Unable to calculate score, item {item.number} does not have a score")

            score = item.score
            # Account for reverse scoring, but only if test was created with reverse scoring
            if item.reverse_scoring and test.created_with_reverse_scoring:
                score = self.reverse_score(item.score)

            # Some items need to be counted in multiple groups
            for group in item.groups:
                # If this is the first item in this group, initialize old_score to 0
                old_score = raw_scores.get(group, 0)
                raw_scores[group] = old_score + score

        return raw_scores
