import random

#### reverse sort


# (range(min, max), how many #)
list1 = random.sample(range(0, 100), 100)

a = 0  # intermediate variable for swap
n = 0  # current list index being checked
ActionsThisCycle = 1  # when 0 after full sweep === end
iteration = 0

print("STARTING CONFIGURATION :")
print(list1)

while ActionsThisCycle > 0:
    n = (len(list1) - 1)
    ActionsThisCycle = 1
    Inaction = True  ## checks to see if at least one swap occurred (not sorted)

    while n > 0:
        if list1[n] < list1[n - 1]:
            a = list1[n]
            list1[n] = list1[n - 1]
            list1[n - 1] = a

            iteration = iteration + 1
            ActionsThisCycle = ActionsThisCycle + 1
            n = n - 1
            Inaction = False

            print(str(list1[:n]) + " " + str(list1[n]) + " " + str(list1[n + 1:]) + "Swaps : " + str(
                ActionsThisCycle - 1), "Iteration : " + str(iteration))


        else:
            iteration = iteration + 1
            n = n - 1

    if Inaction == True:
        ActionsThisCycle = 0
