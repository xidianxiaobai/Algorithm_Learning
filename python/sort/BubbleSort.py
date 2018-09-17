#-*- encoding= utf-8 -*-

 
'''
比较相邻的元素大小，将小的前移，大的后移，就像水中的气泡一样，最小的元素经过几次移动，会最终浮到水面上。

@collator 实验楼
@edit https://www.shiyanlou.com
'''
 
def bubble(list):
    for i in range(len(list)):
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
  
if __name__ == '__main__':                
    list1 = [2,3,5,7,8,9,6,54,1,42]
    bubble(list1)
    print(list1)