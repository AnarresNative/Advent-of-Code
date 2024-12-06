with open("input.txt", "r") as file:
    count_of_valid = 0
    for line in file:
        
        # iterate through all lines in the file
        numbers = line.split()
        valid = True

        # Initialise variables as false to track whether differences are ascending vs descending
        descending = False
        ascending = False
        for i in range(len(numbers)):

            # cast values to integers
            numbers[i] = int(numbers[i])
            numbers[i - 1] = int(numbers[i - 1])
            if i > 0:
                # calculate differences
                difference = numbers[i] - numbers[i - 1]

                # use absolute for calculating the size of the difference, as directionality not important
                difference_abs = abs(difference)
                if difference_abs < 1 or difference_abs > 3:
                    valid = False

                # Track whether differences are ascending or descending so we can filter out those with both
                if difference < 0:
                    descending = True
                if difference > 0:
                    ascending = True

                # Debugging message
                # print(numbers[i], numbers[i - 1], f"difference: {difference}")
                # print(f"ascending: {ascending}, descending {descending}")
        if descending and ascending:
            valid = False
        # print(f"line end, {valid}:")
        if valid:
            count_of_valid += 1

    print(count_of_valid)
