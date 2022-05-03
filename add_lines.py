with open("D:\\Python\\Python Course with Notes\\9. Chapter 9\\add_eachline.txt") as f:
    # use ith open("add_eachline.txt") as f: , use this when doing in other system
    data = f.readlines()
    replaced_data = [elem.replace("\n",'') for elem in data]
    num=0
    for i in range(len(replaced_data)):
        num = num + int(replaced_data[i])
    
print(num)