with open("input.txt", 'r') as file:
    count = 0
    count2 = 0
    for line in file:
        count2 += 1
        numbers = line.split()
        valid = True
        descending = False
        ascending = False
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
            numbers[i-1] = int(numbers[i-1])  
            if i > 0:
                difference = numbers[i] - numbers[i-1]
                differenceabs = abs(difference)
                if differenceabs < 1 or differenceabs > 3:
                    valid = False
                if difference < 0:
                    descending = True
                if difference > 0:
                    ascending = True

                print(numbers[i], numbers[i-1], f"difference: {difference}")
                print(f"ascending: {ascending}, descending {descending}")
        if descending and ascending:
            valid = False
        print(f"line end, {valid}:")
        if valid:   
            count += 1

    print(count)
 

                        
                        
        


