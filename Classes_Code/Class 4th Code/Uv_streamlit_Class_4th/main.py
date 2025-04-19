
count = 1

# while count <= 5:
#     print("Kharak singh k kharakney sai kharak ti hai khirkiya")
#     count += 1

# iftari_itemss = ["Rooz Afza", "Pakorey", "Samosey"]

# for item in iftari_items:
#     print("-" * 50)
#     print(item)

def sum_of_numbers(*n):
    total = 0
    for num in n:
        total += num

    return total

answer = sum_of_numbers(5, 6, 8, 24, 10)
print(answer)







