prime_numbers = [2,3,5,7,11,13,17,19,23,29]
prime_numbers2 = [7,2,5,7,1,13,17,9,23,29]

len = len(prime_numbers)

middlefive_list = prime_numbers[2:7]
print(middlefive_list)

new_list1= prime_numbers[::2]
print(new_list1)

new_list2= prime_numbers[-3:]
print(new_list2)

revere_list= prime_numbers[::-1]
print(revere_list)

decending_list= sorted(prime_numbers2, reverse=True)
print(decending_list)

