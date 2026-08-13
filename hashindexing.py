size = 10
hash_table = [[] for _ in range(size)]
for i in range(3):
    roll_no = int(input("Enter Roll No: "))
    index = roll_no % size
    hash_table[index].append(roll_no)
print("\nHash Index:")
for i in range(size):
    if hash_table[i]:
        print("Index", i, ":", hash_table[i])
