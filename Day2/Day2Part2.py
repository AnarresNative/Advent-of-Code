def validate_numbers(numbers):
    valid = True
    descending = False
    ascending = False


    for i in range(1, len(numbers)):
        # Get the difference between current and previous number
        difference = numbers[i] - numbers[i-1]
        differenceabs = abs(difference)

        # Check if the difference is within the allowed range
        if differenceabs < 1 or differenceabs > 3:
            valid = False

        # ADjust ascending and descending values
        if difference < 0:
            descending = True
        if difference > 0:
            ascending = True

    # If the sequence is both ascending and descending, it is invalid
    if descending and ascending:
        valid = False

    return valid


# Main logic to read from file and apply the validation
with open("input.txt", 'r') as file:
    count = 0   # To track how many lines are valid
    count2 = 0  # To track how many lines have been processed
    for line in file:
        numbers = list(map(int, line.split()))
        line_size = len(numbers)
        # print(line_size)
        count2 += 1
        count3 = 0
        valid = False
        while valid is False and count3 < line_size:
            # print(numbers)
            numbers_dupe = numbers.copy()
            numbers_dupe.pop(count3)
            # print(numbers_dupe)
            valid = validate_numbers(numbers_dupe)
            # print(f"line end, valid: {valid}")
            # print(count3)
            if valid:
                count += 1
            count3 += 1

    # Print the total count of valid lines after processing the file
    print(count)
