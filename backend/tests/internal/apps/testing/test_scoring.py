import pytest

from apps.testing import models
from apps.testing import (cbcl, conners, tscyc, scared, srs, brief, asrs, masc2, cdi2, tscc)
from evaluators.models import User
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
from tests.internal.data.briefp_test import test as briefp_test
from tests.internal.data.briefp_scores import scores as briefp_scores
from tests.internal.data.asrs_6_18_test import test as asrs_6_18_test
from tests.internal.data.asrs_6_18_scores import scores as asrs_6_18_scores
from tests.internal.data.asrs_2_5_test import test as asrs_2_5_test
from tests.internal.data.asrs_2_5_scores import scores as asrs_2_5_scores
from tests.internal.data.masc2_self_test import test as masc2_self_test
from tests.internal.data.masc2_self_scores import scores as masc2_self_scores
from tests.internal.data.masc2_parent_test import test as masc2_parent_test
from tests.internal.data.masc2_parent_scores import scores as masc2_parent_scores
from tests.internal.data.cdi2_self_test import test as cdi2_self_test
from tests.internal.data.cdi2_self_scores import scores as cdi2_self_scores
from tests.internal.data.tscc_test import test as tscc_test
from tests.internal.data.tscc_scores import scores as tscc_scores


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


briefp_data = (
    briefp_test,
    briefp_scores,
    brief.BriefP(),
)


asrs_6_18_data = (
    asrs_6_18_test,
    asrs_6_18_scores,
    asrs.ASRS_6_18(),
)


asrs_2_5_data = (
    asrs_2_5_test,
    asrs_2_5_scores,
    asrs.ASRS_2_5(),
)


masc2_parent_data = (
    masc2_parent_test,
    masc2_parent_scores,
    masc2.MASC2Parent(),
)


masc2_self_data = (
    masc2_self_test,
    masc2_self_scores,
    masc2.MASC2Self(),
)


cdi2_self_data = (
    cdi2_self_test,
    cdi2_self_scores,
    cdi2.CDI2Self(),
)


tscc_data = (
    tscc_test,
    tscc_scores,
    tscc.TSCC(),
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
        briefp_data,
        asrs_6_18_data,
        asrs_2_5_data,
        masc2_self_data,
        masc2_parent_data,
        cdi2_self_data,
        tscc_data,
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
