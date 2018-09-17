 #-*- encoding= utf-8 -*-
 '''
 将一个待排数据按其大小插入到已经排序的数据中的适当位置，直到全部插入完毕。
 @collator 实验楼
 @edit https://www.shiyanlou.com
 '''
def insertsort(list):
    if list != None:
        if len(list) == 1:
            pass
        else:
            for i in range(1,len(list)):#start with second item. 
                temp = list[i]
                for j in range(i):
                    if list[j]>list[i]:
                        for k in range(i,j,-1):#
                            list[k]= list[k-1]
                        list[j] = temp
                         
if __name__ == '__main__':                
    list1 = [3,2,7,5,8,9,6,54,1,42]
    insertsort(list1)
    print(list1)