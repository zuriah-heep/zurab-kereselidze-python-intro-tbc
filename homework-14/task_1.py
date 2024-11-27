def main():
    temperature = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
    _sum = 0

    for i, day in enumerate(temperature, 1):
        _mean = sum(day) / len(day)
        _sum += _mean
        print(f'Day {i} temperatures:')
        print(f'\tMean: {round(_mean, 1)}')
        print(f'\tMax: {max(day)}')
        print(f'\tMin: {min(day)}')

    print(f'Mean temperature of the week: {round(_sum / len(temperature), 1)}')

if __name__ == "__main__":
    main()