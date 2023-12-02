
def read_file(file_name):
    with open(file_name, "r") as f:
        return f.read()


def find_digits(line):
    num = "".join(filter(str.isdigit, line))
    fist_dig = num[0]
    last_dig = num[-1]
    final_dig = fist_dig + last_dig
    final_dig = int(final_dig)
    return final_dig
   
if __name__ == "__main__":
    lines = read_file("../data.txt").splitlines()
    sum = 0
    print(lines)
    for line in lines:
        sum += find_digits(line)

    print(sum)

    