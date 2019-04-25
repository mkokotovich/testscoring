from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class CDI2Self(BaseAssessment):
    test_type = Test.CDI2_SELF

    # These are in a strange order to match how the test looks
    items = [
        ItemDescription('1', description='', group='A'),
        ItemDescription('2', description='', group='B'),
        ItemDescription('3', description='', group='C'),
        ItemDescription('4', description='', group='C'),
        ItemDescription('5', description='', group='D'),
        ItemDescription('20', description='', group='C'),
        ItemDescription('21', description='', group='D'),
        ItemDescription('22', description='', group='C'),
        ItemDescription('23', description='', group='C'),
        ItemDescription('24', description='', group='B'),
        ItemDescription('25', description='', group='D'),
        ItemDescription('26', description='', group='A'),
        ItemDescription('27', description='', group='A'),
        ItemDescription('28', description='', group='C'),
        ItemDescription('6', description='', group='B'),
        ItemDescription('7', description='', group='B'),
        ItemDescription('8', description='', group='B'),
        ItemDescription('9', description='', group='A'),
        ItemDescription('10', description='', group='A'),
        ItemDescription('11', description='', group='D'),
        ItemDescription('12', description='', group='C'),
        ItemDescription('13', description='', group='B'),
        ItemDescription('14', description='', group='C'),
        ItemDescription('15', description='', group='A'),
        ItemDescription('16', description='', group='A'),
        ItemDescription('17', description='', group='A'),
        ItemDescription('18', description='', group='A'),
        ItemDescription('19', description='', group='D'),
    ]

    results_order = [
        'A',
        'B',
        'C',
        'D',
        'Negative Mood/Physical Symptoms (A)',
        'Negative Self-Esteem (B)',
        'Ineffectiveness (C)',
        'Interpersonal Problems (D)',
        'Emotional Problems',
        'Functional Problems',
        'Total',
    ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)

        raw_scores['Negative Mood/Physical Symptoms (A)'] = raw_scores['A']
        raw_scores['Negative Self-Esteem (B)'] = raw_scores['B']
        raw_scores['Ineffectiveness (C)'] = raw_scores['C']
        raw_scores['Interpersonal Problems (D)'] = raw_scores['D']
        raw_scores['Emotional Problems'] = raw_scores['A'] + raw_scores['B']
        raw_scores['Functional Problems'] = raw_scores['C'] + raw_scores['D']
        raw_scores['Total'] = raw_scores['A'] + raw_scores['B'] + raw_scores['C'] + raw_scores['D']

        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj
