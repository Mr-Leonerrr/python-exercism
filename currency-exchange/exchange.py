def exchange_money(budget: float, exchange_rate: float) -> float:
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.

    Function that takes the amount of currency you want to exchange,
    the current unit value for the foreign currency (where
    exchange_rate in original currency = 1 unit for foreign currency),
    and return the value of the foreign currency you expect to receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: int) -> float:
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.

    This function should return the amount of money that is left from the budget.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.

    This function should return the total value of the given bills.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.

    This function should return the number of bills that you can get using the budget.
    """

    return budget // denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.

    This function should return the maximum value of
    the new currency after calculating the exchange rate plus the spread.
    Remember that the currency denomination is a whole number,
    and cannot be sub-divided.
    """

    exchange_value = exchange_money(
        budget, exchange_rate * (1.0 + spread / 100)
    )

    bills = get_number_of_bills(exchange_value, denomination)

    return get_value_of_bills(denomination, bills)


def non_exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.

    This function should return the value that
    is not exchangeable due to the denomination of the bills.
    """

    full_value = exchange_money(budget, exchange_rate * (1.0 + spread / 100))
    exchangeable = exchangeable_value(
        budget, exchange_rate, spread, denomination
    )

    return int(full_value - exchangeable)
