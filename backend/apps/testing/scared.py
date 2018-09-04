from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


scared_items = [
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


scared_results_order = [
    'Panic/Somatic',
    'Generalized Anxiety',
    'Separation',
    'Social',
    'School Avoidance',
    'Total',
]


def create_scared_test_items(test_id):
    create_test_items(test_id, scared_items)


def calculate_scared_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['Total'] = sum([value for key, value in raw_scores.items() if key in scared_results_order])
    return_obj = convert_to_return_value(raw_scores, scared_results_order, test)
    return return_obj
