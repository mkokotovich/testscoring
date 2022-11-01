from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class Brief2(BaseAssessment):
    test_type = Test.BRIEF2

    items = [
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

    results_order = [
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
        'Negativity Score',
        'Infrequency Score',
        'Inconsistency Score',
    ]

    def calculate_negativity_score(self, test):
        negativity_item_numbers = (14, 28, 30, 34, 39, 41, 58, 60)
        significant_items = test.items.filter(number__in=negativity_item_numbers, score=3)

        negativity_score = significant_items.count()
        if negativity_score < 7:
            negativity_classification = "Acceptable"
        elif negativity_score == 7:
            negativity_classification = "Elevated"
        else:
            negativity_classification = "Highly elevated"

        return f"{negativity_score} ({negativity_classification})"

    def calculate_infrequency_score(self, test):
        infrequency_item_numbers = (18, 36, 54)
        significant_items = test.items.filter(number__in=infrequency_item_numbers, score__gte=2)

        infrequency_score = significant_items.count()
        if infrequency_score == 0:
            infrequency_classification = "Acceptable"
        else:
            infrequency_classification = "Questionable"

        return f"{infrequency_score} ({infrequency_classification})"

    def calculate_inconsistency_score(self, test):
        inconsistency_item_pairs = (
            (5, 21),
            (9, 55),
            (10, 48),
            (17, 40),
            (20, 26),
            (22, 56),
            (25, 50),
            (37, 63),
        )
        inconsistency_differences = [
            abs(test.items.get(number=pair[0]).score - test.items.get(number=pair[1]).score)
            for pair in inconsistency_item_pairs
        ]
        inconsistency_score = sum(inconsistency_differences)

        if inconsistency_score < 7:
            inconsistency_classification = "Acceptable"
        elif inconsistency_score < 11:
            inconsistency_classification = "Questionable"
        else:
            inconsistency_classification = "Inconsistent"

        return f"{inconsistency_score} ({inconsistency_classification})"

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
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
        raw_scores['Negativity Score'] = self.calculate_negativity_score(test)
        raw_scores['Infrequency Score'] = self.calculate_infrequency_score(test)
        raw_scores['Inconsistency Score'] = self.calculate_inconsistency_score(test)

        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj


class BriefP(BaseAssessment):
    test_type = Test.BRIEFP

    items = [
        ItemDescription('1', description='', group='Emotional Control'),
        ItemDescription('2', description='', group='Working Memory'),
        ItemDescription('3', description='', group='Inhibit'),
        ItemDescription('4', description='', group='Plan/Organize'),
        ItemDescription('5', description='', group='Shift'),
        ItemDescription('6', description='', group='Emotional Control'),
        ItemDescription('7', description='', group='Working Memory'),
        ItemDescription('8', description='', group='Inhibit'),
        ItemDescription('9', description='', group='Plan/Organize'),
        ItemDescription('10', description='', group='Shift'),
        ItemDescription('11', description='', group='Emotional Control'),
        ItemDescription('12', description='', group='Working Memory'),
        ItemDescription('13', description='', group='Inhibit'),
        ItemDescription('14', description='', group='Plan/Organize'),
        ItemDescription('15', description='', group='Shift'),
        ItemDescription('16', description='', group='Emotional Control'),
        ItemDescription('17', description='', group='Working Memory'),
        ItemDescription('18', description='', group='Inhibit'),
        ItemDescription('19', description='', group='Plan/Organize'),
        ItemDescription('20', description='', group='Shift'),
        ItemDescription('21', description='', group='Emotional Control'),
        ItemDescription('22', description='', group='Working Memory'),
        ItemDescription('23', description='', group='Inhibit'),
        ItemDescription('24', description='', group='Plan/Organize'),
        ItemDescription('25', description='', group='Shift'),
        ItemDescription('26', description='', group='Emotional Control'),
        ItemDescription('27', description='', group='Working Memory'),
        ItemDescription('28', description='', group='Inhibit'),
        ItemDescription('29', description='', group='Plan/Organize'),
        ItemDescription('30', description='', group='Shift'),
        ItemDescription('31', description='', group='Emotional Control'),
        ItemDescription('32', description='', group='Working Memory'),
        ItemDescription('33', description='', group='Inhibit'),
        ItemDescription('34', description='', group='Plan/Organize'),
        ItemDescription('35', description='', group='Shift'),
        ItemDescription('36', description='', group='Emotional Control'),
        ItemDescription('37', description='', group='Working Memory'),
        ItemDescription('38', description='', group='Inhibit'),
        ItemDescription('39', description='', group='Plan/Organize'),
        ItemDescription('40', description='', group='Shift'),
        ItemDescription('41', description='', group='Emotional Control'),
        ItemDescription('42', description='', group='Working Memory'),
        ItemDescription('43', description='', group='Inhibit'),
        ItemDescription('44', description='', group='Plan/Organize'),
        ItemDescription('45', description='', group='Shift'),
        ItemDescription('46', description='', group='Emotional Control'),
        ItemDescription('47', description='', group='Working Memory'),
        ItemDescription('48', description='', group='Inhibit'),
        ItemDescription('49', description='', group='Plan/Organize'),
        ItemDescription('50', description='', group='Shift'),
        ItemDescription('51', description='', group='Working Memory'),
        ItemDescription('52', description='', group='Inhibit'),
        ItemDescription('53', description='', group='Working Memory'),
        ItemDescription('54', description='', group='Inhibit'),
        ItemDescription('55', description='', group='Working Memory'),
        ItemDescription('56', description='', group='Inhibit'),
        ItemDescription('57', description='', group='Working Memory'),
        ItemDescription('58', description='', group='Inhibit'),
        ItemDescription('59', description='', group='Working Memory'),
        ItemDescription('60', description='', group='Inhibit'),
        ItemDescription('61', description='', group='Working Memory'),
        ItemDescription('62', description='', group='Inhibit'),
        ItemDescription('63', description='', group='Working Memory'),
    ]

    results_order = [
        'Inhibit',
        'Shift',
        'Emotional Control',
        'Working Memory',
        'Plan/Organize',
        'ISCI',
        'FI',
        'EMI',
        'GEC',
    ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['ISCI'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Inhibit', 'Emotional Control']
        ])
        raw_scores['FI'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Shift', 'Emotional Control']
        ])
        raw_scores['EMI'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Working Memory', 'Plan/Organize']
        ])
        raw_scores['GEC'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Inhibit', 'Shift', 'Emotional Control', 'Working Memory', 'Plan/Organize']
        ])
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj


