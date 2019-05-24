from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class MASC2Self(BaseAssessment):
    test_type = Test.MASC2_SELF

    items = [
        ItemDescription('1', description='', group='T/R|GAD'),
        ItemDescription('2', description='', group='HA'),
        ItemDescription('3', description='', group='H/R'),
        ItemDescription('4', description='', group='S/P'),
        ItemDescription('5', description='', group='HA'),
        ItemDescription('6', description='', group='GAD|P'),
        ItemDescription('7', description='', group='S/P'),
        ItemDescription('8', description='', group='T/R'),
        ItemDescription('9', description='', group='S/P'),
        ItemDescription('10', description='', group='H/R'),
        ItemDescription('11', description='', group='HA'),
        ItemDescription('12', description='', group='P'),
        ItemDescription('13', description='', group='GAD|HA'),
        ItemDescription('14', description='', group='PF'),
        ItemDescription('15', description='', group='T/R'),
        ItemDescription('16', description='', group='H/R'),
        ItemDescription('17', description='', group='S/P|GAD'),
        ItemDescription('18', description='', group='P'),
        ItemDescription('19', description='', group='S/P'),
        ItemDescription('20', description='', group='P'),
        ItemDescription('21', description='', group='HA'),
        ItemDescription('22', description='', group='GAD|H/R'),
        ItemDescription('23', description='', group='S/P'),
        ItemDescription('24', description='', group='P'),
        ItemDescription('25', description='', group='HA'),
        ItemDescription('26', description='', group='S/P'),
        ItemDescription('27', description='', group='GAD|T/R'),
        ItemDescription('28', description='', group='HA'),
        ItemDescription('29', description='', group='GAD|H/R'),
        ItemDescription('30', description='', group='S/P'),
        ItemDescription('31', description='', group='GAD|P'),
        ItemDescription('32', description='', group='PF'),
        ItemDescription('33', description='', group='S/P'),
        ItemDescription('34', description='', group='T/R'),
        ItemDescription('35', description='', group='HA'),
        ItemDescription('36', description='', group='PF'),
        ItemDescription('37', description='', group='P'),
        ItemDescription('38', description='', group='PF'),
        ItemDescription('39', description='', group='GAD'),
        ItemDescription('40', description='', group='GAD'),
        ItemDescription('41', description='', group='OC'),
        ItemDescription('42', description='', group='OC'),
        ItemDescription('43', description='', group='OC'),
        ItemDescription('44', description='', group='OC'),
        ItemDescription('45', description='', group='OC'),
        ItemDescription('46', description='', group='OC'),
        ItemDescription('47', description='', group='OC'),
        ItemDescription('48', description='', group='OC'),
        ItemDescription('49', description='', group='OC'),
        ItemDescription('50', description='', group='OC'),
    ]

    results_order = [
        'S/P',
        'GAD',
        'SA:T',
        'H/R',
        'PF',
        'OC',
        'PS:T',
        'P',
        'T/R',
        'HA',
        'Total',
        'Inconsistency Index',
    ]

    def calculate_inconsistency_index(self, test):
        inconsistency_pairs = [(3, 10), (4, 9), (8, 15), (13, 35), (20, 27), (22, 29), (43, 44), (47, 50)]
        absolute_differences = [
            abs(test.items.get(number=left).score - test.items.get(number=right).score)
            for left, right in inconsistency_pairs
        ]
        inconsistency_index = sum(absolute_differences)
        return f"{inconsistency_index} ({'🚨GREATER🚨' if inconsistency_index > 8 else 'less'} than 8)"

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['SA:T'] = raw_scores['H/R'] + raw_scores['PF']
        raw_scores['PS:T'] = raw_scores['P'] + raw_scores['T/R']
        raw_scores['Total'] = (
            raw_scores['S/P']
            + raw_scores['SA:T']
            + raw_scores['OC']
            + raw_scores['PS:T']
            + raw_scores['HA']
            + test.items.get(number=39).score
            + test.items.get(number=40).score
        )
        raw_scores['Inconsistency Index'] = self.calculate_inconsistency_index(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj


class MASC2Parent(BaseAssessment):
    test_type = Test.MASC2_PARENT

    items = [
        ItemDescription('1', description='', group='T/R|GAD'),
        ItemDescription('2', description='', group='HA'),
        ItemDescription('3', description='', group='H/R'),
        ItemDescription('4', description='', group='S/P'),
        ItemDescription('5', description='', group='HA'),
        ItemDescription('6', description='', group='GAD|P'),
        ItemDescription('7', description='', group='S/P'),
        ItemDescription('8', description='', group='T/R'),
        ItemDescription('9', description='', group='S/P'),
        ItemDescription('10', description='', group='H/R'),
        ItemDescription('11', description='', group='HA'),
        ItemDescription('12', description='', group='P'),
        ItemDescription('13', description='', group='GAD|HA'),
        ItemDescription('14', description='', group='PF'),
        ItemDescription('15', description='', group='T/R'),
        ItemDescription('16', description='', group='H/R'),
        ItemDescription('17', description='', group='S/P|GAD'),
        ItemDescription('18', description='', group='P'),
        ItemDescription('19', description='', group='S/P'),
        ItemDescription('20', description='', group='P'),
        ItemDescription('21', description='', group='HA'),
        ItemDescription('22', description='', group='GAD|H/R'),
        ItemDescription('23', description='', group='S/P'),
        ItemDescription('24', description='', group='P'),
        ItemDescription('25', description='', group='HA'),
        ItemDescription('26', description='', group='S/P'),
        ItemDescription('27', description='', group='GAD|T/R'),
        ItemDescription('28', description='', group='HA'),
        ItemDescription('29', description='', group='GAD|H/R'),
        ItemDescription('30', description='', group='S/P'),
        ItemDescription('31', description='', group='GAD|P'),
        ItemDescription('32', description='', group='PF'),
        ItemDescription('33', description='', group='S/P'),
        ItemDescription('34', description='', group='T/R'),
        ItemDescription('35', description='', group='HA'),
        ItemDescription('36', description='', group='PF'),
        ItemDescription('37', description='', group='P'),
        ItemDescription('38', description='', group='PF'),
        ItemDescription('39', description='', group='GAD'),
        ItemDescription('40', description='', group='GAD'),
        ItemDescription('41', description='', group='OC'),
        ItemDescription('42', description='', group='OC'),
        ItemDescription('43', description='', group='OC'),
        ItemDescription('44', description='', group='OC'),
        ItemDescription('45', description='', group='OC'),
        ItemDescription('46', description='', group='OC'),
        ItemDescription('47', description='', group='OC'),
        ItemDescription('48', description='', group='OC'),
        ItemDescription('49', description='', group='OC'),
        ItemDescription('50', description='', group='OC'),
    ]

    results_order = [
        'S/P',
        'GAD',
        'SA:T',
        'H/R',
        'PF',
        'OC',
        'PS:T',
        'P',
        'T/R',
        'HA',
        'Total',
        'Inconsistency Index',
    ]

    def calculate_inconsistency_index(self, test):
        inconsistency_pairs = [(2, 11), (3, 10), (4, 9), (5, 13), (8, 15), (16, 22), (43, 44), (45, 46)]
        absolute_differences = [
            abs(test.items.get(number=left).score - test.items.get(number=right).score)
            for left, right in inconsistency_pairs
        ]
        inconsistency_index = sum(absolute_differences)
        return f"{inconsistency_index} ({'🚨GREATER🚨' if inconsistency_index > 8 else 'less'} than 8)"

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['SA:T'] = raw_scores['H/R'] + raw_scores['PF']
        raw_scores['PS:T'] = raw_scores['P'] + raw_scores['T/R']
        raw_scores['Total'] = (
            raw_scores['S/P']
            + raw_scores['SA:T']
            + raw_scores['OC']
            + raw_scores['PS:T']
            + raw_scores['HA']
            + test.items.get(number=39).score
            + test.items.get(number=40).score
        )
        raw_scores['Inconsistency Index'] = self.calculate_inconsistency_index(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
