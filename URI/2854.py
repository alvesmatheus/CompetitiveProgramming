# @author Matheus Alves dos Santos

def build_adjacency_list(edges):
    adjacency_list = {}

    for edge in edges:
        if edge[0] in adjacency_list.keys():
            adjacency_list[edge[0]].append(edge[1])
        else:
            adjacency_list[edge[0]] = [edge[1]]

        if edge[1] in adjacency_list.keys():
            adjacency_list[edge[1]].append(edge[0])
        else:
            adjacency_list[edge[1]] = [edge[0]]

    return adjacency_list


def depth_first_search(node, adjacency_list, visited_nodes):
    if node not in visited_nodes:
        visited_nodes.append(node)

        for adjacent_node in adjacency_list[node]:
            depth_first_search(adjacent_node, adjacency_list, visited_nodes)


n_people, n_relationships = map(int, input().split())
relationships, visited_nodes, n_family_trees = [], [], 0

for i in range(n_relationships):
    person_from, relationship, person_to = input().split()
    relationships.append((person_from, person_to))

family_trees = build_adjacency_list(relationships)
people = list(family_trees.keys())

for person in people:
    if person not in visited_nodes:
        n_family_trees += 1
        depth_first_search(person, family_trees, visited_nodes)

print(n_family_trees)
