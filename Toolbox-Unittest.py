#Toolbox unittesting

import unittest

random_list = [5, 6, 15, -3, 7, -14, 8, 14, -1]

def sort_and_remove_negs(random_list):
    """script to sort a list and remove negative numbers"""
    sorted_list = sorted(random_list)
    sorted_pos_list = []
    for item in sorted_list:
        if item >= 0:
            sorted_pos_list.append(item)
    return sorted_pos_list


class SortRemoveNegs(unittest.TestCase):
    def setUp(self):
        self.random_list = [5, 6, 15, -3, 7, -14, 8, 14, -1]
        self.sorted_list = sort_and_remove_negs(self.random_list)

    def test_sorted(self):
        for i in range(len(self.sorted_list)-1):
            self.assertTrue(self.sorted_list[i] <= self.sorted_list[i+1])

    def test_pos(self):
        for element in self.sorted_list:
            self.assertTrue(element >= 0)

if __name__ == '__main__':
    unittest.main()
