print("Zadejte číslo a: ")
a = input()
print("Zadejte číslo b: ")
b = input()
print("Zadejte číslo c: ")
c = input()

if a > b > c:
    print("a je největší­")
elif a > c > b:
    print("a je největší­")
elif b > a > c:
    print("b je největší­")
elif b > c > a:
    print("b je největší­")
elif c > a > b:
    print("c je největší­")
elif c > b > a:
    print("c je největší­")
else:
    print("Čí­sla jsou stejná")