def best_fit(blocks, processes):
    remaining = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_index = -1

        for j in range(len(remaining)):
            if remaining[j] >= processes[i]:
                if best_index == -1 or remaining[j] < remaining[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            remaining[best_index] -= processes[i]

    return allocation, remaining
