from functools import reduce

from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


conners3_parent_items = [
    ItemDescription('1', description='', group='NI'),
    ItemDescription('2', description='', group='AN'),
    ItemDescription('3', description='', group='AH'),
    ItemDescription('4', description='', group='none'),
    ItemDescription('5', description='', group='LP'),
    ItemDescription('6', description='', group='CD'),
    ItemDescription('7', description='', group='LP'),
    ItemDescription('8', description='', group='NI'),
    ItemDescription('9', description='', group='LP'),
    ItemDescription('10', description='', group='PR'),
    ItemDescription('11', description='', group='CD'),
    ItemDescription('12', description='', group='IN'),
    ItemDescription('13', description='', group='PR'),
    ItemDescription('14', description='', group='OD'),
    ItemDescription('15', description='', group='LP'),
    ItemDescription('16', description='', group='AG|CD'),
    ItemDescription('17', description='', group='none'),
    ItemDescription('18', description='', group='NI'),
    ItemDescription('19', description='', group='HY|GI'),
    ItemDescription('20', description='', group='none'),
    ItemDescription('21', description='', group='OD'),
    ItemDescription('22', description='', group='AG'),
    ItemDescription('23', description='', group='IN'),
    ItemDescription('24', description='', group='PR'),
    ItemDescription('25', description='', group='GI'),
    ItemDescription('26', description='', group='NI'),
    ItemDescription('27', description='', group='AG|CD'),
    ItemDescription('28', description='', group='IN|AN'),
    ItemDescription('29', description='', group='GI'),
    ItemDescription('30', description='', group='AG|CD'),
    ItemDescription('31', description='', group='PI'),
    ItemDescription('32', description='', group='NI'),
    ItemDescription('33', description='', group='PI'),
    ItemDescription('34', description='', group='EF|GI'),
    ItemDescription('35', description='', group='AN'),
    ItemDescription('36', description='', group='LP'),
    ItemDescription('37', description='', group='EF'),
    ItemDescription('38', description='', group='PI'),
    ItemDescription('39', description='', group='CD|AG'),
    ItemDescription('40', description='', group='GI'),
    ItemDescription('41', description='', group='CD'),
    ItemDescription('42', description='', group='NI'),
    ItemDescription('43', description='', group='HY|AH'),
    ItemDescription('44', description='', group='IN'),
    ItemDescription('45', description='', group='HY|AH'),
    ItemDescription('46', description='', group='AG'),
    ItemDescription('47', description='', group='IN|AN'),
    ItemDescription('48', description='', group='AG|OD'),
    ItemDescription('49', description='', group='IN'),
    ItemDescription('50', description='', group='HY|GI'),
    ItemDescription('51', description='', group='LP'),
    ItemDescription('52', description='', group='HY'),
    ItemDescription('53', description='', group='LP'),
    ItemDescription('54', description='', group='HY|AH'),
    ItemDescription('55', description='', group='HY'),
    ItemDescription('56', description='', group='CD'),
    ItemDescription('57', description='', group='AG|OD'),
    ItemDescription('58', description='', group='AG|CD'),
    ItemDescription('59', description='', group='OD'),
    ItemDescription('60', description='', group='LP'),
    ItemDescription('61', description='', group='HY|AH'),
    ItemDescription('62', description='', group='PR'),
    ItemDescription('63', description='', group='EF'),
    ItemDescription('64', description='', group='PR'),
    ItemDescription('65', description='', group='AG|CD'),
    ItemDescription('66', description='', group='none'),
    ItemDescription('67', description='', group='IN|GI'),
    ItemDescription('68', description='', group='AN'),
    ItemDescription('69', description='', group='HY|AH'),
    ItemDescription('70', description='', group='none'),
    ItemDescription('71', description='', group='HY|AH'),
    ItemDescription('72', description='', group='EF'),
    ItemDescription('73', description='', group='OD'),
    ItemDescription('74', description='', group='PI'),
    ItemDescription('75', description='', group='EF'),
    ItemDescription('76', description='', group='CD'),
    ItemDescription('77', description='', group='IN'),
    ItemDescription('78', description='', group='CD'),
    ItemDescription('79', description='', group='EF|AN'),
    ItemDescription('80', description='', group='PI'),
    ItemDescription('81', description='', group='GI'),
    ItemDescription('82', description='', group='none'),
    ItemDescription('83', description='', group='AG'),
    ItemDescription('84', description='', group='EF|AN'),
    ItemDescription('85', description='', group='GI'),
    ItemDescription('86', description='', group='AG'),
    ItemDescription('87', description='', group='LP'),
    ItemDescription('88', description='', group='IN'),
    ItemDescription('89', description='', group='CD'),
    ItemDescription('90', description='', group='EF'),
    ItemDescription('91', description='', group='CD'),
    ItemDescription('92', description='', group='PR'),
    ItemDescription('93', description='', group='HY|AH'),
    ItemDescription('94', description='', group='AG|OD'),
    ItemDescription('95', description='', group='IN|AN'),
    ItemDescription('96', description='', group='CD'),
    ItemDescription('97', description='', group='EF|AN'),
    ItemDescription('98', description='', group='HY|AH'),
    ItemDescription('99', description='', group='HY|GI|AH'),
    ItemDescription('100', description='', group='none'),
    ItemDescription('101', description='', group='AN'),
    ItemDescription('102', description='', group='AG|OD'),
    ItemDescription('103', description='', group='none'),
    ItemDescription('104', description='', group='HY|AH'),
    ItemDescription('105', description='', group='PI'),
    ItemDescription('106', description='', group='none'),
    ItemDescription('107', description='', group='none'),
    ItemDescription('108', description='', group='none'),
]


