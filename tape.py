def optimal_storage_on_tape(files):
    files.sort()

    cumulative_time = 0
    total_retrieval_time = 0

    for size in files:
        cumulative_time += size
        total_retrieval_time += cumulative_time

    average_retrieval_time = total_retrieval_time / len(files)

    return files, total_retrieval_time, average_retrieval_time

files = [20, 10, 30, 5]
order, total_time, avg_time = optimal_storage_on_tape(files)

print("Optimal Order:", order)
print("Total Retrieval Time:", total_time)
print("Average Retrieval Time:", avg_time)

