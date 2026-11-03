def calculate_disk_scheduling(requests, head, cylinders, algorithm, direction="Up"):
    requests = requests.copy()
    sequence = [head]
    movements = []
    total = 0

    def move_to(position):
        nonlocal total
        movements.append(abs(sequence[-1] - position))
        total += movements[-1]
        sequence.append(position)

    if algorithm == "FIFO":
        for request in requests:
            move_to(request)

    elif algorithm == "SSTF":
        while requests:
            nearest = min(requests, key=lambda x: abs(x - sequence[-1]))
            requests.remove(nearest)
            move_to(nearest)

    elif algorithm in ["LOOK", "ELEVATOR", "C-SCAN"]:
        lower = sorted([r for r in requests if r < head])
        upper = sorted([r for r in requests if r > head])
        equal = [r for r in requests if r == head]

        for request in equal:
            move_to(request)

        if direction == "Up":
            first, second = upper, lower
        else:
            first, second = lower[::-1], upper[::-1]

        for request in first:
            move_to(request)

        if algorithm == "LOOK":
            for request in second:
                move_to(request)

        elif algorithm == "ELEVATOR":
            boundary = cylinders - 1 if direction == "Up" else 0
            move_to(boundary)
            for request in second:
                move_to(request)

        elif algorithm == "C-SCAN":
            boundary = cylinders - 1 if direction == "Up" else 0
            opposite = 0 if direction == "Up" else cylinders - 1

            move_to(boundary)

            if second:
                move_to(opposite)
                for request in second:
                    move_to(request)

    average = total / len(movements) if movements else 0

    return {
        "sequence": sequence,
        "movements": movements,
        "total": total,
        "average": average
    }
