import heapq

def min_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)

        cost = first_min + second_min
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6]
print("Мінімальні загальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
