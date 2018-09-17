#-*- encoding= utf-8 -*-
'''
从所有序列中先找到最小的，然后放到第一个位置。之后再看剩余元素中最小的，放到第二个位置……以此类推，就可以完成整个的排序工作
 
 @collator 实验楼
 @edit https://www.shiyanlou.com
'''
 
def selectionsort(list):
    if list != None:
        for i in range(len(list)):
            min = i
            for j in range(i+1,len(list)):
                if list[min] > list[j]:
                    min = j
            if min != i:
                list[min],list[i] = list[i],list[min]
 
if __name__ == '__main__':                
    list1 = [2,3,5,7,8,9,6,54,1,42]
    selectionsort(list1)
    print(list1)