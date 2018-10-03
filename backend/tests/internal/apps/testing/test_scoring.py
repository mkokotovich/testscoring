import pytest
from django.contrib.auth.models import User

from apps.testing import models
from apps.testing import (cbcl, conners, tscyc, scared, srs, brief)
from tests.internal.data.cbcl_6_18_test import test as cbcl_6_18_test
from tests.internal.data.cbcl_6_18_scores import scores as cbcl_6_18_scores
from tests.internal.data.cbcl_1_5_test import test as cbcl_1_5_test
from tests.internal.data.cbcl_1_5_scores import scores as cbcl_1_5_scores
from tests.internal.data.conners3_parent_test import test as conners3_parent_test
from tests.internal.data.conners3_parent_scores import scores as conners3_parent_scores
from tests.internal.data.conners3_self_test import test as conners3_self_test
from tests.internal.data.conners3_self_scores import scores as conners3_self_scores
from tests.internal.data.tscyc_test import test as tscyc_test
from tests.internal.data.tscyc_scores import scores as tscyc_scores
from tests.internal.data.scared_test import test as scared_test
from tests.internal.data.scared_scores import scores as scared_scores
from tests.internal.data.srs2_test import test as srs2_test
from tests.internal.data.srs2_scores import scores as srs2_scores
from tests.internal.data.brief2_test import test as brief2_test
from tests.internal.data.brief2_scores import scores as brief2_scores


cbcl_6_18_data = (
    cbcl_6_18_test,
    cbcl_6_18_scores,
    cbcl.CBCL_6_18(),
)


cbcl_1_5_data = (
    cbcl_1_5_test,
    cbcl_1_5_scores,
    cbcl.CBCL_1_5()
)


conners3_parent_data = (
    conners3_parent_test,
    conners3_parent_scores,
    conners.Conners3Parent(),
)


conners3_self_data = (
    conners3_self_test,
    conners3_self_scores,
    conners.Conners3Self(),
)


tscyc_data = (
    tscyc_test,
    tscyc_scores,
    tscyc.TSCYC(),
)


scared_data = (
    scared_test,
    scared_scores,
    scared.SCARED(),
)


srs2_data = (
    srs2_test,
    srs2_scores,
    srs.SRS2(),
)


brief2_data = (
    brief2_test,
    brief2_scores,
    brief.Brief2(),
)


@pytest.mark.django_db
@pytest.mark.parametrize(
    'test, scores, assessment',
    [
        cbcl_6_18_data,
        cbcl_1_5_data,
        conners3_parent_data,
        conners3_self_data,
        tscyc_data,
        scared_data,
        srs2_data,
        brief2_data,
    ]
)
def test_test_creation_and_scoring(test, scores, assessment):
    owner = User.objects.create(username="test")
    test_obj = models.Test.objects.create(
        owner=owner,
        client_number=test['client_number'],
        test_type=test['test_type'],
    )
    assessment.create_test(test_obj.id)
    for index, item in enumerate(test_obj.items.all()):
        item.score = test['items'][index]['score']
        item.save()
    score_ret = assessment.score_test(test_obj)
    assert score_ret['scores'] == scores['scores']
