Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12

def quarter_of(month):
    if month/12 <= 1/4:
        return 1
    if month/12 <= 1/2:
        return 2
    if month/12 <= 3/4:
        return 3
    else:
        return 4
