def parse_ranges(str_ranges):
    str_ranges = str_ranges.split(',')
    for str_range in str_ranges:
        parts = str_range.partition('-')
        start = int(parts[0])
        try:
            end = int(parts[2])
        except ValueError:
            end = start

        for n in range(start, end + 1):
            yield n
