import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import judo_calculator as calculator


class CalculatorTests(unittest.TestCase):
    def test_monthly_plan_prices_and_invalid_plan(self):
        self.assertEqual([calculator.get_training_fee(p) for p in ('1', '2', '3')], [100, 120, 140])
        with self.assertRaises(ValueError):
            calculator.get_training_fee('4')

    def test_weight_category_boundaries(self):
        cases = [(66, 'Flyweight'), (66.1, 'Lightweight'), (73, 'Lightweight'),
                 (81, 'Light-Middleweight'), (90, 'Middleweight'),
                 (100, 'Light-Heavyweight'), (100.1, 'Heavyweight')]
        for value, expected in cases:
            with self.subTest(weight=value):
                self.assertEqual(calculator.get_weight_category(value), expected)

    @patch('builtins.print')
    def test_weight_reprompts_for_text_negative_zero_and_nonfinite(self, _):
        with patch('builtins.input', side_effect=['abc', '-4', '0', 'nan', 'inf', '72.5']):
            self.assertEqual(calculator.read_number('Weight: ', exclusive_min=True), 72.5)

    @patch('builtins.print')
    def test_competitions_require_nonnegative_integer(self, _):
        with patch('builtins.input', side_effect=['-1', '1.5', 'no', '0']):
            self.assertEqual(calculator.read_number('Entries: ', integer=True), 0)

    @patch('builtins.print')
    def test_coaching_rejects_invalid_values_and_accepts_fractional_hours(self, _):
        with patch('builtins.input', side_effect=['21', '-1', 'nan', 'inf', '2.5']):
            self.assertEqual(calculator.read_number('Hours: ', maximum=20), 2.5)

    def test_beginner_calculation_recovers_from_bad_plan(self):
        inputs = ['1', 'Demo Athlete', 'wrong', '1', '70', '5', '2']
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as output:
            calculator.main()
        printed = '\n'.join(str(call.args[0]) for call in output.call_args_list if call.args)
        self.assertIn('Total Monthly Fee: £147.50', printed)
        self.assertIn('Beginner athletes cannot enter competitions', printed)

    def test_intermediate_competition_and_fractional_coaching_total(self):
        inputs = ['1', 'Demo Athlete', '2', '85', '2', '2.5', '2']
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as output:
            calculator.main()
        printed = '\n'.join(str(call.args[0]) for call in output.call_args_list if call.args)
        self.assertIn('Total Monthly Fee: £187.75', printed)


if __name__ == '__main__':
    unittest.main()
