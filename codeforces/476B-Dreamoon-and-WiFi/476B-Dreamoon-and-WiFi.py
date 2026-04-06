from collections import defaultdict

original = input()
received = input()

target_pos = 0
for char in original:
    target_pos += 1 if char == "+" else -1

outcomes = defaultdict(int)

def find(index, current_val):
    if index == len(received):
        outcomes[current_val] += 1
        return

    char = received[index]
    if char == "+":
        find(index + 1, current_val + 1)
    elif char == "-":
        find(index + 1, current_val - 1)
    else:  
        find(index + 1, current_val + 1)
        find(index + 1, current_val - 1)

find(0, 0)

total_paths = sum(outcomes.values())
successful_paths = outcomes[target_pos]

print(f"{successful_paths / total_paths:.12f}")