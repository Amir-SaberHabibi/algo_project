import heapq, random
import matplotlib.pyplot as plt
import networkx as nx

NUM_NODES = 1000
NUM_EDGES = 1000
src = 0
# dest = 5

# def dijkstra_unidirectional(graph, src, dest):
#     n = len(graph)
#     distances = [float('inf')] * n
#     distances[src] = 0
#     pq = [(0, src)]
#     while pq:
#         d, u = heapq.heappop(pq)
#         if d > distances[u]:
#             continue
#         for v, w in graph[u]:
#             if distances[v] > distances[u] + w:
#                 distances[v] = distances[u] + w
#                 heapq.heappush(pq, (distances[v], v))
#     return distances[dest]

def dijkstra_bidirectional(graph, src, dest):
    n = len(graph)
    distances_f = [float('inf')] * n
    distances_b = [float('inf')] * n
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
    for i in range(n):
        if distances_f[i] + distances_b[i] < min_distance:
            min_distance = distances_f[i] + distances_b[i]
    return min_distance

# Generate two random graphs
graph1 = nx.gnm_random_graph(NUM_NODES, NUM_EDGES, seed=42)
# graph2 = nx.gnm_random_graph(NUM_NODES, NUM_EDGES, seed=43)

# Add random weights to edges
for u, v, data in graph1.edges(data=True):
    data['weight'] = random.randint(1, 10)
for u, v, data in graph1.edges(data=True):
    data['weight'] = random.randint(1, 10)

# Compute shortest path with unidirectional approach
path1_uni = nx.shortest_path(graph1, source=src, target=10, weight='weight')
path2_uni = nx.shortest_path(graph1, source=src, target=10, weight='weight')

# Compute shortest path with bidirectional approach
adj1 = [[] for _ in range(NUM_NODES)]
adj2 = [[] for _ in range(NUM_NODES)]
for u, v, data in graph1.edges(data=True):
    w = data['weight']
    adj1[u].append((v, w))
    adj1[v].append((u, w))
for u, v, data in graph1.edges(data=True):
    w = data['weight']
    adj2[u].append((v, w))
    adj2[v].append((u, w))

# path1_bi = dijkstra_bidirectional(adj1, src=src, dest=NUM_NODES-1)
# path2_bi = dijkstra_bidirectional(adj2, src=src, dest=NUM_NODES-1)
# path_bi = path1_bi + path2_bi

# fig, ax = plt.subplots()
# pos = nx.spring_layout(graph1)
# nx.draw(graph1, pos, with_labels=True)
# nx.draw_networkx_edges(graph1, pos, edgelist=[(path1_uni[i], path1_uni[i+1]) for i in range(len(path1_uni)-1)], edge_color='r', width=3)
# ax.set_title("Shortest path via Dijkstra's algorithm")
# plt.show()

fig, ax = plt.subplots()
pos = nx.spring_layout(graph1)
nx.draw(graph1, pos, with_labels=True)
nx.draw_networkx_edges(graph1, pos, edgelist=[(path1_uni[i], path1_uni[i+1]) for i in range(len(path1_uni)-1)], edge_color='r', width=3)
labels = nx.get_edge_attributes(graph1,'weight')
nx.draw_networkx_edge_labels(graph1,pos,edge_labels=labels)
ax.set_title("Shortest Path via Dijkstra's Algorithm")
print(path1_uni)
plt.show()


# fig, ax = plt.subplots()
# pos = nx.spring_layout(graph1)
# nx.draw(graph1, pos, with_labels=True)
# nx.draw_networkx_edges(graph1, pos, edgelist=[(path1_uni[i], path1_uni[i+1]) for i in range(len(path1_uni)-1)], edge_color='r', width=3)
# labels = nx.get_edge_attributes(graph1,'weight')
# nx.draw_networkx_edge_labels(graph1,pos,edge_labels=labels)
# ax.set_title("Shortest path via Dijkstra's algorithm")
# plt.show()

# fig, ax = plt.subplots()
# pos = nx.spring_layout(graph2)
# nx.draw(graph2, pos, with_labels=True)
# nx.draw_networkx_edges(graph2, pos, edgelist=[(path2_bi[i], path2_bi[i+1]) for i in range(len(path2_bi)-1)], edge_color='r', width=3)
# ax.set_title("Shortest path with bidirectional Dijkstra's algorithm")
# plt.show()
