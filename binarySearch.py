import json, time

startTimeLinearSearch = time.time()
startTimeBinarySearch = time.time()

# loads a large dataset to make tests

fileDatasetName = "list.json"
searchIndexValue = 0

f = open(fileDatasetName)

fileData = json.load(f)
dataListToTest = fileData["metadata"]


def linearSearch(value, list):
    for index, val in enumerate(list):
        if value == val:
            print("--- %s seconds ---" % (time.time() - startTimeBinarySearch))
            return index
    print("--- %s seconds ---" % (time.time() - startTimeBinarySearch))
    return index


def binarySearch(searchItem, list):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2
        if list[mid] == searchItem:
            print("--- %s seconds ---" % (time.time() - startTimeLinearSearch))
            return mid
        else:
            if searchItem > list[mid]:
                low = mid + 1
            else:
                high = mid - 1
    print("--- %s seconds ---" % (time.time() - startTimeLinearSearch))
    return -1


size = len(dataListToTest)
print(f"List size: {size}")

# binarySearch(searchIndexValue, dataListToTest)
# linearSearch(searchIndexValue, dataListToTest)
