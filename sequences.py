def remove_duplicates(sequence):
    result = []
    seen = set()
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result