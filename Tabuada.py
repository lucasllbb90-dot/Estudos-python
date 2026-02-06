tabuada = int(input("digite o numero para ver sua tabuada : "))
print("-" * 12)
for c in range(1, 11):
    print(f"{tabuada} X{c : 3} = {c * tabuada}")