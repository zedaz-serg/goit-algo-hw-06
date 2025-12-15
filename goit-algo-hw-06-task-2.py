import networkx as nx

G = nx.Graph()

stations = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]
G.add_nodes_from(stations)

edges = []
for i in range(len(stations) - 1):
    edges.append((stations[i], stations[i+1]))

G.add_edges_from(edges)

G.add_node("Майдан Незалежності")
G.add_edge("Хрещатик", "Майдан Незалежності")

G.add_node("Золоті Ворота")
G.add_edge("Театральна", "Золоті Ворота")

G.add_node("Палац Спорту")
G.add_edge("Майдан Незалежності", "Палац Спорту")
G.add_node("Кловська")
G.add_edge("Палац Спорту", "Кловська")

start_station = "Академмістечко"
end_station = "Кловська"

print(f"Старт: {start_station}")
print(f"Фініш: {end_station}")
print("---")

try:
    bfs_path = list(nx.shortest_path(G, source=start_station, target=end_station))
except nx.NetworkXNoPath:
    bfs_path = "Шлях не знайдено"

print(f"Шлях BFS (ширина): \n{bfs_path}")
print(f"Довжина шляху BFS (кількість переходів): {len(bfs_path) - 1 if isinstance(bfs_path, list) else 'N/A'}")
print("---")

try:
    dfs_paths_generator = nx.all_simple_paths(G, source=start_station, target=end_station, cutoff=100)
    dfs_path = next(dfs_paths_generator)
except StopIteration:
    dfs_path = "Шлях не знайдено"
except nx.NetworkXNoPath:
    dfs_path = "Шлях не знайдено"

print(f"Шлях DFS (глибина): \n{dfs_path}")
print(f"Довжина шляху DFS (кількість переходів): {len(dfs_path) - 1 if isinstance(dfs_path, list) else 'N/A'}")