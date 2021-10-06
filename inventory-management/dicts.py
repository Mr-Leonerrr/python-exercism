from typing import Counter


def create_inventory(items: list) -> dict:
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """

    return Counter(items)


def add_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """

    inventory = Counter(inventory)
    inventory.update(items)

    return inventory


def decrement_items(inventory: dict, items: list) -> dict:
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for item in items:
        if inventory.get(item):
            inventory[item] -= 1

    return inventory


def remove_item(inventory: dict, item: str) -> dict:
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """

    if item in inventory:
        del inventory[item]

    return inventory


def list_inventory(inventory: dict) -> "list[tuple]":
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(item, count) for item, count in inventory.items() if count > 0]
