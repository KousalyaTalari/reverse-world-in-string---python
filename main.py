input1=input("enter the sentence:").split(' ')
# print(input1)
output_list=[]
for i in range(len(input1)):
    output1=input1.pop()
    # print(type(output1))
    output1 = output1[::-1]
    # print(type(output1))
    # print(output1)
    output_list.insert(0,output1)
    i+=1
    continue
# print(output_list)
position_reverse=' '.join(output_list)
print(position_reverse)
