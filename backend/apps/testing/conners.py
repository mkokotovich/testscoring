from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


# Helper class used by Conners3 assessments
class ADHDCriteria():
    def __init__(self, criteria, item_score_tuples, all_required=True):
        self.criteria = criteria
        self.item_score_tuples = item_score_tuples
        self.all_required = all_required

    def is_indicated(self, test):
        items_greater_than_min = [
            1 if test.items.get(number=item_number).score >= min_score else 0
            for item_number, min_score in self.item_score_tuples
        ]
        indicated_items = sum(items_greater_than_min)
        return indicated_items == len(self.item_score_tuples) if self.all_required else indicated_items > 0


class Conners3Parent(BaseAssessment):
    test_type = Test.CONNERS3_PARENT

    items = [
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

    results_order = [
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

    adhd_inattentive_criterion = [
        ADHDCriteria('A1a', [('47', 2)]),
        ADHDCriteria('A1b', [('95', 2)]),
        ADHDCriteria('A1c', [('35', 2)]),
        ADHDCriteria('A1d', [('68', 2), ('79', 2)], all_required=True),
        ADHDCriteria('A1e', [('84', 2)]),
        ADHDCriteria('A1f', [('28', 3)]),
        ADHDCriteria('A1g', [('97', 2)]),
        ADHDCriteria('A1h', [('101', 2)]),
        ADHDCriteria('A1i', [('2', 2)]),
    ]

    adhd_hyperactive_impulsive_criterion = [
        ADHDCriteria('A2a', [('98', 2)]),
        ADHDCriteria('A2b', [('93', 2)]),
        ADHDCriteria('A2c', [('69', 2), ('99', 2)], all_required=False),
        ADHDCriteria('A2d', [('71', 2)]),
        ADHDCriteria('A2e', [('54', 2), ('45', 2)], all_required=False),
        ADHDCriteria('A2f', [('3', 2)]),
        ADHDCriteria('A2g', [('43', 2)]),
        ADHDCriteria('A2h', [('61', 2)]),
        ADHDCriteria('A2i', [('104', 2)]),
    ]

    def calculate_adhd_scores(self, raw_scores, test):
        inattentive = [
            criteria.criteria
            for criteria in self.adhd_inattentive_criterion
            if criteria.is_indicated(test)
        ]

        hyperactive = [
            criteria.criteria
            for criteria in self.adhd_hyperactive_impulsive_criterion
            if criteria.is_indicated(test)
        ]

        return [
            {
                'group': 'ADHD Inattentive Symptom Count',
                'score': f'{len(inattentive)} ({", ".join(inattentive)})',
            },
            {
                'group': 'ADHD Hyperactive Impulsive Symptom Count',
                'score': f'{len(hyperactive)} ({", ".join(hyperactive)})',
            },
        ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        adhd_scores = self.calculate_adhd_scores(raw_scores, test)
        return_obj['scores'].extend(adhd_scores)
        return return_obj


class Conners3Self(BaseAssessment):
    test_type = Test.CONNERS3_SELF

    items = [
        ItemDescription('1', description='', group='OD'),
        ItemDescription('2', description='', group='none'),
        ItemDescription('3', description='', group='OD'),
        ItemDescription('4', description='', group='HY'),
        ItemDescription('5', description='', group='AN'),
        ItemDescription('6', description='', group='HY|AH'),
        ItemDescription('7', description='', group='HY|AH'),
        ItemDescription('8', description='', group='AG|CD'),
        ItemDescription('9', description='', group='HY|AH'),
        ItemDescription('10', description='', group='NI'),
        ItemDescription('11', description='', group='NI'),
        ItemDescription('12', description='', group='PI'),
        ItemDescription('13', description='', group='CD'),
        ItemDescription('14', description='', group='FR'),
        ItemDescription('15', description='', group='LP'),
        ItemDescription('16', description='', group='AG|CD'),
        ItemDescription('17', description='', group='IN|AN'),
        ItemDescription('18', description='', group='AG'),
        ItemDescription('19', description='', group='NI'),
        ItemDescription('20', description='', group='HY|AH'),
        ItemDescription('21', description='', group='AN'),
        ItemDescription('22', description='', group='AG'),
        ItemDescription('23', description='', group='FR'),
        ItemDescription('24', description='', group='OD'),
        ItemDescription('25', description='', group='CD|AG'),
        ItemDescription('26', description='', group='FR'),
        ItemDescription('27', description='', group='AH'),
        ItemDescription('28', description='', group='NI'),
        ItemDescription('29', description='', group='none'),
        ItemDescription('30', description='', group='IN'),
        ItemDescription('31', description='', group='IN|AN'),
        ItemDescription('32', description='', group='AN'),
        ItemDescription('33', description='', group='AG|CD'),
        ItemDescription('34', description='', group='HY|AH'),
        ItemDescription('35', description='', group='LP'),
        ItemDescription('36', description='', group='none'),
        ItemDescription('37', description='', group='PI'),
        ItemDescription('38', description='', group='AG|CD'),
        ItemDescription('39', description='', group='AN'),
        ItemDescription('40', description='', group='NI'),
        ItemDescription('41', description='', group='NI'),
        ItemDescription('42', description='', group='AN'),
        ItemDescription('43', description='', group='IN'),
        ItemDescription('44', description='', group='none'),
        ItemDescription('45', description='', group='LP'),
        ItemDescription('46', description='', group='none'),
        ItemDescription('47', description='', group='CD'),
        ItemDescription('48', description='', group='PI'),
        ItemDescription('49', description='', group='IN'),
        ItemDescription('50', description='', group='HY'),
        ItemDescription('51', description='', group='AN'),
        ItemDescription('52', description='', group='AG|CD'),
        ItemDescription('53', description='', group='IN'),
        ItemDescription('54', description='', group='PI'),
        ItemDescription('55', description='', group='AH'),
        ItemDescription('56', description='', group='LP'),
        ItemDescription('57', description='', group='HY'),
        ItemDescription('58', description='', group='LP'),
        ItemDescription('59', description='', group='AG|CD'),
        ItemDescription('60', description='', group='HY|AH'),
        ItemDescription('61', description='', group='AN'),
        ItemDescription('62', description='', group='AG|OD'),
        ItemDescription('63', description='', group='IN|AN'),
        ItemDescription('64', description='', group='HY|AH'),
        ItemDescription('65', description='', group='LP'),
        ItemDescription('66', description='', group='HY|AH'),
        ItemDescription('67', description='', group='OD'),
        ItemDescription('68', description='', group='none'),
        ItemDescription('69', description='', group='FR'),
        ItemDescription('70', description='', group='LP'),
        ItemDescription('71', description='', group='IN'),
        ItemDescription('72', description='', group='AG|CD'),
        ItemDescription('73', description='', group='FR'),
        ItemDescription('74', description='', group='OD'),
        ItemDescription('75', description='', group='PI'),
        ItemDescription('76', description='', group='LP'),
        ItemDescription('77', description='', group='IN|AN'),
        ItemDescription('78', description='', group='CD'),
        ItemDescription('79', description='', group='IN'),
        ItemDescription('80', description='', group='none'),
        ItemDescription('81', description='', group='IN'),
        ItemDescription('82', description='', group='AG|CD'),
        ItemDescription('83', description='', group='FR'),
        ItemDescription('84', description='', group='HY|AH'),
        ItemDescription('85', description='', group='FR'),
        ItemDescription('86', description='', group='AG|CD'),
        ItemDescription('87', description='', group='OD'),
        ItemDescription('88', description='', group='HY'),
        ItemDescription('89', description='', group='FR'),
        ItemDescription('90', description='', group='none'),
        ItemDescription('91', description='', group='AG|CD'),
        ItemDescription('92', description='', group='HY'),
        ItemDescription('93', description='', group='PI'),
        ItemDescription('94', description='', group='AG|OD'),
        ItemDescription('95', description='', group='none'),
        ItemDescription('96', description='', group='none'),
        ItemDescription('97', description='', group='none'),
    ]

    results_order = [
        'IN',
        'HY',
        'LP',
        'AG',
        'FR',
        'AN',
        'AH',
        'CD',
        'OD',
        'PI',
        'NI',
    ]

    adhd_inattentive_criterion = [
        ADHDCriteria('A1a', [('31', 2), ('39', 3)], all_required=False),
        ADHDCriteria('A1b', [('63', 2)]),
        ADHDCriteria('A1c', [('42', 2)]),
        ADHDCriteria('A1d', [('61', 2), ('17', 2)], all_required=True),
        ADHDCriteria('A1e', [('21', 3)]),
        ADHDCriteria('A1f', [('51', 3)]),
        ADHDCriteria('A1g', [('5', 2)]),
        ADHDCriteria('A1h', [('77', 3)]),
        ADHDCriteria('A1i', [('32', 3)]),
    ]

    adhd_hyperactive_impulsive_criterion = [
        ADHDCriteria('A2a', [('60', 3)]),
        ADHDCriteria('A2b', [('64', 2)]),
        ADHDCriteria('A2c', [('20', 2), ('7', 2)], all_required=False),
        ADHDCriteria('A2d', [('84', 2)]),
        ADHDCriteria('A2e', [('66', 2), ('55', 3)], all_required=False),
        ADHDCriteria('A2f', [('34', 2)]),
        ADHDCriteria('A2g', [('9', 2)]),
        ADHDCriteria('A2h', [('27', 2)]),
        ADHDCriteria('A2i', [('6', 2)]),
    ]

    def calculate_adhd_scores(self, raw_scores, test):
        inattentive = [
            criteria.criteria
            for criteria in self.adhd_inattentive_criterion
            if criteria.is_indicated(test)
        ]

        hyperactive = [
            criteria.criteria
            for criteria in self.adhd_hyperactive_impulsive_criterion
            if criteria.is_indicated(test)
        ]

        return [
            {
                'group': 'ADHD Inattentive Symptom Count',
                'score': f'{len(inattentive)} ({", ".join(inattentive)})',
            },
            {
                'group': 'ADHD Hyperactive Impulsive Symptom Count',
                'score': f'{len(hyperactive)} ({", ".join(hyperactive)})',
            },
        ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        adhd_scores = self.calculate_adhd_scores(raw_scores, test)
        return_obj['scores'].extend(adhd_scores)
        return return_obj
