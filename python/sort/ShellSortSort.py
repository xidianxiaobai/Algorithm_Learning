#先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序
# 然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）
#再对全体元素进行一次直接插入排序。
'''
 @collator 实验楼
 @edit https://www.shiyanlou.com
'''
test=[9,2,3,5,7]

def ShellSort(data,flag):
    '''
    data: list,to be sorted
    flag: 0->asc,1->desc
    return a new sorted list
    '''
    retData=[]
    
    #copy data to retData
    for item in data:
        retData.append(item)    
    
    #sort retData
    count=len(retData)
    step=count/2;
    while step>0:
        i=0
        while i<count:
            j=i+step
            while j<count:
                t=retData.pop(j)
                k=j-step
                #asc
                if flag==0:
                    while k>=0:
                        if t>=retData[k]:
                            retData.insert(k+1, t)
                            break
                        k=k-step
                        
                    if k<0:
                        retData.insert(0, t)
                #desc
                elif flag==1:    
                    while k>=0:
                        if t<=retData[k]:
                            retData.insert(k+1, t)
                            break
                        k=k-step
                    if k<0:
                        retData.insert(0, t)
                        
                j=j+step
            
            i=i+1
        
        step=step/2
    
    return retData


data=ShellSort(test,0)
print 'Asc:',data
data=ShellSort(test,1)
print 'Desc:',data