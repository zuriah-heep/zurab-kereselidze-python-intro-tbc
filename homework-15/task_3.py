def main():
    friends = {}
    while True:
        info = input('Please input name pairs: ').upper()
        if info == 'FINISH':
            break
        pair = tuple(map(lambda x: x.strip().capitalize(), info.split('-')))
        for i in range(2):
            if pair[i] not in friends:
                friends[pair[i]] = pair[1 - i]
            elif pair[1 - i] not in friends[pair[i]]:
                friends[pair[i]] += ', ' + pair[1 - i]

    for key, val in friends.items():
        print(key, '-', val)

if __name__ == '__main__':
    main()