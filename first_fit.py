def first_fit(blocks, processes):
    remaining = blocks.copy()
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(remaining)):
            if remaining[j] >= processes[i]:
                allocation[i] = j
                remaining[j] -= processes[i]
                break

    return allocation, remaining
