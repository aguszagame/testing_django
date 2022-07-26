
import unittest
from unittest import mock 


from l1_calculator.services import parse_number, parse_operator, parse_elements

class ServicesTestCases(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    
    def test_parse_number_int(self):
        actual = parse_number('3')
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_parse_number_float(self):
        actual = parse_number('3.9')
        expected = 3.9
        self.assertEqual(actual, expected)
            
       
    def test_parse_number_type_error(self):
        actual = parse_number(None)
        expected = None
        self.assertEqual(actual, expected)
        
    def test_parse_number_value_error(self):
        actual = parse_number('abc')
        expected = None
        self.assertEqual(actual, expected)    
        
            
    def test_parse_operator(self):
        actual = parse_operator('+')
        expected = '+'
        self.assertEqual(actual, expected) 
    
    def test_parse_operator_not_string(self):
        actual = parse_operator(3)
        expected = None
        self.assertEqual(actual, expected) 
    
    def test_parse_operator_str_err(self):
        actual = parse_operator('%')        
        self.assertIsNone(actual) 
        
    def test_parse_elements_integrations(self):
       first, operator, second = parse_elements('3', '- ', '2')
       self.assertEqual(first, 3)
       self.assertEqual(operator, '-' )
       self.assertEqual(second, 2 )
       
#con mocks porque simulan cualquier ocsa.
# con un decorador le pasamos al mock lo que queremos que imite y lo que esperamos que devuelva

    @mock.patch('l1_calculator.services.parse_operator')
    @mock.patch('l1_calculator.services.parse_number')
    def test_parse_elements_unit(self, mock_parse_number, mock_parse_operator):
        arg_number = '3'
        arg_operator = '+ '
       
        
        mock_parse_number.return_value = 3
        mock_parse_operator.return_value = '+'
        
        first, operator, second = parse_elements(arg_number, arg_operator, arg_number)
        
        self.assertEqual(first, 3)
        self.assertEqual(second, 3)
        self.assertEqual(operator, '+')
        
        self.assertEqual(mock_parse_number.call_count, 2)
        mock_parse_number.assert_called_with(arg_number)
        
        mock_parse_operator.assert_called_once_with(arg_operator)
        
    