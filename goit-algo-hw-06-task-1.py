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

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Кількість станцій (Вершин V): {num_nodes}")
print(f"Кількість сполучень (Ребер E): {num_edges}")

degree_map = dict(G.degree())
sorted_degree = sorted(degree_map.items(), key=lambda item: item[1], reverse=True)

print("\nТоп-5 станцій за Ступенем:")
for station, degree in sorted_degree[:5]:
    print(f"- {station}: {degree}")

print(f"\nСтупінь станції 'Хрещатик': {degree_map.get('Хрещатик')}")
print(f"Ступінь станції 'Лісова': {degree_map.get('Лісова')}")

pos = nx.spring_layout(G, seed=42)

hubs = [node for node, degree in G.degree() if degree >= 3]
other_nodes = [node for node in G.nodes() if node not in hubs]

plt.figure(figsize=(12, 8))

nx.draw(G, pos,
        edgelist=G.edges(),
        edge_color='gray',
        width=1.5,
        with_labels=False,
        node_size=0)

nx.draw(G, pos,
        nodelist=hubs,
        node_size=1000,
        node_color='red',
        with_labels=False)

nx.draw(G, pos,
        nodelist=other_nodes,
        node_size=500,
        node_color='skyblue',
        with_labels=False)

nx.draw(G, pos,
        with_labels=True,
        node_size=0,
        font_size=10,
        font_weight='bold',
        font_color='black') 

plt.scatter([], [], color='red', s=100, label='Хаби/Переходи')
plt.scatter([], [], color='skyblue', s=100, label='Станції')

plt.title("Модель транспортної мережі (фрагмент метро)", fontsize=15)
plt.legend(scatterpoints=1)
plt.axis('off')
plt.show()