from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")                       # Terry arrives
queue.append("Graham")                      # Graham arrives
print(queue.popleft())                      # The first to arrive now leaves 'Eric'
print(queue.popleft())                      # The second to arrive now leaves 'John'
print(queue)                                # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
