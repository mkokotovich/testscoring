import pytest
from django.contrib.auth.models import User

from apps.testing import models
from apps.testing import cbcl
from tests.internal.data.cbcl_6_18_test import test as cbcl_6_18_test
from tests.internal.data.cbcl_6_18_scores import scores as cbcl_6_18_scores


@pytest.mark.django_db
@pytest.mark.parametrize(
    'test, scores, create_function, score_function',
    [
        (
            cbcl_6_18_test,
            cbcl_6_18_scores,
            cbcl.create_cbcl_6_18_test_items,
            cbcl.calculate_cbcl_6_18_test_scores,
        ),
    ]
)
def test_test_creation_and_scoring(test, scores, create_function, score_function):
    owner = User.objects.create(username="test")
    test_obj = models.Test.objects.create(
        owner=owner,
        client_number=test['client_number'],
        test_type=test['test_type'],
    )
    create_function(test_obj.id)
    for index, item in enumerate(test_obj.items.all()):
        item.score = test['items'][index]['score']
        item.save()
    score_ret = score_function(test_obj)
    assert score_ret['scores'] == scores['scores']
