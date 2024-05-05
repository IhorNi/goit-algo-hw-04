import timeit
import random
from custom_sorting import merge_sort, insertion_sort


def test_algorithm(algorithm, data):
    return round(timeit.timeit(lambda: algorithm(data.copy()), number=1), 6)


def main():
    sizes = [100, 1000, 5000, 10000, 25000, 50000]
    datasets = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}
    
    print(f"{'Size':<10}{'Merge Sort':<20}{'Insertion Sort':<20}{'Timsort (sorted)':<20}")
    print("-" * 70)
    
    for size, data in datasets.items():
        merge_sort_time = test_algorithm(merge_sort, data)
        insertion_sort_time = test_algorithm(insertion_sort, data)
        timsort_time = test_algorithm(sorted, data)
        print(f"{size:<10}{merge_sort_time:<20}{insertion_sort_time:<20}{timsort_time:<20}")


if __name__ == '__main__':
    main()
