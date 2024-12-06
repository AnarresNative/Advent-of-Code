file_path = "input.txt"
list_1 = []
list_2 = []

def list_insert_sorted(locations, to_add):
    # using a non optimal sorting function as the list of values is only 1000
    index = 0
    inserted = False
    for i in locations:
        i = int(i)
        if int(to_add) < i and not inserted:
            locations.insert(index, int(to_add))
            inserted = True
        elif index == (len(locations)-1) and not inserted:
            locations.insert((index+1), int(to_add))
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
            list_1.append(int(numbers[0]))
            list_2.append(int(numbers[1]))
            inserted_first = True


diff = 0
n = len(list_1)
# calculate difference between sorted lists
similarity_score_total = 0
for i in list_1:
    similarity_counter = 0
    for x in list_2:
        # use the absolute difference as some will be pos and some neg
        if i == x:
            similarity_counter += 1
    
    similarity_score  = i * similarity_counter
    similarity_score_total = similarity_score_total + similarity_score 
    
    print(similarity_score_total)
