from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.serializers import TestSerializer
from apps.testing.utils import ItemDescription, calculate_raw_scores


cbcl_6_18_items = [
    ItemDescription('1', description='', group='VI'),
    ItemDescription('2', description='', group='VII'),
    ItemDescription('3', description='', group='VIII'),
    ItemDescription('4', description='', group='VI'),
    ItemDescription('5', description='', group='II'),
    ItemDescription('6', description='', group='other'),
    ItemDescription('7', description='', group='other'),
    ItemDescription('8', description='', group='VI'),
    ItemDescription('9', description='', group='V'),
    ItemDescription('10', description='', group='VI'),
    ItemDescription('11', description='', group='IV'),
    ItemDescription('12', description='', group='IV'),
    ItemDescription('13', description='', group='VI'),
    ItemDescription('14', description='', group='I'),
    ItemDescription('15', description='', group='other'),
    ItemDescription('16', description='', group='VIII'),
    ItemDescription('17', description='', group='VI'),
    ItemDescription('18', description='', group='V'),
    ItemDescription('19', description='', group='VIII'),
    ItemDescription('20', description='', group='VIII'),
    ItemDescription('21', description='', group='VIII'),
    ItemDescription('22', description='', group='VIII'),
    ItemDescription('23', description='', group='VIII'),
    ItemDescription('24', description='', group='other'),
    ItemDescription('25', description='', group='IV'),
    ItemDescription('26', description='', group='VII'),
    ItemDescription('27', description='', group='IV'),
    ItemDescription('28', description='', group='VII'),
    ItemDescription('29', description='', group='I'),
    ItemDescription('30', description='', group='I'),
    ItemDescription('31', description='', group='I'),
    ItemDescription('32', description='', group='I'),
    ItemDescription('33', description='', group='I'),
    ItemDescription('34', description='', group='IV'),
    ItemDescription('35', description='', group='I'),
    ItemDescription('36', description='', group='IV'),
    ItemDescription('37', description='', group='VIII'),
    ItemDescription('38', description='', group='IV'),
    ItemDescription('39', description='', group='VII'),
    ItemDescription('40', description='', group='V'),
    ItemDescription('41', description='', group='VI'),
    ItemDescription('42', description='', group='II'),
    ItemDescription('43', description='', group='VII'),
    ItemDescription('44', description='', group='other'),
    ItemDescription('45', description='', group='I'),
    ItemDescription('46', description='', group='V'),
    ItemDescription('47', description='', group='III'),
    ItemDescription('48', description='', group='IV'),
    ItemDescription('49', description='', group='III'),
    ItemDescription('50', description='', group='I'),
    ItemDescription('51', description='', group='III'),
    ItemDescription('52', description='', group='I'),
    ItemDescription('53', description='', group='other'),
    ItemDescription('54', description='', group='III'),
    ItemDescription('55', description='', group='other'),
    ItemDescription('56a', description='', group='III'),
    ItemDescription('56b', description='', group='III'),
    ItemDescription('56c', description='', group='III'),
    ItemDescription('56d', description='', group='III'),
    ItemDescription('56e', description='', group='III'),
    ItemDescription('56f', description='', group='III'),
    ItemDescription('56g', description='', group='III'),
    ItemDescription('56h', description='', group='other'),
    ItemDescription('57', description='', group='VIII'),
    ItemDescription('58', description='', group='V'),
    ItemDescription('59', description='', group='V'),
    ItemDescription('60', description='', group='V'),
    ItemDescription('61', description='', group='VI'),
    ItemDescription('62', description='', group='IV'),
    ItemDescription('63', description='', group='VII'),
    ItemDescription('64', description='', group='IV'),
    ItemDescription('65', description='', group='II'),
    ItemDescription('66', description='', group='V'),
    ItemDescription('67', description='', group='VII'),
    ItemDescription('68', description='', group='VIII'),
    ItemDescription('69', description='', group='II'),
    ItemDescription('70', description='', group='V'),
    ItemDescription('71', description='', group='I'),
    ItemDescription('72', description='', group='VII'),
    ItemDescription('73', description='', group='VII'),
    ItemDescription('74', description='', group='other'),
    ItemDescription('75', description='', group='II'),
    ItemDescription('76', description='', group='V'),
    ItemDescription('77', description='', group='other'),
    ItemDescription('78', description='', group='VI'),
    ItemDescription('79', description='', group='IV'),
    ItemDescription('80', description='', group='VI'),
    ItemDescription('81', description='', group='VII'),
    ItemDescription('82', description='', group='VII'),
    ItemDescription('83', description='', group='V'),
    ItemDescription('84', description='', group='V'),
    ItemDescription('85', description='', group='V'),
    ItemDescription('86', description='', group='VIII'),
    ItemDescription('87', description='', group='VIII'),
    ItemDescription('88', description='', group='VIII'),
    ItemDescription('89', description='', group='VIII'),
    ItemDescription('90', description='', group='VII'),
    ItemDescription('91', description='', group='I'),
    ItemDescription('92', description='', group='V'),
    ItemDescription('93', description='', group='other'),
    ItemDescription('94', description='', group='VIII'),
    ItemDescription('95', description='', group='VIII'),
    ItemDescription('96', description='', group='VII'),
    ItemDescription('97', description='', group='VIII'),
    ItemDescription('98', description='', group='other'),
    ItemDescription('99', description='', group='VII'),
    ItemDescription('100', description='', group='V'),
    ItemDescription('101', description='', group='VII'),
    ItemDescription('102', description='', group='II'),
    ItemDescription('103', description='', group='II'),
    ItemDescription('104', description='', group='VIII'),
    ItemDescription('105', description='', group='VII'),
    ItemDescription('106', description='', group='VII'),
    ItemDescription('107', description='', group='other'),
    ItemDescription('108', description='', group='other'),
    ItemDescription('109', description='', group='other'),
    ItemDescription('110', description='', group='other'),
    ItemDescription('111', description='', group='II'),
    ItemDescription('112', description='', group='I'),
    ItemDescription('113', description='', group='other'),
]

