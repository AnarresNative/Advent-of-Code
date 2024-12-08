import re
with open("input.txt", "r") as file:
    content = file.read()
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",content)

    results = [(int(a), int(b)) for a, b in matches]

    products = [a * b for a, b in results]

    sum = sum(products)
    print(sum)
