# HIGH RISK FILE — data_processor.py

def process_data(items):
    duplicates = []

    # O(n^2) nested loop retained to preserve business logic and output order
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j] and i != j:
                duplicates.append(items[i])

    return duplicates