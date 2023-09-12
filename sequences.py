def remove_duplicates(sequence):
    result = []
    seen = set()
    for item in sequence:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)