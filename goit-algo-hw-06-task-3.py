import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]
G.add_nodes_from(stations)

travel_time_base = 2  # вага ребра (2 хвилини між сусідніми станціями)

edges_with_weights = []
for i in range(len(stations) - 1):
    edges_with_weights.append((stations[i], stations[i+1], {'weight': travel_time_base}))

G.add_edges_from(edges_with_weights)

transfer_time = 5 # пересадка в хабі наприклад 5 хвилин

G.add_node("Майдан Незалежності")
G.add_edge("Хрещатик", "Майдан Незалежності", weight=transfer_time)

G.add_node("Золоті Ворота")
G.add_edge("Театральна", "Золоті Ворота", weight=transfer_time)

G.add_node("Палац Спорту")
G.add_edge("Майдан Незалежності", "Палац Спорту", weight=transfer_time)
G.add_node("Кловська")
G.add_edge("Палац Спорту", "Кловська", weight=travel_time_base)

# Визначення станцій для розрахунку
start_station = "Лісова"
end_station = "Золоті Ворота"

shortest_path = nx.dijkstra_path(G, source=start_station, target=end_station, weight='weight')
shortest_time = nx.dijkstra_path_length(G, source=start_station, target=end_station, weight='weight')

print(f"## ➡️ Найкоротший шлях від '{start_station}' до '{end_station}' (Алгоритм Дейкстри):")
print(f"Шлях: {' -> '.join(shortest_path)}")
print(f"Загальний час у дорозі: {shortest_time} хвилин")
    
pos = nx.spring_layout(G, seed=42)

hubs = [node for node, degree in G.degree() if degree >= 3]
other_nodes = [node for node in G.nodes() if node not in hubs]

plt.figure(figsize=(14, 9))

nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=1.5)

path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='purple', width=3.0, label='Найкоротший шлях')

nx.draw_networkx_nodes(G, pos, nodelist=hubs, node_size=1000, node_color='red')
nx.draw_networkx_nodes(G, pos, nodelist=other_nodes, node_size=500, node_color='skyblue')

nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold', font_color='black')

plt.scatter([], [], color='red', s=100, label='Хаби (Пересадки)')
plt.scatter([], [], color='skyblue', s=100, label='Станції')
plt.plot([], [], color='purple', linewidth=3, label='Обраний шлях')

plt.title(f"Модель метро з вагами: Шлях від {start_station} до {end_station}", fontsize=15)
plt.legend(scatterpoints=1)
plt.axis('off')
plt.show()