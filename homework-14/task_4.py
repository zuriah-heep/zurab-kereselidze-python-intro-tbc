import timeit

def chunk_data(data, chunk_size):
    return (tuple(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size))

def chunk_data_1(data, chunk_size):
    yield from (tuple(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size))

def chunk_data_2(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield tuple(data[i:i + chunk_size])

def main():
    data = (10, -2, '', 'word', 35)
    chunk_size = 3
    print('Data:', data)
    print('Chunk size:', chunk_size)
    print('Chunks:')
    for chunk in chunk_data_2(data, chunk_size):
        print(chunk)
    print()

    data = [1, 2, 3, 4, 5, 6, 7, 8]
    chunk_size = 3
    print('Data:', data)
    print('Chunk size:', chunk_size)
    print('Chunks:')
    for chunk in chunk_data(data, chunk_size):
        print(chunk)
    print()


    def method_1():
        for _ in chunk_data(data, chunk_size):
            continue
    def method_2():
        for _ in chunk_data(data, chunk_size):
            continue
    def method_3():
        for _ in chunk_data_2(data, chunk_size):
            continue

    print("Time for method 1 executed 100000 times:", timeit.timeit(method_1, number=100000))
    print("Time for method 2 executed 100000 times:", timeit.timeit(method_2, number=100000))
    print("Time for method 3 executed 100000 times:", timeit.timeit(method_3, number=100000))
    print()

    print('Method 1 output type:', type(chunk_data(data, chunk_size)))
    print('Method 2 output type:', type(chunk_data_1(data, chunk_size)))
    print('Method 3 output type:', type(chunk_data_2(data, chunk_size)))

if __name__ == "__main__":
    main()