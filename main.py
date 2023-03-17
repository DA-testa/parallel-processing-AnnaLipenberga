# python3
 
    
def parallel_processing(n, data):
    output = []
    Btimes = n*[0]

    for work in data:
        Min = min(Btimes)
        thread = Btimes.index(Min)

        output.append((thread, min_busy_time))
        Btimes[thread] += work

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()
