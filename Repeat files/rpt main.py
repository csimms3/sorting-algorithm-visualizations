import random
from BubbleSort_simple_rpt import bubblesortsimple
from BubbleSort_v5_rpt import bubblesortfast
from InsertionSort_v2_rpt import insertionsort
from MergeSort_v2_rpt import mergeSortMain
from QuickSort_v1_rpt import quickSortMain
from RadixSort_v1_rpt import radixsort
from SelectionSort_v1_rpt import selectionsort
from HeapSort_v1_rpt import heapSort
from BubbleSort_optimized import bubblesortoptimized

print("Options:\n"
      "1: Bubblesort (slow)\n"
      "2: Bubblesort (fast)\n"
      "3: Insertionsort\n"
      "4: Mergesort\n"
      "5: Quicksort\n"
      "6: Radixsort\n"
      "7: Selectionsort\n"
      "8: Heapsort\n"
      "9: Bubblesort (best)")

chosenalgorithm = int(input("Algorithm Choice (Number from above): "))
repitiions = int(input("# of runs: "))
sample_size = int(input("Sample size to be sorted: "))
show_full_list = input("Show entire list while sorting? (y/n): ")

algorithms = {1: bubblesortsimple,
              2: bubblesortfast,
              3: insertionsort,
              4: mergeSortMain,
              5: quickSortMain,
              6: radixsort,
              7: selectionsort,
              8: heapSort,
              9: bubblesortoptimized}


def printfunc(opt, list):
    if opt == "y":
        print(list)

    else:
        print(f"{list[0], list[1], list[2], list[3]} ... {list[-4], list[-3], list[-2], list[-1]}")


def main(algo, reps, sample):
    timearr = []

    for i in range(0, reps):
        list1 = random.sample(range(0, sample), sample)

        print(f"Trial {i + 1}")
        printfunc(show_full_list, list1)

        timearr.append(algorithms[algo](list1))

        printfunc(show_full_list, list1)
        print(f"Trial {i + 1}, {timearr[i]} seconds")
        print("--------------------------")

    print(f"Results for {algorithms[algo].__name__}:")
    print("--------------------------")
    for i in timearr:
        print(i)
    print("--------------------------")

    total = 0
    for i, value in enumerate(timearr):
        total += value

    average = round(total / len(timearr), 4)
    worsttime = max(timearr)
    besttime = min(timearr)

    print(f"Average: {average}")
    print(f"Best time: {besttime}")
    print(f"Worst time: {worsttime}")
    print(f"Total Runtime: {round(total, 4)}")


main(chosenalgorithm, repitiions, sample_size)
