def gen_bin_tree(height=4, root=4):

    tree = {
        'root': root,
        'left': gen_bin_tree(height - 1, root * 4),
        'right': gen_bin_tree(height - 1, root + 1)
    }

    return tree
