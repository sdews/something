def binary_search(item_list, item_to_search):
    low_ind = 0
    high_ind = len(item_list) - 1

    SEARCH_COUNT = 0

    while low_ind <= high_ind:
        SEARCH_COUNT += 1
        print("binary_search SEARCH_COUNT: %d" % SEARCH_COUNT)

        mid_ind = int((low_ind + high_ind) / 2)
        if item_list[mid_ind] == item_to_search:
            return mid_ind
        elif item_list[mid_ind] < item_to_search:
            low_ind = mid_ind + 1
        else:
            high_ind = mid_ind - 1

    return None


def interpolation_search(item_list, item_to_search):
    low = 0
    high = len(item_list) - 1

    SEARCH_COUNT = 0

    while low <= high:
        SEARCH_COUNT += 1
        print("interpolation_search SEARCH_COUNT: %d" % SEARCH_COUNT)

        mid = low + int(float((high - low) / (item_list[high] - item_list[low])) * (item_to_search - item_list[low]))
        if item_list[mid] == item_to_search:
            return mid
        elif item_list[mid] < item_to_search:
            low = mid + 1
        else:
            high = mid - 1

    return None


def bubble_sort(item_list):
    length = len(item_list)

    # loop through all numbers, 共需要遍历 length - 1 次
    # 遍历第1次 第一大的元素放到了尾部
    # 遍历第2次 第二大的元素放到了倒数第二的位置
    # ......
    for i in range(length - 1):
        swapped = False

        # 遍历剩前面剩下的元素, 共需要遍历 length - 1 - i 次
        for j in range(length - 1 - i):
            to_print = "     Items compared: [ %d, %d ] " % (item_list[j], item_list[j + 1])

            if item_list[j] > item_list[j + 1]:
                temp = item_list[j]
                item_list[j] = item_list[j + 1]
                item_list[j + 1] = temp
                swapped = True
                to_print += " => swapped [%d, %d]\n" % (item_list[j], item_list[j + 1])
            else:
                to_print += " => not swapped\n"

            print(to_print)

        # if no number was swapped that means array is sorted now, break the loop.
        if not swapped:
            break

        print("Iteration {}#: {}\n" .format(i + 1, item_list))

    return item_list


def quick_sort(item_list):
    if len(item_list) == 0:
        return []

    pivlot = item_list[0]
    left = []
    right = []
    for item in item_list[1:]:
        if item < pivlot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort(left) + [pivlot] + quick_sort(right)


if __name__ == '__main__':
    # print(binary_search([10, 14, 19, 26, 27, 31, 33, 35, 42, 44], 33))
    # print(interpolation_search([10, 14, 19, 26, 27, 31, 33, 35, 42, 44], 33))

    # print(bubble_sort([1, 8, 4, 6, 0, 3, 5, 2, 7, 9]))
    # aa = quick_sort([7, 3, 1, 20, 5, 13])
    # print(aa)
    pass
