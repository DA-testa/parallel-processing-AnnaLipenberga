# python3
 
    
   def parallel_processing(n, data):
    output = []
    thread = n*[0]
    heap = [(0, i) for i in range(n)]

    def heapify(heap):
        for i in range(len(heap)-1, -1, -1):
            heapify_down(heap, i)

    def heapify_down(heap, i):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i

        if l < len(heap) and heap[l][0] < heap[smallest][0]:
            smallest = l

        if r < len(heap) and heap[r][0] < heap[smallest][0]:
            smallest = r

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            heapify_down(heap, smallest)

    heapify(heap)

    for job_exec_time in data:
        _, thread = heap[0]
        output.append((thread, thread[thread]))
        thread[thread] += job_exec_time
        heap[0] = (thread[thread], thread)
        heapify_down(heap, 0)

    return output


def main():
    n, _ = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, data)
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()
