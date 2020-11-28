# @author Matheus Alves dos Santos

def find_set(item, sets):
    if sets[item] != item:
        sets[item] = find_set(sets[item], sets)

    return sets[item]


def join_sets(item1, item2, sets):
    set1, set2 = find_set(item1, sets), find_set(item2, sets)

    if set1 != set2:
        sets[set2] = set1


while True:
    n_junctions, n_roads = map(int, input().split())
    if (n_junctions + n_roads) == 0:
        break

    roads = []
    for i in range(n_roads):
        junction1, junction2, length = map(int, input().split())
        roads.append((length, junction1, junction2))

    junction_sets = [i for i in range(n_junctions)]
    roads = sorted(roads, reverse=True)

    spared_amout = 0
    while roads:
        length, junction1, junction2 = roads.pop()
        set1 = find_set(junction1, junction_sets)
        set2 = find_set(junction2, junction_sets)

        if (set1 == set2):
            spared_amout += length
        else:
            join_sets(junction1, junction2, junction_sets)

    print(spared_amout)
