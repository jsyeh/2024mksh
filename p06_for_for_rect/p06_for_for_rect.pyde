# p06_for_for_rect
# 在 600x600裡,放10x10共100格
size(600,600)
background(164,255,85) # 背景色
for x in range(10):
    for y in range(10):
        fill(247,127,208) # 填充色
        rect(x*60, y*60, 55, 55)
