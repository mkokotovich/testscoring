from apps.testing.utils import ItemDescription, BaseAssessment
from apps.testing.models import Test


class ASRS_6_18(BaseAssessment):
    test_type = Test.ASRS_6_18

    items = [
        ItemDescription('1', description='', group='SR|AT'),
        ItemDescription('2', description='', group='UB|DSM|SS'),
        ItemDescription('3', description='', group='SC|PS'),
        ItemDescription('4', description='', group='SC|SER'),
        ItemDescription('5', description='', group='SR|AT'),
        ItemDescription('6', description='', group='SR'),
        ItemDescription('7', description='', group='SR'),
        ItemDescription('8', description='', group='SC|DSM|SER'),
        ItemDescription('9', description='', group='SC|DSM|SER'),
        ItemDescription('10', description='', group='AT'),
        ItemDescription('11', description='', group='DSM|SER'),
        ItemDescription('12', description='', group='SC'),
        ItemDescription('13', description='', group='UB|DSM|BR'),
        ItemDescription('14', description='', group='PS'),
        ItemDescription('15', description='', group='DSM|SER'),
        ItemDescription('16', description='', group='SR|AT'),
        ItemDescription('17', description='', group='UB|AL'),
        ItemDescription('18', description='', group='SR|AS'),
        ItemDescription('19', description='', group='DSM|PS'),
        ItemDescription('20', description='', group='UB|DSM|AL'),
        ItemDescription('21', description='', group='UB|DSM|AL'),
        ItemDescription('22', description='', group='UB|BR'),
        ItemDescription('23', description='', group='SC|DSM'),
        ItemDescription('24', description='', group='UB|DSM|BR'),
        ItemDescription('25', description='', group='UB|DSM|SS'),
        ItemDescription('26', description='', group='UB|DSM|AL'),
        ItemDescription('27', description='', group='UB|DSM|SS'),
        ItemDescription('28', description='', group='SC|DSM|SER'),
        ItemDescription('29', description='', group='UB|DSM|SS'),
        ItemDescription('30', description='', group='SR|AT'),
        ItemDescription('31', description='', group='SC|DSM|PS'),
        ItemDescription('32', description='', group='SC|DSM|SER'),
        ItemDescription('33', description='', group='SC|DSM|AS'),
        ItemDescription('34', description='', group='SR|AS'),
        ItemDescription('35', description='', group='SR|AT'),
        ItemDescription('36', description='', group='SR|AT'),
        ItemDescription('37', description='', group='DSM|AS'),
        ItemDescription('38', description='', group='UB|DSM|SS'),
        ItemDescription('39', description='', group='SC|DSM|SER'),
        ItemDescription('40', description='', group='UB|BR'),
        ItemDescription('41', description='', group='SER'),
        ItemDescription('42', description='', group='SC|DSM|SER'),
        ItemDescription('43', description='', group='SC|DSM|SER'),
        ItemDescription('44', description='', group='SR|AT'),
        ItemDescription('45', description='', group='SC|PS'),
        ItemDescription('46', description='', group='UB|DSM|ST'),
        ItemDescription('47', description='', group='AT'),
        ItemDescription('48', description='', group='UB|DSM|ST'),
        ItemDescription('49', description='', group='UB|DSM|BR'),
        ItemDescription('50', description='', group='UB|DSM|PS'),
        ItemDescription('51', description='', group='UB|DSM|BR'),
        ItemDescription('52', description='', group='SR|AT'),
        ItemDescription('53', description='', group='DSM|ST'),
        ItemDescription('54', description='', group='UB|DSM|ST'),
        ItemDescription('55', description='', group='SC|DSM|SER'),
        ItemDescription('56', description='', group='SC|DSM'),
        ItemDescription('57', description='', group='SR|AT'),
        ItemDescription('58', description='', group='SR|AL'),
        ItemDescription('59', description='', group='AS'),
        ItemDescription('60', description='', group='SR'),
        ItemDescription('61', description='', group='SC|DSM|SER'),
        ItemDescription('62', description='', group='UB|DSM|SS'),
        ItemDescription('63', description='', group='UB|DSM|BR'),
        ItemDescription('64', description='', group='PS'),
        ItemDescription('65', description='', group='UB|DSM|BR'),
        ItemDescription('66', description='', group='SR|AS'),
        ItemDescription('67', description='', group='UB|DSM|ST'),
        ItemDescription('68', description='', group='UB|AL'),
        ItemDescription('69', description='', group='SC|DSM|PS'),
        ItemDescription('70', description='', group='SC|DSM|PS'),
        ItemDescription('71', description='', group='SR'),
    ]

    results_order = [
        'SC',
        'UB',
        'SR',
        'DSM',
        'PS',
        'AS',
        'SER',
        'AL',
        'ST',
        'BR',
        'SS',
        'AT',
    ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj


class ASRS_2_5(BaseAssessment):
    test_type = Test.ASRS_2_5

    items = [
        ItemDescription('1', description='', group='SC|DSM|SER'),
        ItemDescription('2', description='', group='UB|DSM|SS'),
        ItemDescription('3', description='', group='SC|DSM|SER'),
        ItemDescription('4', description='', group='SC|DSM|PS'),
        ItemDescription('5', description='', group='SC|DSM|SER'),
        ItemDescription('6', description='', group='AL'),
        ItemDescription('7', description='', group='SC'),
        ItemDescription('8', description='', group='UB|DSM|BR'),
        ItemDescription('9', description='', group='UB|DSM|BR'),
        ItemDescription('10', description='', group='UB|DSM|BR'),
        ItemDescription('11', description='', group='UB|DSM|ST'),
        ItemDescription('12', description='', group='UB|DSM|SS'),
        ItemDescription('13', description='', group='SC|DSM|SER'),
        ItemDescription('14', description='', group='SC|DSM|SER'),
        ItemDescription('15', description='', group='SC|PS'),
        ItemDescription('16', description='', group='SC|DSM|SER'),
        ItemDescription('17', description='', group='SC|ASR'),
        ItemDescription('18', description='', group='SC|DSM'),
        ItemDescription('19', description='', group='SC|DSM|SER'),
        ItemDescription('20', description='', group='UB|DSM|BR'),
        ItemDescription('21', description='', group='SC|DSM|AS'),
        ItemDescription('22', description='', group='SC|AL'),
        ItemDescription('23', description='', group='AS'),
        ItemDescription('24', description='', group='SC|PS'),
        ItemDescription('25', description='', group='SC|ASR'),
        ItemDescription('26', description='', group='UB|DSM'),
        ItemDescription('27', description='', group='UB|BR'),
        ItemDescription('28', description='', group='SC|DSM'),
        ItemDescription('29', description='', group='SC|DSM'),
        ItemDescription('30', description='', group='SC|PS'),
        ItemDescription('31', description='', group='AS'),
        ItemDescription('32', description='', group='SC|ASR'),
        ItemDescription('33', description='', group='SC|AS'),
        ItemDescription('34', description='', group='ASR'),
        ItemDescription('35', description='', group='SC'),
        ItemDescription('36', description='', group='SC|SER'),
        ItemDescription('37', description='', group='SC|ASR'),
        ItemDescription('38', description='', group='SC|DSM|SER'),
        ItemDescription('39', description='', group='UB|DSM|ST'),
        ItemDescription('40', description='', group='SC|DSM|PS'),
        ItemDescription('41', description='', group='UB|DSM'),
        ItemDescription('42', description='', group='UB|DSM|AL'),
        ItemDescription('43', description='', group='SC|DSM|SER'),
        ItemDescription('44', description='', group='SC|AS'),
        ItemDescription('45', description='', group='UB|DSM|SS'),
        ItemDescription('46', description='', group='UB|DSM|SS'),
        ItemDescription('47', description='', group='UB|DSM|ST'),
        ItemDescription('48', description='', group='UB|DSM|BR'),
        ItemDescription('49', description='', group='SC|PS'),
        ItemDescription('50', description='', group='SC|DSM|SER'),
        ItemDescription('51', description='', group='SC|DSM|PS'),
        ItemDescription('52', description='', group='SC|PS'),
        ItemDescription('53', description='', group='UB|DSM|AL'),
        ItemDescription('54', description='', group='SC|DSM|SER'),
        ItemDescription('55', description='', group='SC|ASR'),
        ItemDescription('56', description='', group='UB|DSM|BR'),
        ItemDescription('57', description='', group='SC|ASR'),
        ItemDescription('58', description='', group='ASR'),
        ItemDescription('59', description='', group='AL'),
        ItemDescription('60', description='', group='UB|BR'),
        ItemDescription('61', description='', group='SC|DSM|PS'),
        ItemDescription('62', description='', group='SC|ASR'),
        ItemDescription('63', description='', group='SC|ASR'),
        ItemDescription('64', description='', group='UB|DSM|ST'),
        ItemDescription('65', description='', group='UB|DSM|ST'),
        ItemDescription('66', description='', group='DSM|SS'),
        ItemDescription('67', description='', group='SC'),
        ItemDescription('68', description='', group='ST'),
        ItemDescription('69', description='', group='UB|DSM|SS'),
        ItemDescription('70', description='', group='UB|DSM|AL'),
    ]

    results_order = [
        'SC',
        'UB',
        'DSM',
        'PS',
        'AS',
        'SER',
        'AL',
        'ST',
        'BR',
        'SS',
        'ASR',
    ]

    def score_test(self, test):
        raw_scores = self._calculate_raw_scores(test)
        return_obj = self._convert_to_return_value(raw_scores, self.results_order, test)
        return return_obj