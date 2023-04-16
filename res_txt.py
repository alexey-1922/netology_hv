import os
ls = [i for i in os.listdir() if i.endswith('.txt')]
list_len = []
list_file = []
for j in ls:
    s = open((j),encoding='utf-8').readlines()
    list_file.append(j) 
    list_len.append(len(s))
file_len = list(zip(list_len, list_file))
file_len.sort()
#print(file_len)    

with open('res','w', encoding='utf-8') as f:
  for len, file in file_len:
    s = open((file), encoding='utf-8').read()
    print(s)
    f.write(file)
    f.write('\n')
    f.write(str(len))
    f.write('\n')
    f.write(s)
    f.write('\n')
     
    
