def solution(string):
    if string.islower():
        if 2 <= len(string) <= 300000: 
            split_string = [string[i:i+2] for i in range(0, len(string), 1)]
            
            l1=[]
            l2=[]
            l3=[]
            results=[]
            s = 0
            
            for i in split_string:
                if i not in l1:
                    l1.append(i)
                else:
                    l2.append(i)
            
            if not l2:
                print('-1')
                exit()
            else:
                for i in l2:
                    for item in split_string:
                        if item == i:
                            l3.append(s)
                        s = s + 1    
                    x = max(l3) - min(l3)
                    results.append(x)    
                    l3.clear()
                    s = 0
                    
            maximo = max(results)
            print(maximo)
        else:
            print('String too long')
    else:
        print('Only lowercase please')
    
        
    
            
