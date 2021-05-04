def solution(array, commands):
    for item in commands:
        list_of_command =[]
        list_of_command =list_of_command.append(item)  
        i=item[0]
        j=item[1]
        k=item[2]
        before_sort=array[i:k]
        sorted_list=sort(before_sort)
        answer= sorted_list[k]       
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])