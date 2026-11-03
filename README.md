# Judo Training Fee Calculator (Python)

A console program for a judo club that works out an athlete's monthly fees. It uses a
training plan, private coaching hours and competition entries, and shows the athlete's
weight category.

## Pricing
| Item | Price |
|---|---|
| Beginner plan (2 sessions a week) | £25 a week (£100 a month) |
| Intermediate plan (3 sessions a week) | £30 a week (£120 a month) |
| Elite plan (5 sessions a week) | £35 a week (£140 a month) |
| Private coaching | £9.50 an hour, up to 20 hours a month |
| Competition entry | £22 each (not available on the beginner plan) |

## Weight categories
| Category | Limit |
|---|---|
| Flyweight | up to 66 kg |
| Lightweight | up to 73 kg |
| Light-Middleweight | up to 81 kg |
| Middleweight | up to 90 kg |
| Light-Heavyweight | up to 100 kg |
| Heavyweight | over 100 kg |

## Features
- Choose a training plan, then calculate the monthly training fee
- Add private coaching hours (capped at 20 a month)
- Add competition entries for intermediate and elite athletes
- Show the athlete's weight category

## How to run
1. Install Python 3.
2. Run `python judo_calculator.py` in a terminal.
3. Choose option 1 to calculate fees, or option 2 to exit.

## Example
A beginner with 5 private coaching hours and no competitions:
- Training fee: £100.00
- Private coaching: £47.50
- Total: £147.50

## What I'd improve next
- Check that the user types a number for weight, hours and competitions, so the program doesn't crash
- Remove the weight-limit warning, since the category is calculated from the same weight and the warning can never trigger
- Store the plan prices in a dictionary, so the code doesn't repeat the same checks
