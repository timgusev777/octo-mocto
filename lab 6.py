import matplotlib.pyplot as plt
import timeit


def gen_bin_tree_rec(height=4, root=4):
    if height == 1:
        return {'root': root}
    return {
        'root': root,
        'left': gen_bin_tree_rec(height - 1, root * 4),
        'right': gen_bin_tree_rec(height - 1, root + 1)
    }

def gen_bin_tree_iter(height=4, root=4, left_branch=lambda l: l * 4, right_branch=lambda r: r + 1):

    tree = {root: {}}

    if height == 0:
        return tree
    if height < 0:
        return "значение не должно быть отрицательным"

    levels = [[root]]

    for current_height in range(1, height):
        prev_level = levels[-1]
        new_level = []
        for val in prev_level:
            new_level.append(left_branch(val))
            new_level.append(right_branch(val))
        levels.append(new_level)


    val_node = {}

    for value in levels[-1]:
        val_node[value] = {}


    for level_val in range(len(levels) - 2, -1, -1):
        current_level = levels[level_val]
        next_level = levels[level_val + 1]
        leaf_index = 0

        for val_value in current_level:
            left_leaf = next_level[leaf_index]
            right_leaf = next_level[leaf_index + 1]

            val_node[val_value] = {
                left_leaf: val_node[left_leaf],
                right_leaf: val_node[right_leaf]
            }

            leaf_index += 2

    root_value = levels[0][0]
    return {root_value: val_node[root_value]}

def measure_time(func, number=1):
    return timeit.timeit(func, number=number)
#####
rec_time = measure_time(gen_bin_tree_rec, number=1)

iter_time = measure_time(gen_bin_tree_iter, number=1)

print(rec_time, iter_time)

plt.figure(figsize=(10, 6))
plt.plot([4], [rec_time], marker='o', label='Рекурсивный', color='red')
plt.plot([4], [iter_time], marker='s', label='Итеративный', color='blue')
plt.ylabel('Время построения (сек)')
plt.xlabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()