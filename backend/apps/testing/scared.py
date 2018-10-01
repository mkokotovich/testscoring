from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class SCARED(BaseAssessment):
    test_type = Test.SCARED

    items = [
        ItemDescription('1', description='', group='Panic/Somatic'),
        ItemDescription('2', description='', group='School Avoidance'),
        ItemDescription('3', description='', group='Social'),
        ItemDescription('4', description='', group='Separation'),
        ItemDescription('5', description='', group='Generalized Anxiety'),
        ItemDescription('6', description='', group='Panic/Somatic'),
        ItemDescription('7', description='', group='Generalized Anxiety'),
        ItemDescription('8', description='', group='Separation'),
        ItemDescription('9', description='', group='Panic/Somatic'),
        ItemDescription('10', description='', group='Social'),
        ItemDescription('11', description='', group='School Avoidance'),
        ItemDescription('12', description='', group='Panic/Somatic'),
        ItemDescription('13', description='', group='Separation'),
        ItemDescription('14', description='', group='Generalized Anxiety'),
        ItemDescription('15', description='', group='Panic/Somatic'),
        ItemDescription('16', description='', group='Separation'),
        ItemDescription('17', description='', group='School Avoidance'),
        ItemDescription('18', description='', group='Panic/Somatic'),
        ItemDescription('19', description='', group='Panic/Somatic'),
        ItemDescription('20', description='', group='Separation'),
        ItemDescription('21', description='', group='Generalized Anxiety'),
        ItemDescription('22', description='', group='Panic/Somatic'),
        ItemDescription('23', description='', group='Generalized Anxiety'),
        ItemDescription('24', description='', group='Panic/Somatic'),
        ItemDescription('25', description='', group='Separation'),
        ItemDescription('26', description='', group='Social'),
        ItemDescription('27', description='', group='Panic/Somatic'),
        ItemDescription('28', description='', group='Generalized Anxiety'),
        ItemDescription('29', description='', group='Separation'),
        ItemDescription('30', description='', group='Panic/Somatic'),
        ItemDescription('31', description='', group='Separation'),
        ItemDescription('32', description='', group='Social'),
        ItemDescription('33', description='', group='Generalized Anxiety'),
        ItemDescription('34', description='', group='Panic/Somatic'),
        ItemDescription('35', description='', group='Generalized Anxiety'),
        ItemDescription('36', description='', group='School Avoidance'),
        ItemDescription('37', description='', group='Generalized Anxiety'),
        ItemDescription('38', description='', group='Panic/Somatic'),
        ItemDescription('39', description='', group='Social'),
        ItemDescription('40', description='', group='Social'),
        ItemDescription('41', description='', group='Social'),
    ]

    results_order = [
        'Total',
        'Panic/Somatic',
        'Generalized Anxiety',
        'Separation',
        'Social',
        'School Avoidance',
    ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        raw_scores['Total'] = sum([value for key, value in raw_scores.items() if key in self.results_order])
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
