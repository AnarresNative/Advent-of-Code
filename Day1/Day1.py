file_path = "input.txt"
list_1 = []
list_2 = []

def list_insert_sorted(locations, to_add):
    # using a non optimal sorting function as the list of values is only 1000
    index = 0
    inserted = False
    for i in locations:
        if to_add < i and not inserted:
            locations.insert(index, to_add)
            inserted = True
        elif index == (len(locations)-1) and not inserted:
            locations.insert((index+1), to_add)
            inserted = True
        index += 1
    return(locations)

# create ordered lists
with open(file_path, "r") as file:
    inserted_first = False
    for line in file:       
        # iterate through all lines in the file
        numbers = line.split()
        if inserted_first:
            list_1 = list_insert_sorted(locations=list_1, to_add=numbers[0])
            list_2 = list_insert_sorted(locations=list_2, to_add=numbers[1])
        # add first value
        if not inserted_first:
            list_1.append(numbers[0])
            list_2.append(numbers[1])
            inserted_first = True


diff = 0
n = len(list_1)
# calculate difference between sorted lists
for i in range(n):
    # use the absolute difference as some will be pos and some neg
    diff = diff + abs((int(list_1[i])-int(list_2[i])))
print(diff)
