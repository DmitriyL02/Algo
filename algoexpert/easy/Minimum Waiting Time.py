def minimumWaitingTime(queries):
    # Write your code here.

    if not queries:
        return

    queries_count = len(queries) - 1
    idx = 1
    queries.sort()

    queries_amount_count = queries[0] * queries_count

    while queries_count > 0:

        queries_amount_count += queries[idx] * (queries_count - 1)
        queries_count -= 1
        idx += 1

    return queries_amount_count
