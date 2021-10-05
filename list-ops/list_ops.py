def append(list1, list2):
    return list1 + list2


def concat(lists):
    return sum(lists, [])


def filter(function, list):
    return [data for data in list if function(data)]


def length(list):
    return len(list)


def map(function, list):
    return [function(data) for data in list]


def foldl(function, list, initial):
    value = initial
    for data in list:
        value = function(value, data)

    return value


def foldr(function, list, initial):
    value = initial

    for data in list[::-1]:
        value = function(data, value)

    return value


def reverse(list):
    return list[::-1]
