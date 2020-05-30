import math

def shortest_path(M,start,goal):
    print("shortest path called")

    map_dict = M.intersections
    road_list = M.roads

    start_coordinate = map_dict[start]
    end_coordinate = map_dict[goal]

    path = str(start)
    frontier_dict = {}

    shortest_path = shortest_path_rec(map_dict, road_list, start, goal, frontier_dict, 0, path)

    return shortest_path


def shortest_path_rec(map_dict, road_list, start, goal, frontier_dict, shortest_distance, path):
        if start == goal:
            path = path.split("-")
            final = []
            for intersection in path:
                final.append(int(intersection))
            return final

        start_coordinate = map_dict[start]
        end_coordinate = map_dict[goal]

        for stop in road_list[start]:
            path_a = path
            coordinate = map_dict[stop]
            g_distance = math.sqrt((coordinate[0] - start_coordinate[0])**2 + (coordinate[1] - start_coordinate[1])**2) + shortest_distance
            h_distance = math.sqrt((end_coordinate[0] - coordinate[0])**2 + (end_coordinate[1] - coordinate[1])**2)
            f_distance = g_distance + h_distance
            path_a += "-" + str(stop)
            frontier_dict[stop] = (f_distance, g_distance, path_a)

        sorted_frontier = sorted(frontier_dict.items(), key = lambda x:x[1][0])
        f_d, shortest_distance, path = frontier_dict.pop(sorted_frontier[0][0])

        return shortest_path_rec(map_dict, road_list, sorted_frontier[0][0], goal, frontier_dict, shortest_distance, path)
