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
    ]

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
