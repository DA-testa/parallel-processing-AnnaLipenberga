# python3

def parallel_processing(n, data):
    output = []
    thread_busy_times = [0] * n

    for job_exec_time in data:
        first_to_finish = min(thread_busy_times)
        thread = thread_busy_times.index(first_to_finish)

        output.append((thread, first_to_finish))
        thread_busy_times[thread] += job_exec_time

    return output


def main():
    n, _ = map(int, input().split(' '))
    data = list(map(int, input().split(' ')))

    result = parallel_processing(n, data)
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()


    
    
    
    import heapq

def parallel_processing(n, data):
    output = []
    thread = n*[0]
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    for job_exec_time in data:
        
        _, thread = heapq.heappop(heap)

        output.append((thread, thread_busy_times[thread]))
        thread[thread] += job_exec_time

        
        heapq.heappush(heap, (thread[thread], thread))

    return output


def main():
    n, _ = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()
