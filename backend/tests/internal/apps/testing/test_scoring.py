import pytest
from django.contrib.auth.models import User

from apps.testing import models
from apps.testing import (cbcl, conners)
from tests.internal.data.cbcl_6_18_test import test as cbcl_6_18_test
from tests.internal.data.cbcl_6_18_scores import scores as cbcl_6_18_scores
from tests.internal.data.cbcl_1_5_test import test as cbcl_1_5_test
from tests.internal.data.cbcl_1_5_scores import scores as cbcl_1_5_scores
from tests.internal.data.conners3_parent_test import test as conners3_parent_test
from tests.internal.data.conners3_parent_scores import scores as conners3_parent_scores


cbcl_6_18_data = (
    cbcl_6_18_test,
    cbcl_6_18_scores,
    cbcl.create_cbcl_6_18_test_items,
    cbcl.calculate_cbcl_6_18_test_scores,
)


# TODO: these scores are unverified, replace with verified scores
cbcl_1_5_data = (
    cbcl_1_5_test,
    cbcl_1_5_scores,
    cbcl.create_cbcl_1_5_test_items,
    cbcl.calculate_cbcl_1_5_test_scores,
)


conners3_parent_data = (
    conners3_parent_test,
    conners3_parent_scores,
    conners.create_conners3_parent_test_items,
    conners.calculate_conners3_parent_test_scores,
)


@pytest.mark.django_db
@pytest.mark.parametrize(
    'test, scores, create_function, score_function',
    [
        cbcl_6_18_data,
        cbcl_1_5_data,
        conners3_parent_data,
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
