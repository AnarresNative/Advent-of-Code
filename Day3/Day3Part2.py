import re

def count_mul(input_string=""):
    """ 
    This is a functionised version of the regex counter from part 1.
    My current thinking is to split the string imported from input.txt at do's and dont's and then process
    """
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",input_string)
    
    results = [(int(a), int(b)) for a, b in matches]

    products = [a * b for a, b in results]

    multi_sum = sum(products)

    return multi_sum

with open("input.txt", "r") as file:
    content = file.read()
    delete = False
    cleaned_content = []
    i = 0
    # iterate through the string and only add anything after a do() clause
    while i < len(content):
        if content[i:].startswith("don't()"):
            delete = True
            i += len("don't()")
        elif content[i:].startswith("do()"):
            delete = False
            i += len("do()")
        else:
            if not delete:
                cleaned_content.append(content[i])
            i += 1

final_output = "".join(cleaned_content)
final_count = count_mul(final_output)
print(final_count)
