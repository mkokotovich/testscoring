from django.db.models import Q

from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class CAT_A(BaseAssessment):
    test_type = Test.CAT_A

    def reverse_score(self, score):
        return 5 - score

    items = [
        ItemDescription('1', description='', group='CM-ATT|CM-AO|CM-INT'),
        ItemDescription('2', description='', group='CM-IMP|CM-SOC|CM-EXT'),
        ItemDescription('3', description='', group='CM-ATT|CM-SOC|CM-INT', reverse_scoring=True),
        ItemDescription('4', description='', group='CM-HYP|CM-PER|CM-INT'),
        ItemDescription('5', description='', group='CM-HYP|CM-AO|CM-INT'),
        ItemDescription('6', description='', group='CM-HYP|CM-PER|CM-INT'),
        ItemDescription('7', description='', group='CM-IMP|CM-AO|CM-EXT'),
        ItemDescription('8', description='', group='CM-HYP|CM-PER|CM-EXT'),
        ItemDescription('9', description='', group='CM-HYP|CM-PER|CM-INT'),
        ItemDescription('10', description='', group='CM-ATT|CM-SOC|CM-EXT'),
        ItemDescription('11', description='', group='CM-HYP|CM-AO|CM-INT'),
        ItemDescription('12', description='', group='CM-IMP|CM-PER|CM-EXT', reverse_scoring=True),
        ItemDescription('13', description='', group='CM-IMP|CM-PER|CM-EXT'),
        ItemDescription('14', description='', group='CM-IMP|CM-SOC|CM-INT'),
        ItemDescription('15', description='', group='CM-HYP|CM-SOC|CM-EXT'),
        ItemDescription('16', description='', group='CM-ATT|CM-PER|CM-INT'),
        ItemDescription('17', description='', group='CM-ATT|CM-SOC|CM-EXT'),
        ItemDescription('18', description='', group='CM-IMP|CM-AO|CM-EXT'),
        ItemDescription('19', description='', group='CM-ATT|CM-PER|CM-EXT'),
        ItemDescription('20', description='', group='CM-HYP|CM-PER|CM-EXT'),
        ItemDescription('21', description='', group='CM-ATT|CM-AO|CM-INT'),
        ItemDescription('22', description='', group='CM-IMP|CM-PER|CM-INT'),
        ItemDescription('23', description='', group='CM-ATT|CM-SOC|CM-EXT'),
        ItemDescription('24', description='', group='CM-ATT|CM-SOC|CM-INT'),
        ItemDescription('25', description='', group='CM-IMP|CM-AO|CM-INT'),
        ItemDescription('26', description='', group='CM-HYP|CM-AO|CM-INT', reverse_scoring=True),
        ItemDescription('27', description='', group='CM-HYP|CM-PER|CM-EXT'),
        ItemDescription('28', description='', group='CM-ATT|CM-AO|CM-INT', reverse_scoring=True),
        ItemDescription('29', description='', group='CM-IMP|CM-SOC|CM-INT'),
        ItemDescription('30', description='', group='CM-HYP|CM-SOC|CM-EXT', reverse_scoring=True),
        ItemDescription('31', description='', group='CM-IMP|CM-SOC|CM-EXT'),
        ItemDescription('32', description='', group='CM-IMP|CM-AO|CM-EXT'),
        ItemDescription('33', description='', group='CM-IMP|CM-SOC|CM-INT'),
        ItemDescription('34', description='', group='CM-IMP|CM-AO|CM-INT'),
        ItemDescription('35', description='', group='CM-IMP|CM-SOC|CM-EXT'),
        ItemDescription('36', description='', group='CM-HYP|CM-SOC|CM-INT'),
        ItemDescription('37', description='', group='CM-ATT|CM-PER|CM-INT'),
        ItemDescription('38', description='', group='CM-HYP|CM-AO|CM-EXT'),
        ItemDescription('39', description='', group='CM-IMP|CM-PER|CM-EXT'),
        ItemDescription('40', description='', group='CM-ATT|CM-AO|CM-EXT'),
        ItemDescription('41', description='', group='CM-ATT|CM-AO|CM-EXT'),
        ItemDescription('42', description='', group='CM-HYP|CM-SOC|CM-INT'),
        ItemDescription('43', description='', group='CM-HYP|CM-AO|CM-EXT'),
        ItemDescription('44', description='', group='CM-IMP|CM-PER|CM-INT'),
        ItemDescription('45', description='', group='CM-HYP|CM-SOC|CM-INT'),
        ItemDescription('46', description='', group='CM-ATT|CM-PER|CM-EXT'),
        ItemDescription('47', description='', group='CM-HYP|CM-AO|CM-EXT'),
        ItemDescription('48', description='', group='CM-ATT|CM-SOC|CM-INT'),
        ItemDescription('49', description='', group='CM-ATT|CM-AO|CM-EXT'),
        ItemDescription('50', description='', group='CM-IMP|CM-AO|CM-INT'),
        ItemDescription('51', description='', group='CM-IMP|CM-PER|CM-INT', reverse_scoring=True),
        ItemDescription('52', description='', group='CM-ATT|CM-PER|CM-INT'),
        ItemDescription('53', description='', group='CM-HYP|CM-SOC|CM-EXT'),
        ItemDescription('54', description='', group='CM-ATT|CM-PER|CM-EXT'),
        ItemDescription('55', description='', group='CS-HYP|CS-PER|CS-EXT'),
        ItemDescription('56', description='', group='CS-IMP|CS-AO|CS-INT'),
        ItemDescription('57', description='', group='CS-IMP|CS-AO|CS-INT'),
        ItemDescription('58', description='', group='CS-HYP|CS-AO|CS-EXT'),
        ItemDescription('59', description='', group='CS-IMP|CS-AO|CS-EXT'),
        ItemDescription('60', description='', group='CS-ATT|CS-SOC|CS-EXT'),
        ItemDescription('61', description='', group='CS-HYP|CS-AO|CS-INT'),
        ItemDescription('62', description='', group='CS-IMP|CS-PER|CS-INT'),
        ItemDescription('63', description='', group='CS-ATT|CS-SOC|CS-EXT'),
        ItemDescription('64', description='', group='CS-IMP|CS-AO|CS-EXT'),
        ItemDescription('65', description='', group='CS-ATT|CS-AO|CS-EXT'),
        ItemDescription('66', description='', group='CS-IMP|CS-AO|CS-EXT'),
        ItemDescription('67', description='', group='CS-HYP|CS-SOC|CS-EXT'),
        ItemDescription('68', description='', group='CS-ATT|CS-SOC|CS-INT'),
        ItemDescription('69', description='', group='CS-IMP|CS-SOC|CS-INT'),
        ItemDescription('70', description='', group='CS-HYP|CS-AO|CS-EXT'),
        ItemDescription('71', description='', group='CS-HYP|CS-SOC|CS-EXT'),
        ItemDescription('72', description='', group='CS-HYP|CS-PER|CS-INT'),
        ItemDescription('73', description='', group='CS-HYP|CS-SOC|CS-INT'),
        ItemDescription('74', description='', group='CS-HYP|CS-AO|CS-INT'),
        ItemDescription('75', description='', group='CS-IMP|CS-PER|CS-INT', reverse_scoring=True),
        ItemDescription('76', description='', group='CS-HYP|CS-SOC|CS-INT'),
        ItemDescription('77', description='', group='CS-IMP|CS-SOC|CS-EXT'),
        ItemDescription('78', description='', group='CS-ATT|CS-SOC|CS-INT'),
        ItemDescription('79', description='', group='CS-ATT|CS-AO|CS-INT', reverse_scoring=True),
        ItemDescription('80', description='', group='CS-ATT|CS-PER|CS-EXT'),
        ItemDescription('81', description='', group='CS-IMP|CS-PER|CS-EXT'),
        ItemDescription('82', description='', group='CS-IMP|CS-AO|CS-INT', reverse_scoring=True),
        ItemDescription('83', description='', group='CS-HYP|CS-SOC|CS-EXT'),
        ItemDescription('84', description='', group='CS-IMP|CS-PER|CS-EXT'),
        ItemDescription('85', description='', group='CS-ATT|CS-AO|CS-EXT', reverse_scoring=True),
        ItemDescription('86', description='', group='CS-IMP|CS-SOC|CS-EXT'),
        ItemDescription('87', description='', group='CS-IMP|CS-PER|CS-INT'),
        ItemDescription('88', description='', group='CS-ATT|CS-AO|CS-INT'),
        ItemDescription('89', description='', group='CS-ATT|CS-PER|CS-EXT'),
        ItemDescription('90', description='', group='CS-HYP|CS-SOC|CS-INT', reverse_scoring=True),
        ItemDescription('91', description='', group='CS-ATT|CS-PER|CS-INT'),
        ItemDescription('92', description='', group='CS-IMP|CS-SOC|CS-EXT'),
        ItemDescription('93', description='', group='CS-ATT|CS-PER|CS-INT'),
        ItemDescription('94', description='', group='CS-IMP|CS-SOC|CS-INT'),
        ItemDescription('95', description='', group='CS-ATT|CS-AO|CS-INT', reverse_scoring=True),
        ItemDescription('96', description='', group='CS-ATT|CS-SOC|CS-INT'),
        ItemDescription('97', description='', group='CS-HYP|CS-AO|CS-INT'),
        ItemDescription('98', description='', group='CS-ATT|CS-PER|CS-EXT'),
        ItemDescription('99', description='', group='CS-ATT|CS-SOC|CS-EXT'),
        ItemDescription('100', description='', group='CS-HYP|CS-AO|CS-EXT'),
        ItemDescription('101', description='', group='CS-HYP|CS-PER|CS-INT'),
        ItemDescription('102', description='', group='CS-HYP|CS-PER|CS-EXT'),
        ItemDescription('103', description='', group='CS-IMP|CS-SOC|CS-INT'),
        ItemDescription('104', description='', group='CS-HYP|CS-PER|CS-INT'),
        ItemDescription('105', description='', group='CS-ATT|CS-PER|CS-INT'),
        ItemDescription('106', description='', group='CS-IMP|CS-PER|CS-EXT'),
        ItemDescription('107', description='', group='CS-HYP|CS-PER|CS-EXT'),
        ItemDescription('108', description='', group='CS-ATT|CS-AO|CS-EXT'),
    ]

    results_order = [
        'CM-ATT',
        'CM-IMP',
        'CM-HYP',
        'Childhood Memories Clinical Index (CM CI)',
        'CM-PER',
        'CM-AO',
        'CM-SOC',
        'CM-INT',
        'CM-EXT',
        'CS-ATT',
        'CS-IMP',
        'CS-HYP',
        'Current Symptoms Clinical Index (CS CI)',
        'CS-PER',
        'CS-AO',
        'CS-SOC',
        'CS-INT',
        'CS-EXT',
        'CAT-A Clinical Index',
        'Negative Impression',
        'Infrequency',
        'Positive Impression',
    ]

    def calculate_negative_score(self, test):
        # We need to reverse the ones that need to be reversed, so first pull
        # all possible ones from DB
        possible_significant_items = test.items.filter(Q(score=4) | Q(score=1))
        significant_items = [
            item for item in possible_significant_items
            if (item.reverse_scoring and self.reverse_score(item.score) == 4) or (not item.reverse_scoring and item.score == 4)
        ]

        negativity_score = len(significant_items)
        if negativity_score < 46:
            negativity_classification = "Typical"
        elif negativity_score < 78:
            negativity_classification = "Atypical"
        else:
            negativity_classification = "Very atypical"

        return f"{negativity_score} ({negativity_classification})"

    def calculate_infrequency_score(self, test):
        infrequency_item_numbers = (10, 27, 28, 58, 72, 77, 81, 83, 85, 92)
        # We need to reverse the ones that need to be reversed, so first pull
        # all possible ones from DB
        possible_significant_items = test.items.filter(Q(score=4) | Q(score=1), number__in=infrequency_item_numbers)
        significant_items = [
            item for item in possible_significant_items
            if (item.reverse_scoring and self.reverse_score(item.score) == 4) or (not item.reverse_scoring and item.score == 4)
        ]

        infrequency_score = len(significant_items)
        if infrequency_score < 4:
            infrequency_classification = "Typical"
        elif infrequency_score < 6:
            infrequency_classification = "Atypical"
        else:
            infrequency_classification = "Very atypical"

        return f"{infrequency_score} ({infrequency_classification})"

    def calculate_positive_score(self, test):
        # We need to reverse the ones that need to be reversed, so first pull
        # all possible ones from DB
        possible_significant_items = test.items.filter(Q(score=4) | Q(score=1))
        significant_items = [
            item for item in possible_significant_items
            if (item.reverse_scoring and self.reverse_score(item.score) == 1) or (not item.reverse_scoring and item.score == 1)
        ]

        positive_score = len(significant_items)

        if positive_score < 63:
            positive_classification = "Typical"
        elif positive_score < 80:
            positive_classification = "Atypical"
        else:
            positive_classification = "Very atypical"

        return f"{positive_score} ({positive_classification})"


    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['Childhood Memories Clinical Index (CM CI)'] = sum([
            value for key, value in raw_scores.items()
            if key in ['CM-ATT', 'CM-IMP', 'CM-HYP']
        ])
        raw_scores['Current Symptoms Clinical Index (CS CI)'] = sum([
            value for key, value in raw_scores.items()
            if key in ['CS-ATT', 'CS-IMP', 'CS-HYP']
        ])
        raw_scores['CAT-A Clinical Index'] = raw_scores['Childhood Memories Clinical Index (CM CI)'] + raw_scores["Current Symptoms Clinical Index (CS CI)"]
        raw_scores['Negative Impression'] = self.calculate_negative_score(test)
        raw_scores['Infrequency'] = self.calculate_infrequency_score(test)
        raw_scores['Positive Impression'] = self.calculate_positive_score(test)

        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
