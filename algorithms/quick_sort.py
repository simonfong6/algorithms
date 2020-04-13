"""Quick Sort

Partition array around a pivot.
"""

array_state = "{array}"

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, start, end):
    i = start
    j = end

    p = (start + end) // 2

    pivot = array[p]

    if not j > i:
        return

    # Right side with will be >= pivot.
    while j > i:
        while array[i] < pivot:
            i += 1

            if not j > i:
                break

        if not j > i:
                break

        while array[j] >= pivot:
            j -= 1
            if not j > i:
                break

        if not j > i:
                break
        swap(array, i, j)

        print(array, i, j, pivot)

    print(array, i, j, pivot)

    partition_index = i

    partition(array, start, partition_index - 1)
    partition(array, partition_index, end)
    


def quick_sort(array):
    # Partition
    length = len(array)

    start = 0
    end = length - 1

    mid = partition(array, start, end)



    # Partition Left
    # Partition Right

    return array



def main():
    import random

    nums = list(range(7))
    random.shuffle(nums)

    print("Unsorted")
    print(nums)

    print("Quick Sort")
    quick_sort(nums)

    print("Sorted")
    print(nums)


if __name__ == '__main__':
    main()
