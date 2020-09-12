def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
x=int(input("enter first number :"))
y=int(input("enter second number :"))
z=int(input("enter third number :"))
print("sum is",sum(x, y, z))