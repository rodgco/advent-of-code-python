def all_equal(arr):
    return len(set(arr)) == 1


def join_to_string(arr):
    return int("".join([str(i) for i in arr]))
