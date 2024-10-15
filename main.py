import time
import random


def is_sorted(lst:list) -> bool:
    """Checks to see if a list is sorted or not
    takes a list and returns a bool
    """
    first = lst[0]
    for i in lst[1:]:
        if type(first) is not int:
            raise TypeError
        if first > i:
            return False
        first = i
    else:
        if lst == sorted(lst):
            return True
        else:
            return False
        
def quicksort(lst, low_index = 0, high_index = None) -> tuple[list, int, int]:
    def _partition(lst, low, high) -> tuple[int, int, int]:
        pivot = lst[high] # Putting the pivot at the end so I only sort one side
        small_index = low-1
        comparisons_p = 0
        swaps_p = 0
        # Loops through the list section and swaps items so all items to the right of pivot are smaller
        for i in range(low, high):
            if lst[i] <= pivot:
                small_index += 1
                comparisons_p += 1
                swaps_p += 1
                lst[small_index], lst[i] = lst[i], lst[small_index]
        swaps_p += 1
        lst[small_index+1], lst[high] = lst[high], lst[small_index+1]
        
        return small_index + 1, comparisons_p, swaps_p
    
    comparisons = 0
    swaps = 0
    if high_index is None:
        high_index = len(lst) - 1
    # run until low index and high index overlap
    if low_index < high_index:
        pivot, comps, swap = _partition(lst, low_index, high_index)
        comparisons += comps
        swaps += swap
        resulting = quicksort(lst, low_index, pivot-1)
        comparisons += resulting[1]
        swaps += resulting[2]
        resulting, quicksort(lst, pivot+1, high_index)
        comparisons += resulting[1]
        swaps += resulting[2]
    return (lst, comparisons, swaps)

def selection_sort(lst):
    comparisons = 0
    swaps = 0
    for full_index in range(len(lst)-1):
        index_smallest = full_index+1
        for index, value in enumerate(lst[full_index:]):
            comparisons += 1
            if value < lst[index_smallest]:
                index_smallest = index+full_index
        swaps += 1
        lst[index_smallest], lst[full_index] = lst[full_index], lst[index_smallest]
    return (lst, comparisons, swaps)

def insertion_sort(lst:list):   
    comparisons = 0
    swaps = 0
    for main_index, main_value in enumerate(lst[1:]):
        index = 0
        while main_value > lst[index]:
            comparisons += 1
            index+=1
        swaps += 1
        popped = lst.pop(main_index+1)
        lst.insert(index, popped)
    return (lst, comparisons, swaps)

def mergesort(lst:list) -> tuple[list, int, int]:
    def merge(ls:list[int], rs:list[int]) -> list[int]:
        """Merge the two arrays while sorting them

        Args:
            ls (list[int]): left side
            rs (list[int]): right side

        Returns:
            list[int]: the sorted list
        """
        sorted = []
        i = 0
        j = 0
        comparisons_m = 0
        swaps_m = 0
        while i<len(ls) and j<len(rs):
            if ls[i] < rs[j]:
                comparisons_m += 1
                swaps_m += 1
                sorted.append(ls[i])
                i += 1
            else:
                comparisons_m += 1
                swaps_m += 1
                sorted.append(rs[j])
                j += 1
        if i < len(ls):
            sorted.extend(ls[i:])
        
        if j < len(rs):
            sorted.extend(rs[j:])
            
        return sorted, comparisons_m, swaps_m
            
        
    comparisons = 0
    swaps = 0
    if len(lst) <= 1:
        return (lst, 0, 0)

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    
    sorted_left = mergesort(left)
    comparisons += sorted_left[1]
    swaps += sorted_left[2]
    sorted_right = mergesort(right)
    comparisons += sorted_right[1]
    swaps += sorted_right[2]
    
    final, comps, swap = merge(sorted_left[0], sorted_right[0])
    
    comparisons += comps
    swaps += swap
    
    return (final, comparisons, swaps)
    
    

def main():
    input_list = [random.randrange(-100,100) for _ in range(random.randint(5,500))]
    def gather_input(name, function):
        beginning_time = time.time()
        result = function(input_list.copy())
        end_time = time.time()
        print_result(name, result[0], result[1], result[2], end_time-beginning_time)
        
    def print_result(name:str, lst, comparisons, swaps, time):
        if is_sorted(lst):
            print(f"{name} Completed!\n\
                Comparisons: {comparisons}\n\
                Swaps: {swaps}\n\
                Time: {round((time), 5)} seconds\n\
                ")
            return True
        else:
            print(f"{name.upper()} FAILED IN {round(time,5)} SECONDS")
            return False
    
    assert is_sorted([1,2,5,9,15])
    assert not is_sorted([1, 2, 5, 9, 8])
    print("Starting the sorting benchmarks\n\n")
    gather_input("QuickSort", quicksort)
    gather_input("MergeSort", mergesort)
    gather_input("Selection Sort", selection_sort)
    gather_input("Insertion Sort", insertion_sort)
    

if __name__ == "__main__":
    main()