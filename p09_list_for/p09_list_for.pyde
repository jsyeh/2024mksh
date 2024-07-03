# p09_list_for
names = ['Alice', 'Bob', 'Cola'] # list陣列
for name in names:
    print(name)
background(0, 0, 255)
size(300, 300)
for i in range(len(names)):
    text(names[i], i*100, 100)
    
