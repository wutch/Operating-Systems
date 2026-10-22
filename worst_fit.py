def worst_fit(blocks, processes):
    remaining = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_index = -1

        for j in range(len(remaining)):
            if remaining[j] >= processes[i]:
                if worst_index == -1 or remaining[j] > remaining[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            remaining[worst_index] -= processes[i]

    return allocation, remaining