conners3_parent_results_order = [
    'IN',
    'HY',
    'LP',
    'EF',
    'AG',
    'PR',
    'GI',
    'AN',
    'AH',
    'CD',
    'OD',
    'PI',
    'NI',
]


def create_conners3_parent_test_items(test_id):
    create_test_items(test_id, conners3_parent_items)


class ADHDCriteria():
    def __init__(self, criteria, items, min_score, all_required=True):
        self.criteria = criteria
        self.items = items
        self.min_score = min_score
        self.all_required = all_required

    def is_indicated(self, test):
        scores = [test.items.get(number=item_number).score for item_number in self.items]
        indicated_items = reduce(lambda accum, score: accum + 1 if score >= self.min_score else accum,
                                 scores,
                                 0)
        return indicated_items == len(self.items) if self.all_required else indicated_items > 0


adhd_inattentive_criterion = [
    ADHDCriteria('A1a', ['47'], 2),
    ADHDCriteria('A1b', ['95'], 2),
    ADHDCriteria('A1c', ['35'], 2),
    ADHDCriteria('A1d', ['68', '79'], 2, all_required=True),
    ADHDCriteria('A1e', ['84'], 2),
    ADHDCriteria('A1f', ['28'], 3),
    ADHDCriteria('A1g', ['97'], 2),
    ADHDCriteria('A1h', ['101'], 2),
    ADHDCriteria('A1i', ['2'], 2),
]


adhd_hyperactive_impulsive_criterion = [
    ADHDCriteria('A2a', ['98'], 2),
    ADHDCriteria('A2b', ['93'], 2),
    ADHDCriteria('A2c', ['69', '99'], 2, all_required=False),
    ADHDCriteria('A2d', ['71'], 2),
    ADHDCriteria('A2e', ['54', '45'], 2, all_required=False),
    ADHDCriteria('A2f', ['3'], 2),
    ADHDCriteria('A2g', ['43'], 2),
    ADHDCriteria('A2h', ['61'], 2),
    ADHDCriteria('A2i', ['104'], 2),
]


def calculate_adhd_scores(raw_scores, test):
    inattentive = reduce(lambda accum, criteria: accum + (1 if criteria.is_indicated(test) else 0),
                         adhd_inattentive_criterion,
                         0)

    hyperactive = reduce(lambda accum, criteria: accum + (1 if criteria.is_indicated(test) else 0),
                         adhd_hyperactive_impulsive_criterion,
                         0)

    return [
        {
            'group': 'ADHD Inattentive Symptom Count',
            'score': inattentive,
        },
        {
            'group': 'ADHD Hyperactive Impulsive Symptom Count',
            'score': hyperactive,
        },
    ]


def calculate_conners3_parent_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    return_obj = convert_to_return_value(raw_scores, conners3_parent_results_order, test)
    adhd_scores = calculate_adhd_scores(raw_scores, test)
    return_obj['scores'].extend(adhd_scores)
    return return_obj
