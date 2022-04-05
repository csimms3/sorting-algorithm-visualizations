import random


# (range(min, max), how many) to sort x numbers : (0, x), x)
list1 = random.sample(range(0, 20), 20)

a = 0  # intermediate variable for swap

sortingForwards = True
ActionsThisCycle = 1

print("STARTING CONFIGURATION :")
print(list1)

def forwardsort():
    n = 0
    iteration = 0
    ActionsThisCycle = 0
    InactionForward = True

    while n < (len(list1) - 1):

        if list1[n] > list1[n + 1]:
            a = list1[n]
            list1[n] = list1[n + 1]
            list1[n + 1] = a

            iteration += 1
            ActionsThisCycle += 1
            n += 1
            InactionForward = False

            print(str(list1[:n]) + " " + str(list1[n]) + " " + str(list1[n + 1:]) + "Swaps : " + str(
                ActionsThisCycle - 1), "Iteration : " + str(iteration) + " fwd")

        else:
            iteration += 1
            n += 1

    sortingForwards = False

    if InactionForward == True:
        ActionsThisCycle = 0


def reversesort():

    n = (len(list1) - 1)
    iteration = 0
    ActionsThisCycle = 0
    InactionReverse = True

    while n >= 1:
        if list1[n] < list1[n - 1]:
            a = list1[n]
            list1[n] = list1[n - 1]
            list1[n - 1] = a

            iteration += 1
            ActionsThisCycle += 1
            n -= 1
            InactionReverse = False

            print(str(list1[:n]) + " " + str(list1[n]) + " " + str(list1[n + 1:]) + "Swaps : " + str(
                ActionsThisCycle - 1), "Iteration : " + str(iteration) + " bckwd")

        else:
            iteration += 1
            n -= 1

    sortingForwards = True

    if InactionReverse == True:
        ActionsThisCycle = 0


while ActionsThisCycle > 0:

    if sortingForwards == True:
        reversesort()


    else: forwardsort()