def create_cbcl_6_18_test_items(test_id):
    test = Test.objects.get(id=test_id)
    items = [
        Item.objects.create(
            test=test,
            number=item.number,
            description=item.description,
            group=item.group
        ) for item in cbcl_6_18_items
    ]


def calculate_cbcl_6_18_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['a'] = raw_scores['I'] + raw_scores['II'] + raw_scores['III']
    raw_scores['b'] = raw_scores['VII'] + raw_scores['VIII']
    raw_scores['c'] = raw_scores['IV'] + raw_scores['V'] + raw_scores['VI'] + raw_scores['other']
    raw_scores['total'] = raw_scores['a'] + raw_scores['b'] + raw_scores['c']
    return convert_to_return_value(raw_scores, test)


def convert_to_return_value(raw_scores, test):
    score_list = []

    score_list.append({'group': 'I', 'score': raw_scores.pop('I')})
    score_list.append({'group': 'II', 'score': raw_scores.pop('II')})
    score_list.append({'group': 'III', 'score': raw_scores.pop('III')})
    score_list.append({'group': 'IV', 'score': raw_scores.pop('IV')})
    score_list.append({'group': 'V', 'score': raw_scores.pop('V')})
    score_list.append({'group': 'VI', 'score': raw_scores.pop('VI')})
    score_list.append({'group': 'VII', 'score': raw_scores.pop('VII')})
    score_list.append({'group': 'VIII', 'score': raw_scores.pop('VIII')})
    score_list.append({'group': 'other', 'score': raw_scores.pop('other')})
    score_list.append({'group': 'a', 'score': raw_scores.pop('a')})
    score_list.append({'group': 'b', 'score': raw_scores.pop('b')})
    score_list.append({'group': 'c', 'score': raw_scores.pop('c')})
    score_list.append({'group': 'total', 'score': raw_scores.pop('total')})

    if raw_scores.keys():
        # There should not be anything left in raw scores
        raise APIException(f"Extra data was in raw scores, check scoring logic. Extra data: {raw_scores.keys()}")

    serializer = TestSerializer(test)
    return {"scores": score_list, "test": serializer.data}
