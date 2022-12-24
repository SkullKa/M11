import unittest

a = [4, 5, 6, 10, 1, 3]

# def bubble_sort(a):
#     n = len(a)
#     for i in range(n - 1):
#         for j in range(n - i- 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j +1] = a[j +1], a[j]
#     return a 

# print(a)
# print(bubble_sort(a))



def merge_sort(a):
    if len(a) < 2:
        return a[:]
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merg(left, right)

def merg(left, right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

print(merge_sort(a))




class TestSort(unittest.TestCase):

    def test1(self):
        b = [1, 4, 3, 6, 5]
        s = sorted(b)
        self.assertEqual(merge_sort(b), s)

    def test2(self):
        b = [-6, 0, -2, 1]
        s = sorted(b)
        self.assertEqual(merge_sort(b), s)


unittest.main()