from functools import reduce

from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


brief2_items = [
    ItemDescription('1', description='', group='Inhibit'),
    ItemDescription('2', description='', group='Shift'),
    ItemDescription('3', description='', group='Working Memory'),
    ItemDescription('4', description='', group='Self-Monitor'),
    ItemDescription('5', description='', group='Task-Monitor'),
    ItemDescription('6', description='', group='Emotional Control'),
    ItemDescription('7', description='', group='Plan/Organize'),
    ItemDescription('8', description='', group='Organization of Materials'),
    ItemDescription('9', description='', group='Initiate'),
    ItemDescription('10', description='', group='Inhibit'),
    ItemDescription('11', description='', group='Shift'),
    ItemDescription('12', description='', group='Working Memory'),
    ItemDescription('13', description='', group='Self-Monitor'),
    ItemDescription('14', description='', group='Emotional Control'),
    ItemDescription('15', description='', group='Plan/Organize'),
    ItemDescription('16', description='', group='Inhibit'),
    ItemDescription('17', description='', group='Shift'),
    ItemDescription('18', description='', group='none'),
    ItemDescription('19', description='', group='Working Memory'),
    ItemDescription('20', description='', group='Self-Monitor'),
    ItemDescription('21', description='', group='Task-Monitor'),
    ItemDescription('22', description='', group='Emotional Control'),
    ItemDescription('23', description='', group='Plan/Organize'),
    ItemDescription('24', description='', group='Inhibit'),
    ItemDescription('25', description='', group='Working Memory'),
    ItemDescription('26', description='', group='Self-Monitor'),
    ItemDescription('27', description='', group='Emotional Control'),
    ItemDescription('28', description='', group='Working Memory'),
    ItemDescription('29', description='', group='Task-Monitor'),
    ItemDescription('30', description='', group='Inhibit'),
    ItemDescription('31', description='', group='Shift'),
    ItemDescription('32', description='', group='Working Memory'),
    ItemDescription('33', description='', group='Task-Monitor'),
    ItemDescription('34', description='', group='Emotional Control'),
    ItemDescription('35', description='', group='Plan/Organize'),
    ItemDescription('36', description='', group='none'),
    ItemDescription('37', description='', group='Organization of Materials'),
    ItemDescription('38', description='', group='Initiate'),
    ItemDescription('39', description='', group='Inhibit'),
    ItemDescription('40', description='', group='Shift'),
    ItemDescription('41', description='', group='Working Memory'),
    ItemDescription('42', description='', group='Task-Monitor'),
    ItemDescription('43', description='', group='Emotional Control'),
    ItemDescription('44', description='', group='Plan/Organize'),
    ItemDescription('45', description='', group='Organization of Materials'),
    ItemDescription('46', description='', group='Working Memory'),
    ItemDescription('47', description='', group='Organization of Materials'),
    ItemDescription('48', description='', group='Inhibit'),
    ItemDescription('49', description='', group='Shift'),
    ItemDescription('50', description='', group='Initiate'),
    ItemDescription('51', description='', group='Emotional Control'),
    ItemDescription('52', description='', group='Plan/Organize'),
    ItemDescription('53', description='', group='Organization of Materials'),
    ItemDescription('54', description='', group='none'),
    ItemDescription('55', description='', group='Initiate'),
    ItemDescription('56', description='', group='Emotional Control'),
    ItemDescription('57', description='', group='Plan/Organize'),
    ItemDescription('58', description='', group='Shift'),
    ItemDescription('59', description='', group='Plan/Organize'),
    ItemDescription('60', description='', group='Shift'),
    ItemDescription('61', description='', group='Initiate'),
    ItemDescription('62', description='', group='Inhibit'),
    ItemDescription('63', description='', group='Organization of Materials'),
]


brief2_results_order = [
    'Inhibit',
    'Self-Monitor',
    'Shift',
    'Emotional Control',
    'Initiate',
    'Working Memory',
    'Plan/Organize',
    'Task-Monitor',
    'Organization of Materials',
    'BRI',
    'ERI',
    'CRI',
    'GEC',
]


def create_brief2_test_items(test_id):
    create_test_items(test_id, brief2_items)


def calculate_brief2_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['BRI'] = sum([
        value for key, value in raw_scores.items()
        if key in ['Inhibit', 'Self-Monitor']
    ])
    raw_scores['ERI'] = sum([
        value for key, value in raw_scores.items()
        if key in ['Shift', 'Emotional Control']
    ])
    raw_scores['CRI'] = sum([
        value for key, value in raw_scores.items()
        if key in ['Initiate', 'Working Memory', 'Plan/Organize', 'Task-Monitor', 'Organization of Materials']
    ])
    raw_scores['GEC'] = raw_scores['BRI'] + raw_scores['ERI'] + raw_scores['CRI']
    return_obj = convert_to_return_value(raw_scores, brief2_results_order, test)
    return return_obj
