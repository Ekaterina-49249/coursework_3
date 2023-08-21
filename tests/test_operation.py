import operation
import pytest


@pytest.mark.parametrize('input_from, input_to, result_from, result_to', [
    ("Счет 84163357546688983493",
     "Visa Platinum 8990922113665229",
     "Счет **3493",
     "Visa Platinum 8990 92** **** 5229"),
    (None,
     "Visa Platinum 8990922113665229",
     "Нет данных",
     "Visa Platinum 8990 92** **** 5229")])
def test_operation_mask(input_from, input_to, result_from, result_to):
    test_operation = operation.Operation("2019-08-26T10:50:58.294041",
                                         "",
                                         input_from,
                                         input_to,
                                         "",
                                         "")

    assert test_operation.get_from() == result_from
    assert test_operation.get_to() == result_to


@pytest.mark.parametrize('input_date, result',
                         [("2018-03-23T10:45:06.972075", "23.03.2018")])
def test_operation_date(input_date, result):
    test_operation = operation.Operation(input_date,
                                         "",
                                         "",
                                         "",
                                         "",
                                         "")

    assert test_operation.get_date() == result


@pytest.mark.parametrize('input_amount, input_currency, result', [("40701.91",
                                                                   "руб.",
                                                                   "40701.91 руб.")])
def test_operation_amount(input_amount, input_currency, result):
    test_operation = operation.Operation("2019-10-30T01:49:52.939296",
                                         "",
                                         "",
                                         "",
                                         input_amount,
                                         input_currency)

    assert test_operation.get_amount_str() == result
