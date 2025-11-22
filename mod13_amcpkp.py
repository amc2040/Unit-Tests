import unittest
from datetime import datetime


def validate_symbol(symbol):
    if not symbol:
        return False
    if not symbol.isalpha():
        return False
    if not symbol.isupper():
        return False
    if len(symbol) < 1 or len(symbol) > 7:
        return False
    return True


def validate_chart_type(chart_type):
    try:
        number = int(chart_type)
        if number == 1 or number == 2:
            return True
        else:
            return False
    except:
        return False


def validate_time_series(time_series):
    try:
        number = int(time_series)
        if number == 1 or number == 2 or number == 3 or number == 4:
            return True
        else:
            return False
    except:
        return False


def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except:
        return False


class TestStockSymbol(unittest.TestCase):
    
    def test_valid_symbols(self):
        self.assertTrue(validate_symbol('AAPL'))
        self.assertTrue(validate_symbol('GOOGL'))
        self.assertTrue(validate_symbol('MSFT'))
        self.assertTrue(validate_symbol('A'))
        self.assertTrue(validate_symbol('ABCDEFG'))
    
    def test_lowercase_rejected(self):
        self.assertFalse(validate_symbol('aapl'))
        self.assertFalse(validate_symbol('Aapl'))
        self.assertFalse(validate_symbol('AaPl'))
    
    def test_numbers_rejected(self):
        self.assertFalse(validate_symbol('AAPL1'))
        self.assertFalse(validate_symbol('123'))
        self.assertFalse(validate_symbol('A1B2'))
    
    def test_special_characters_rejected(self):
        self.assertFalse(validate_symbol('AAP$L'))
        self.assertFalse(validate_symbol('GO@GL'))
        self.assertFalse(validate_symbol('MSF-T'))
    
    def test_length_requirements(self):
        self.assertFalse(validate_symbol(''))
        self.assertTrue(validate_symbol('A'))
        self.assertTrue(validate_symbol('ABCDEFG'))
        self.assertFalse(validate_symbol('ABCDEFGH'))


class TestChartType(unittest.TestCase):
    
    def test_valid_chart_types(self):
        self.assertTrue(validate_chart_type(1))
        self.assertTrue(validate_chart_type(2))
        self.assertTrue(validate_chart_type('1'))
        self.assertTrue(validate_chart_type('2'))
    
    def test_invalid_numbers(self):
        self.assertFalse(validate_chart_type(0))
        self.assertFalse(validate_chart_type(3))
        self.assertFalse(validate_chart_type(10))
        self.assertFalse(validate_chart_type(-1))
    
    def test_non_numbers_rejected(self):
        self.assertFalse(validate_chart_type('bar'))
        self.assertFalse(validate_chart_type('line'))
        self.assertFalse(validate_chart_type('abc'))
        self.assertFalse(validate_chart_type(''))


class TestTimeSeries(unittest.TestCase):
    
    def test_valid_time_series(self):
        self.assertTrue(validate_time_series(1))
        self.assertTrue(validate_time_series(2))
        self.assertTrue(validate_time_series(3))
        self.assertTrue(validate_time_series(4))
        self.assertTrue(validate_time_series('1'))
        self.assertTrue(validate_time_series('2'))
        self.assertTrue(validate_time_series('3'))
        self.assertTrue(validate_time_series('4'))
    
    def test_invalid_numbers(self):
        self.assertFalse(validate_time_series(0))
        self.assertFalse(validate_time_series(5))
        self.assertFalse(validate_time_series(10))
        self.assertFalse(validate_time_series(-1))
    
    def test_non_numbers_rejected(self):
        self.assertFalse(validate_time_series('daily'))
        self.assertFalse(validate_time_series('weekly'))
        self.assertFalse(validate_time_series('abc'))
        self.assertFalse(validate_time_series(''))


class TestStartDate(unittest.TestCase):
    
    def test_valid_start_dates(self):
        self.assertTrue(validate_date('2025-11-21'))  
    
    def test_invalid_start_dates(self):
        self.assertFalse(validate_date('01-01-2024'))   
        self.assertFalse(validate_date('2024-13-01'))   
        self.assertFalse(validate_date(''))             


class TestEndDate(unittest.TestCase):
    
    def test_valid_end_dates(self):
        self.assertTrue(validate_date('2025-11-21'))  
    
    def test_invalid_end_dates(self):
        self.assertFalse(validate_date('2024/12/31'))  
        self.assertFalse(validate_date('2024-00-10'))   
        self.assertFalse(validate_date('2024-02-30'))   


if __name__ == '__main__':
    unittest.main()
