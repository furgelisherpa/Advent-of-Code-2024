# part one
def total_distance(lhs: list, rhs: list) -> int:
    if lhs is None or rhs is None:
        raise ValueError("lhs or rhs is None")
    if not (isinstance(lhs, (tuple, list)) and isinstance(rhs, (tuple, list))):
        raise ValueError("lhs and rhs must be lists or tuples")

    lhs.sort()
    rhs.sort()

    total = 0
    for lhi, rhi in zip(lhs, rhs):
        total += abs(lhi-rhi)
    return total


# part two
def similarity_score(lhs: list, rhs: list) -> int:
    similarity = 0
    for i in set(lhs):
        count = rhs.count(i)
        if count > 0:
            similarity += count*i
    return similarity


def read_input(filename: str):
    lhs, rhs = [], []
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    lh, rh = map(int, line.strip().split())
                    lhs.append(lh)
                    rhs.append(rh)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
    except FileNotFoundError:
        print(f"Error: file {filename} not found")
        return [], []
    return lhs, rhs


def main():
    filename = "01_input"
    lhs, rhs = read_input(filename)

    result = total_distance(lhs, rhs)
    simi = similarity_score(lhs, rhs)

    print(f"total distance: {result}")
    print(f"similarity scores: {simi}")


if __name__ == "__main__":
    main()
