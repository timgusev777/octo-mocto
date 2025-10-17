import unittest

def gen_bin_tree(height=4, root=4):
    if height == 1:
        return {'root': root}
    return {
        'root': root,
        'left': gen_bin_tree(height - 1, root * 4),
        'right': gen_bin_tree(height - 1, root + 1)
    }

class TestMath(unittest.TestCase):

    def test_height_1(self):
        self.assertEqual(gen_bin_tree(height = 1, root = 5), {'root': 5})

    def test_height_2(self):
        self.assertEqual(gen_bin_tree(height = 2, root = 3), {
                'root': 3,
                'left': {'root': 12},
                'right': {'root': 4}
            }
        )

unittest.main(argv=[''], verbosity=2, exit=False)
