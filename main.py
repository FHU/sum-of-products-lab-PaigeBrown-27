#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        list_products = []
        for i in range (0, len(list1) -1):
            list_products.append(list1[i] * list2[i])
        end_num = sum(list_products)
        return end_num
    else:
       return "Error"

if __name__ == '__main__':
    nl1 = input()
    nl2 = input()
    num_list1 = nl1.split(" ")
    num_list2 = nl2.split(" ")
    
    for i in range (0, len(nl1)):
        num_list1.append(int(nl1[i]))
    for i in range (0, len(nl2)):
        num_list2.append(int(nl2[i]))
    #num_list1 = [int(input("Give me a list of numbers: "))]
    #num_list2 = [int(input("Give me a second list of numbers: "))]
    print(sum_of_products(num_list1, num_list2))
