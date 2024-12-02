def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check all differences are valid
    if not all(diff in (-3, -2, -1, 1, 2, 3) for diff in differences):
        return False

    # Check if the report is consistently increasing or decreasing
    is_increasing = all(diff > 0 for diff in differences)
    is_decreasing = all(diff < 0 for diff in differences)

    return is_increasing or is_decreasing

safe_count = 0

with open("data.txt", "r") as reports:
    for report in reports:
        report = list(map(int, report.split()))
        if is_safe(report):
            safe_count += 1


print(f"Number of safe reports: {safe_count}")
