import heapq

li = [5, 7, 9, 1, 3]

heapq.heapify(li)

# take not of pattern
print("created heap is :", (list(li)))

heapq.heappush(li, 4)
print("modified heap after push is :", list(li))

print("")

li1 = [5, 1, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]

heapq.heapify(li1)
heapq.heapify(li2)

# pops 2
print("popped item using heappushpop is : ", end="")
print(heapq.heappushpop(li1, 2))
print("modified heap after heappushpop is :", list(li1))


# pops 3
print("popped item using heapreplace is : ", end="")
print(heapq.heapreplace(li2, 2))
print("modified heap after heapreplace is :", list(li2))
