import multiprocessing


def a():
    for i in range(1, 1001):
        print("+++", i)


def b():
    for i in range(1, 1001):
        print("---", i)


process1 = multiprocessing.Process(target=a)
process2 = multiprocessing.Process(target=b)

if __name__ == "__main__":
    process1.start()
    process2.start()

# look at the result it is amazing :)