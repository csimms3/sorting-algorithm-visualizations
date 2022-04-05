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
      "9: Bubblesort (best)\n")

chosenalgorithm = int(input("Algorithm Choice (Number from above): "))
repitiions = int(input("# of runs: "))
samples = list(map(int, input("Enter sample sizes to be sorted (space separated, no commas): ").split()))
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


# small line break
def sb():
    print("-----------------------")


# large line break
def lb():
    print("=======================")


def printfunc(opt, list):
    if opt == "y":
        print(list)

    else:
        print(f"{list[0], list[1], list[2], list[3]} ... {list[-4], list[-3], list[-2], list[-1]}")


def printsinglerun(list, i):
    total = 0

    sb()

    for j, val in enumerate(list[i]):
        print(val)
        total += val

    sb()

    average = round(total / len(list[i]), 4)
    worsttime = max(list[i])
    besttime = min(list[i])

    print(f"Average: {average}")
    print(f"Best time: {besttime}")
    print(f"Worst time: {worsttime}")
    print(f"Total Runtime: {round(total, 4)}")


def main(algo, reps, sample_array):
    timearr2d = []

    # loop for each sample size given
    for i, val in enumerate(sample_array):
        run_index = i
        sample_size = val
        timearr = []

        lb()
        print(f"Run {run_index + 1} starting, Sample of {sample_size}")
        lb()

        # actual sorting run for x reps at a certain sample size
        for j in range(0, reps):
            list1 = random.sample(range(1, sample_size + 1), sample_size)

            print(f"Run {run_index + 1}, Sample: {sample_size}, Trial {j + 1}")
            printfunc(show_full_list, list1)

            timearr.append(algorithms[algo](list1))

            printfunc(show_full_list, list1)
            print(f"Trial {j + 1}, {timearr[j]} seconds")
            sb()

        timearr2d.append(timearr)

        # during run time print
        print(f"Run {i + 1} finished ({sample_size} samples). Results:")

        printsinglerun(timearr2d, i)

    # Results Print

    lb()
    print(f"Results for {algorithms[algo].__name__}:")
    lb()

    for i, arr in enumerate(timearr2d):
        sb()

        print(f"Run {i + 1}, Sample: {sample_array[i]}")

        printsinglerun(timearr2d, i)

    sb()

    hold = input("DONE")


main(chosenalgorithm, repitiions, samples)
