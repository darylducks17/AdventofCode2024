def answer1(): 
    
    left_list = []
    right_list = []

    with open("day1/input.txt") as input: 
        #splitting the input into left and right lists
        for line in input: 
            left_column, right_column = map(int, line.split())
            left_list.append(left_column)
            right_list.append(right_column)
        #sorting the list from smallest to largest (ascending)    
        l = sorted(left_list)
        r = sorted(right_list)
        #iteration of subtracting the smallest number in left list from the right list
        #https://sparkbyexamples.com/python/python-list-subtraction/#:~:text=You%20can%20perform%20list%20subtraction,elements%20from%20list1%20and%20list2%20.
        #https://www.w3schools.com/python/ref_func_abs.asp
        distances = [abs(left - right) for left, right in zip(l, r)]
        #sum of distances
        result = sum(distances)
        print(f'Sum of Distances: {result}' )

answer1()

def answer2(): 
    left_list = []
    right_list = []

    with open("day1/input.txt") as input: 
        #splitting the input into left and right lists
        for line in input: 
            left_column, right_column = map(int, line.split())
            left_list.append(left_column)
            right_list.append(right_column)
        #sorting the list from smallest to largest (ascending)    
        l = sorted(left_list)
        r = sorted(right_list)
        #counting occurrences of each number in the right list
        #https://www.geeksforgeeks.org/python-frequency-of-elements-from-other-list/
        result = {key: r.count(key) for key in l}
        #calculating the similarity score
        similarity_score = 0 
        for number in l: 
            #multiply the number by its count in the right list
            similarity_score += number * result[number] 
        print(f'Similarity Score: {similarity_score}')

answer2()