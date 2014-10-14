# Enter your code here. Read input from STDIN. Print output to STDOUT


import fileinput

line_array = []
for line in fileinput.input():
    line_array.append(int(line))

target_num = line_array[1]
result_num = target_num
no_of_digits = 0
#print target_num , "target"
while result_num > 0:
    last_digit = result_num % 10
    #print last_digit, "last_digit"
    if result_num % last_digit == 0:
        no_of_digits += 1
        #print no_of_digits , "num of digits"
    result_num = int(result_num / 10)
    #print result_num, "result num"
    
print no_of_digits
    