class BriefA(BaseAssessment):
    test_type = Test.BRIEFA

    items = [
        ItemDescription('1', description='', group='Emotional Control'),
        ItemDescription('2', description='', group='Task Monitor'),
        ItemDescription('3', description='', group='Organization of Materials'),
        ItemDescription('4', description='', group='Working Memory'),
        ItemDescription('5', description='', group='Inhibit'),
        ItemDescription('6', description='', group='Initiate'),
        ItemDescription('7', description='', group='Organization of Materials'),
        ItemDescription('8', description='', group='Shift'),
        ItemDescription('9', description='', group='Plan/Organize'),
        ItemDescription('10', description='', group='none'),
        ItemDescription('11', description='', group='Working Memory'),
        ItemDescription('12', description='', group='Emotional Control'),
        ItemDescription('13', description='', group='Self-Monitor'),
        ItemDescription('14', description='', group='Initiate'),
        ItemDescription('15', description='', group='Plan/Organize'),
        ItemDescription('16', description='', group='Inhibit'),
        ItemDescription('17', description='', group='Working Memory'),
        ItemDescription('18', description='', group='Task Monitor'),
        ItemDescription('19', description='', group='Emotional Control'),
        ItemDescription('20', description='', group='Initiate'),
        ItemDescription('21', description='', group='Plan/Organize'),
        ItemDescription('22', description='', group='Shift'),
        ItemDescription('23', description='', group='Self-Monitor'),
        ItemDescription('24', description='', group='Task Monitor'),
        ItemDescription('25', description='', group='Initiate'),
        ItemDescription('26', description='', group='Working Memory'),
        ItemDescription('27', description='', group='none'),
        ItemDescription('28', description='', group='Emotional Control'),
        ItemDescription('29', description='', group='Inhibit'),
        ItemDescription('30', description='', group='Organization of Materials'),
        ItemDescription('31', description='', group='Organization of Materials'),
        ItemDescription('32', description='', group='Shift'),
        ItemDescription('33', description='', group='Emotional Control'),
        ItemDescription('34', description='', group='Plan/Organize'),
        ItemDescription('35', description='', group='Working Memory'),
        ItemDescription('36', description='', group='Inhibit'),
        ItemDescription('37', description='', group='Self-Monitor'),
        ItemDescription('38', description='', group='none'),
        ItemDescription('39', description='', group='Plan/Organize'),
        ItemDescription('40', description='', group='Organization of Materials'),
        ItemDescription('41', description='', group='Task Monitor'),
        ItemDescription('42', description='', group='Emotional Control'),
        ItemDescription('43', description='', group='Inhibit'),
        ItemDescription('44', description='', group='Shift'),
        ItemDescription('45', description='', group='Initiate'),
        ItemDescription('46', description='', group='Working Memory'),
        ItemDescription('47', description='', group='Plan/Organize'),
        ItemDescription('48', description='', group='none'),
        ItemDescription('49', description='', group='Initiate'),
        ItemDescription('50', description='', group='Self-Monitor'),
        ItemDescription('51', description='', group='Emotional Control'),
        ItemDescription('52', description='', group='Task Monitor'),
        ItemDescription('53', description='', group='Initiate'),
        ItemDescription('54', description='', group='Plan/Organize'),
        ItemDescription('55', description='', group='Inhibit'),
        ItemDescription('56', description='', group='Working Memory'),
        ItemDescription('57', description='', group='Emotional Control'),
        ItemDescription('58', description='', group='Inhibit'),
        ItemDescription('59', description='', group='none'),
        ItemDescription('60', description='', group='Organization of Materials'),
        ItemDescription('61', description='', group='Shift'),
        ItemDescription('62', description='', group='Initiate'),
        ItemDescription('63', description='', group='Plan/Organize'),
        ItemDescription('64', description='', group='Self-Monitor'),
        ItemDescription('65', description='', group='Organization of Materials'),
        ItemDescription('66', description='', group='Plan/Organize'),
        ItemDescription('67', description='', group='Shift'),
        ItemDescription('68', description='', group='Working Memory'),
        ItemDescription('69', description='', group='Emotional Control'),
        ItemDescription('70', description='', group='Self-Monitor'),
        ItemDescription('71', description='', group='Plan/Organize'),
        ItemDescription('72', description='', group='Emotional Control'),
        ItemDescription('73', description='', group='Inhibit'),
        ItemDescription('74', description='', group='Organization of Materials'),
        ItemDescription('75', description='', group='Task Monitor'),
    ]

    results_order = [
        'Inhibit',
        'Shift',
        'Emotional Control',
        'Self-Monitor',
        'Initiate',
        'Working Memory',
        'Plan/Organize',
        'Task Monitor',
        'Organization of Materials',
        'BRI',
        'MI',
        'GEC',
        'Negativity Score',
        'Infrequency Score',
        'Inconsistency Score',
    ]

    def calculate_negativity_score(self, test):
        negativity_item_numbers = (1, 8, 19, 21, 22, 23, 29, 36, 39, 40)
        significant_items = test.items.filter(number__in=negativity_item_numbers, score=3)

        negativity_score = significant_items.count()
        if negativity_score < 5:
            negativity_classification = "Acceptable"
        else:
            negativity_classification = "Elevated"

        return f"{negativity_score} ({negativity_classification})"

    def calculate_infrequency_score(self, test):
        significant_scores_by_item_number = {
            10: 3,
            27: 1,
            38: 3,
            48: 1,
            59: 1,
        }
        infrequency_items = test.items.filter(number__in=significant_scores_by_item_number.keys())
        significant_items = [item for item in infrequency_items if int(item.score) == significant_scores_by_item_number.get(int(item.number))]

        infrequency_score = len(significant_items)
        if infrequency_score < 3:
            infrequency_classification = "Acceptable"
        else:
            infrequency_classification = "Infrequent"

        return f"{infrequency_score} ({infrequency_classification})"

    def calculate_inconsistency_score(self, test):
        inconsistency_item_pairs = (
            (2, 41),
            (25, 49),
            (28, 42),
            (33, 72),
            (34, 63),
            (44, 61),
            (46, 56),
            (52, 75),
            (60, 74),
            (64, 70),
        )
        inconsistency_differences = [
            abs(test.items.get(number=pair[0]).score - test.items.get(number=pair[1]).score)
            for pair in inconsistency_item_pairs
        ]
        inconsistency_score = sum(inconsistency_differences)

        if inconsistency_score < 8:
            inconsistency_classification = "Acceptable"
        else:
            inconsistency_classification = "Inconsistent"

        return f"{inconsistency_score} ({inconsistency_classification})"

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['BRI'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Inhibit', 'Shift', 'Emotional Control', 'Self-Monitor']
        ])
        raw_scores['MI'] = sum([
            value for key, value in raw_scores.items()
            if key in ['Initiate', 'Working Memory', 'Plan/Organize', 'Task Monitor', 'Organization of Materials']
        ])
        raw_scores['GEC'] = raw_scores['BRI'] + raw_scores['MI']
        raw_scores['Negativity Score'] = self.calculate_negativity_score(test)
        raw_scores['Infrequency Score'] = self.calculate_infrequency_score(test)
        raw_scores['Inconsistency Score'] = self.calculate_inconsistency_score(test)

        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
