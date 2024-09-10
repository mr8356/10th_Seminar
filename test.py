from heapq import heappush, heappop, heapify

def solution(jobs):
    heap = []
    answer = 0
    time = 0
    for s, t in jobs:
        heappush(heap, (-1 * (s+t), s, t))
    for _ in range(len(jobs)):
        w,s,t = heappop(heap)
        if time - s >= 0:
              time += t
              answer += (time - s) + t
        else:
              answer += t
              time += (s - time) + t
    answer /= len(jobs)
    return answer