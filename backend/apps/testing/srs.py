from functools import reduce

from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


srs2_items = [
    ItemDescription('1', description='', group='Mot'),
    ItemDescription('2', description='', group='Awr'),
    ItemDescription('3', description='', group='Mot'),
    ItemDescription('4', description='', group='RRB'),
    ItemDescription('5', description='', group='Cog'),
    ItemDescription('6', description='', group='Mot'),
    ItemDescription('7', description='', group='Awr'),
    ItemDescription('8', description='', group='RRB'),
    ItemDescription('9', description='', group='Mot'),
    ItemDescription('10', description='', group='Cog'),
    ItemDescription('11', description='', group='Mot'),
    ItemDescription('12', description='', group='Com'),
    ItemDescription('13', description='', group='Com'),
    ItemDescription('14', description='', group='RRB'),
    ItemDescription('15', description='', group='Cog'),
    ItemDescription('16', description='', group='Com'),
    ItemDescription('17', description='', group='Cog'),
    ItemDescription('18', description='', group='Com'),
    ItemDescription('19', description='', group='Com'),
    ItemDescription('20', description='', group='RRB'),
    ItemDescription('21', description='', group='Com'),
    ItemDescription('22', description='', group='Com'),
    ItemDescription('23', description='', group='Mot'),
    ItemDescription('24', description='', group='RRB'),
    ItemDescription('25', description='', group='Awr'),
    ItemDescription('26', description='', group='Com'),
    ItemDescription('27', description='', group='Mot'),
    ItemDescription('28', description='', group='RRB'),
    ItemDescription('29', description='', group='RRB'),
    ItemDescription('30', description='', group='Cog'),
    ItemDescription('31', description='', group='RRB'),
    ItemDescription('32', description='', group='Awr'),
    ItemDescription('33', description='', group='Com'),
    ItemDescription('34', description='', group='Mot'),
    ItemDescription('35', description='', group='Com'),
    ItemDescription('36', description='', group='Com'),
    ItemDescription('37', description='', group='Com'),
    ItemDescription('38', description='', group='Com'),
    ItemDescription('39', description='', group='RRB'),
    ItemDescription('40', description='', group='Cog'),
    ItemDescription('41', description='', group='Com'),
    ItemDescription('42', description='', group='Cog'),
    ItemDescription('43', description='', group='Mot'),
    ItemDescription('44', description='', group='Cog'),
    ItemDescription('45', description='', group='Awr'),
    ItemDescription('46', description='', group='Com'),
    ItemDescription('47', description='', group='Com'),
    ItemDescription('48', description='', group='Cog'),
    ItemDescription('49', description='', group='RRB'),
    ItemDescription('50', description='', group='RRB'),
    ItemDescription('51', description='', group='Com'),
    ItemDescription('52', description='', group='Awr'),
    ItemDescription('53', description='', group='Com'),
    ItemDescription('54', description='', group='Awr'),
    ItemDescription('55', description='', group='Com'),
    ItemDescription('56', description='', group='Awr'),
    ItemDescription('57', description='', group='Com'),
    ItemDescription('58', description='', group='Cog'),
    ItemDescription('59', description='', group='Cog'),
    ItemDescription('60', description='', group='Com'),
    ItemDescription('61', description='', group='Com'),
    ItemDescription('62', description='', group='Cog'),
    ItemDescription('63', description='', group='RRB'),
    ItemDescription('64', description='', group='Mot'),
    ItemDescription('65', description='', group='Mot'),
]


srs2_results_order = [
    'Awr',
    'Cog',
    'Com',
    'Mot',
    'RRB',
]


def create_srs2_test_items(test_id):
    create_test_items(test_id, srs2_items)


def calculate_srs2_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    return_obj = convert_to_return_value(raw_scores, srs2_results_order, test)
    return return_obj
