a = int(input())
b = int(input())
old_a = a
old_b = b

a, b = b, a

print(f"Before:\na = {old_a}\nb = {old_b}")
print(f"After:\na = {a}\nb = {b}")
