import heapq, time
from random import randint
import matplotlib.pyplot as plt

NUM_NODES_LIST = [100 * (i + 1) for i in range(11)]
NUM_EDGES = 10000
src = 0
times_uni = []
times_bi = []

def generate_random_graph(num_nodes, NUM_EDGES):
    graph = {i: [] for i in range(num_nodes)}
    for i in range(NUM_EDGES):
        u = randint(0, num_nodes - 1)
        v = randint(0, num_nodes - 1)
        w = randint(1, 10)
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph

def dijkstra_unidirectional(graph, src, dest):
    distances = [float('inf')] * len(graph)
    distances[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > distances[u]:
            continue
        for v, w in graph[u]:
            if distances[v] > distances[u] + w:
                distances[v] = distances[u] + w
                heapq.heappush(pq, (distances[v], v))
    return distances[dest]

def dijkstra_bidirectional(graph, src, dest):
    distances_f = [float('inf')] * len(graph)
    distances_b = [float('inf')] * len(graph)
    distances_f[src] = 0
    distances_b[dest] = 0
    pq_f = [(0, src)]
    pq_b = [(0, dest)]
    visited_f = set()
    visited_b = set()
    while pq_f and pq_b:
        d_f, u_f = heapq.heappop(pq_f)
        d_b, u_b = heapq.heappop(pq_b)
        if d_f > distances_f[u_f]:
            continue
        if d_b > distances_b[u_b]:
            continue
        visited_f.add(u_f)
        visited_b.add(u_b)
        if u_f in visited_b or u_b in visited_f:
            break
        for v_f, w_f in graph[u_f]:
            if distances_f[v_f] > distances_f[u_f] + w_f:
                distances_f[v_f] = distances_f[u_f] + w_f
                heapq.heappush(pq_f, (distances_f[v_f], v_f))
        for v_b, w_b in graph[u_b]:
            if distances_b[v_b] > distances_b[u_b] + w_b:
                distances_b[v_b] = distances_b[u_b] + w_b
                heapq.heappush(pq_b, (distances_b[v_b], v_b))
    min_distance = float('inf')
    for i in range(len(graph)):
        if distances_f[i] + distances_b[i] < min_distance:
            min_distance = distances_f[i] + distances_b[i]
    return min_distance


for num_nodes in NUM_NODES_LIST:
    graph = generate_random_graph(num_nodes, NUM_EDGES)
    
    start_time = time.time()
    dijkstra_unidirectional(graph, src, num_nodes - 1)
    end_time = time.time()
    times_uni.append(end_time - start_time)
    
    start_time = time.time()
    dijkstra_bidirectional(graph, src, num_nodes - 1)
    end_time = time.time()
    times_bi.append(end_time - start_time)

plt.plot(NUM_NODES_LIST, times_uni, color='red', label='Unidirectional')
plt.plot(NUM_NODES_LIST, times_bi, color='blue', label='Bidirectional')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
