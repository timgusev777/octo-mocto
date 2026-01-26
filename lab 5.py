def gen_bin_tree(height=4, root=4, left_branch=lambda l: l * 4, right_branch=lambda r: r + 1):
    '''строим бинарное дерево заданной высоты нерекурсивным способом'''

    tree = {root: {}}
    '''проверка значения высоты'''
    if height == 0:
        return tree
    if height < 0:
        return "значение не должно быть отрицательным"

    '''создаем уровни дерева'''
    levels = [[root]]

    '''проходим по уровням и задаем для каждого следующий уровень'''
    for current_height in range(1, height):
        prev_level = levels[-1]
        new_level = []
        for val in prev_level:
            new_level.append(left_branch(val))
            new_level.append(right_branch(val))
        levels.append(new_level)

    '''создаем словарь для узлов в дереве, словарь содержит поддерево'''
    val_node = {}

    for value in levels[-1]:
        val_node[value] = {}

    '''идем снизу вверх, начиная с предпоследнего уровня. для каждого узла записываем его листья'''
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
