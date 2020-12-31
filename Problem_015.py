import time
tri_numbers = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231]
store = dict()

start_time = time.time()

def add_to_store(num, level, count):
    if num not in store:
        store[num] = dict()
    store[num][level] = count


def get_store_count(num, level):
    sub_store = store.get(num, 0)
    if sub_store == 0:
        return 0
    return sub_store.get(level, 0)


def triangle_recur(num, level):
    if level == 0:
        return tri_numbers[num]

    count = get_store_count(num, level)
    if count != 0:
        return count

    for i in range(1, num + 1):
        count += triangle_recur(i, level - 1)
    add_to_store(num, level, count)
    return count


grid_size = 8
print(triangle_recur(grid_size + 1, grid_size - 2))
print("--- %s seconds ---" % (time.time() - start_time))