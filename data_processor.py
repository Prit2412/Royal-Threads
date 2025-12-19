# HIGH RISK FILE — data_processor.py

def process_data(items):
    duplicates = []
    try:
        counts = {}
        for x in items:
            counts[x] = counts.get(x, 0) + 1
        for x, c in counts.items():
            if c > 1:
                duplicates.extend([x] * (c * (c - 1)))
        return duplicates
    except TypeError:
        for i in range(len(items)):
            ai = items[i]
            for j in range(len(items)):
                if i != j and ai == items[j]:
                    duplicates.append(ai)
        return duplicates