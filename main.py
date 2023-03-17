# python3
 
    
def parallel_processing(n, data):
    output = []
    thread_busy_times = n*[0]

    for job_exec_time in data:
        min_busy_time = min(thread_busy_times)
        thread = thread_busy_times.index(min_busy_time)

        output.append((thread, min_busy_time))
        thread_busy_times[thread] += job_exec_time

    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()
