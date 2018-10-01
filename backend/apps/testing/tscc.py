from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class TSCC(BaseAssessment):
    test_type = Test.TSCC

    items = [
        ItemDescription('1', description='', group='PTS'),
        ItemDescription('2', description='', group='ANX'),
        ItemDescription('3', description='', group='PTS'),
        ItemDescription('4', description='', group='SC|SC-P'),
        ItemDescription('5', description='', group='DIS|DIS-F'),
        ItemDescription('6', description='', group='ANG'),
        ItemDescription('7', description='', group='DEP'),
        ItemDescription('8', description='', group='SC|SC-P'),
        ItemDescription('9', description='', group='DEP'),
        ItemDescription('10', description='', group='PTS'),
        ItemDescription('11', description='', group='PTS|DIS|DIS-O'),
        ItemDescription('12', description='', group='PTS'),
        ItemDescription('13', description='', group='ANG'),
        ItemDescription('14', description='', group='DEP'),
        ItemDescription('15', description='', group='ANX'),
        ItemDescription('16', description='', group='ANG'),
        ItemDescription('17', description='', group='SC|SC-P'),
        ItemDescription('18', description='', group='DIS|DIS-O'),
        ItemDescription('19', description='', group='ANG'),
        ItemDescription('20', description='', group='DEP'),
        ItemDescription('21', description='', group='ANG'),
        ItemDescription('22', description='', group='SC|SC-P'),
        ItemDescription('23', description='', group='SC|SC-P|SC-D'),
        ItemDescription('24', description='', group='ANX|PTS'),
        ItemDescription('25', description='', group='ANX|PTS'),
        ItemDescription('26', description='', group='DEP'),
        ItemDescription('27', description='', group='DEP'),
        ItemDescription('28', description='', group='DEP'),
        ItemDescription('29', description='', group='DIS|DIS-O'),
        ItemDescription('30', description='', group='DIS|DIS-O'),
        ItemDescription('31', description='', group='DIS|DIS-O'),
        ItemDescription('32', description='', group='ANX'),
        ItemDescription('33', description='', group='ANX'),
        ItemDescription('34', description='', group='SC|SC-D'),
        ItemDescription('35', description='', group='PTS'),
        ItemDescription('36', description='', group='ANG'),
        ItemDescription('37', description='', group='ANG'),
        ItemDescription('38', description='', group='DIS|DIS-F'),
        ItemDescription('39', description='', group='ANX'),
        ItemDescription('40', description='', group='SC|SC-D'),
        ItemDescription('41', description='', group='ANX'),
        ItemDescription('42', description='', group='DEP'),
        ItemDescription('43', description='', group='PTS'),
        ItemDescription('44', description='', group='SC|SC-P'),
        ItemDescription('45', description='', group='DIS|DIS-O'),
        ItemDescription('46', description='', group='ANG'),
        ItemDescription('47', description='', group='SC|SC-P'),
        ItemDescription('48', description='', group='DIS|DIS-O'),
        ItemDescription('49', description='', group='ANG'),
        ItemDescription('50', description='', group='ANX'),
        ItemDescription('51', description='', group='PTS'),
        ItemDescription('52', description='', group='DEP'),
        ItemDescription('53', description='', group='DIS|DIS-F'),
        ItemDescription('54', description='', group='SC|SC-D'),
    ]

    results_order = [
        'ANX',
        'DEP',
        'ANG',
        'PTS',
        'DIS',
        'DIS-O',
        'DIS-F',
        'SC',
        'SC-P',
        'SC-D',
        'UND',
        'HYP',
    ]

    def calculate_und(self, items):
        possibles = items.filter(number__in=[1, 2, 6, 9, 10, 19, 28, 41, 49, 53])
        only_zeros = possibles.filter(score=0)
        numbers = [item.number for item in only_zeros]
        number_string = f" - ({', '.join(numbers)})" if numbers else ""
        return f"{only_zeros.count()}{number_string}"

    def calculate_hyp(self, items):
        possibles = items.filter(number__in=[1, 18, 24, 25, 26, 27, 39, 45])
        only_threes = possibles.filter(score=3)
        numbers = [item.number for item in only_threes]
        number_string = f" - ({', '.join(numbers)})" if numbers else ""
        return f"{only_threes.count()}{number_string}"

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['UND'] = self.calculate_und(test.items)
        raw_scores['HYP'] = self.calculate_hyp(test.items)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
