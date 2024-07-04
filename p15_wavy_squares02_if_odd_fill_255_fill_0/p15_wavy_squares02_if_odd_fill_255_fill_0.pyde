# p15_wavy_squares02_if_odd_fill_255_fill_0
size(480, 480)
for i in range(16):
    for j in range(16):
        if (i+j)%2==1: fill(255) # 白色
        else: fill(0) # 黑色
        
        rect(i*30, j*30, 30, 30)
        
        if (i+j)%2==1: fill(0) # 黑色
        else: fill(255) # 白色
        
        rect(i*30+2, j*30+2, 9, 9)
        rect(i*30+19, j*30+19, 9, 9)
