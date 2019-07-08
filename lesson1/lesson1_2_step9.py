objects = ["str", True, 1, 123, 5.4, [1,2,3], 1, "str", "abc"]

mn = set()

for obj in objects:
    mn.add(id(obj)) # Если не использовать идентификаторы элементов списка, то при сравнении True и 1 будет равенство
                    # Так как True is not 1, но True == 1

ans = len(mn)

print(ans)
