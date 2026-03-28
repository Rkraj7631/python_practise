'''
def rev(str):
    str1=str[::-1]
    print(str1)

rev("suraj")
'''

'''
def reverse_string(s):
    result=""
    for char in s:
        result=char+result
    return result
print(reverse_string("kumar"))
'''
'''
def str_pal(s):
    if(s==s[::-1]):
       print("string is pallindrome")
    else:
        print("string is not pallindrome")
str_pal("madam")
str_pal("suraj")
'''
'''
def count_cv(s):
    vowels="aeiou"
    v=0
    c=0
    s=s.lower().strip()
    for char in s:
        if char.isalpha():
            if char in vowels:
                v+=1
            else:
                c+=1
    print(f"vowels={v}in{s}")
    print(f"constant={c} in {s}")

count_cv("suraj kumar")
'''
'''
def count_words(s):
    str=s.strip().split()
    word=len(str)
    print(word)

count_words("suraj kumar")
'''

'''
def remove_space(s):
    str=s.replace(" ","")
    print(str)
remove_space("suraj kumar raj")
'''
'''
def fre_char(s):
    for i in range(len(s)):
        print(f"{i}-{s[i]}")
fre_char("suraj")
'''

'''
def char_frequency(s):
    freq={}
    for ch in s:
        if ch !=" ":
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
    print(freq)
char_frequency("suraj kumar")
'''

'''
def first_char(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i]==s[j]:
                return(s[i])
print(first_char("suraj kumar"))
'''

'''
def anargms(s):
    str=s.split()
    if (sorted(str[0])==sorted(str[1])):
        print("string is anagrams")
    else:
        print("string is not anagrams")

anargms(input("emter two word string : "))    
'''

'''
def replace_space(str):
    return str.replace(" ", "-")
print(replace_space("suraj kumar raj"))
'''

'''
def remove_duplicate(str):
    result=[]
    for i in str:
        if i not in result:
            result.append(i)
    print(result)
remove_duplicate("surajkumar")
'''

'''
def longest_word(sen):
    word=sen.split()
    long=""
    print(word)
    for words in word:
        if len(words)>len(long):
            long=words
    return long
print(longest_word("suraj kumar is learning python programming"))
'''
'''
def capital_first(s):
    word=s.split()
    result=[]
    for i in word:
        str1=i[0].upper()+i[1:]
        result.append(str1)
    return " ".join(result)
print(capital_first("suraj kumar is learning python programming"))
'''
'''
def largest_ele(num):
    largest_number=0
    for i in num:
        if i>largest_number:
            largest_number=i
    return largest_number
print(largest_ele([10,2,3,4,5,650,0,120,12,651,321,321,51653]))
'''

'''
def second_large(num):
    large=0
    second_large=0
    for i in range(len(num)):
        if num[i]>large:
            second_large=large
            large=num[i]
        elif (num[i]>large and num[i]!=second_large):
            second_large=num[i]
            
    print(large)
    return second_large
print(second_large([4654,5165,151,215]))
'''
'''
def remove_dup(s):
    result=[]
    for i in range(len(s)):
        if s[i] not in result:
            result.append(s[i])
    return result

print(remove_dup([5,55,15,15,5,6,1,52,565,165,465,465,45,21]))
'''
'''
def sort_list(s):
    n=len(s)
    print(n)
    for i in range(n):
        for j in range(0,n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    print(s)
sort_list([2,56,1,0,65])
'''
'''
a=[2,4,6,2]
b=[1,1,2,12,15]
a.extend(b)
print(a)
'''
'''
a=[2,4,2,551,21,151]
b=[5,8,121,31,32,31,2,1,11,1]

result=[]
for i in a:
    if i in b:
        result.append(i)
print(result)
'''

'''
def rev_list(lst):
  #lst1=lst[::-1]
    #return lst1  
    result=[]
    n=len(lst)
    for i in range(n-1,-1,-1):
        result.append(lst[i])
    return result
print(rev_list([2,5,1,5,1,5,32,2]))
'''
'''
def freq_list(lst):
    result={}
    for i in lst:
        if i in result:
            result[i]+=1
        else:
            result[i]=1
    return result
print(freq_list([1,5,1,5,1,2,1,3,8,2,6,5,5,5,1,2,5,2,1,6,5,8,7,5,8,7,4,6,]))
'''
'''
def miss_num(lst):
    n=lst[-1]
    total=n*(n+1)//2
    actual=sum(lst)
    return total-actual
print(miss_num([1,2,3,4,5,6,8,9]))
'''
'''
def dup_ele(lst):
    result=[]
    duplicate=[]
    for i in lst:
        if i not in result:
            result.append(i)
        elif i in result:
            duplicate.append(i)
    return result and duplicate
print(dup_ele([1,5,1,5,1,2,1]))
'''
'''
lst=[1,5,1,5,1,2,1,4]
result=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] == lst[j]and lst[i] not in result:
            result.append(lst[i])
print(result)
'''
'''
def find_pair(arr,target):
    result=[]
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target :
                result.append((arr[i],arr[j]))

    return result
print(find_pair([1,3,-2,5,2,4,-2,6,0],6))
'''
'''
def move_end(lst):
    n=len(lst)
    result=[]
    count=0
    for i in range(n):
        if lst[i]==0:
            count+=1
        else:
            result.append(lst[i])
    result.extend([0]*count)
    return result
print(move_end([2,0,3,4,0,6,4,0]))
'''
'''
def sep_evenodd(lst):
    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even Number in list = {even} \nOdd Number in list = {odd}")

sep_evenodd([45,154,2,54,2,154,1,5465,12,541,2,54])
'''
'''
def max_sum(lst):
    max=0
    add=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst),1):
            max_add=lst[i]+lst[j]
            if max_add > max:
                max=max_add

    return max
print(max_sum([5,10,2,4,6]))
'''

'''
def flatten(lst):
    result=[]
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1, [10, 3], [4, [5, 6]]]))
'''
'''
def check_pallindrome(lst):
    if (lst==lst[::-1]):
        print("list is pallindrome")
    else:
        print("list is not pallindrome")

check_pallindrome([1,2,1])
check_pallindrome(["m","a","d","a","m"])
check_pallindrome(["m","a","s","t","m"])
'''
'''
def self_pro(lst):
    result=[]
    for i in range(len(lst)):
        prod=1
        for j in range(len(lst)):
            if i !=j:
                prod=prod*lst[j]
        result.append(prod)
    return result
print(self_pro([2,5,1,0]))
'''

'''
def lst_chunk(lst,value):
    result=[]
    for i in range(0,len(lst),value):
        result.append(lst[i:i+value])

    return result
print(lst_chunk([1,5,3,31,5,1,2],2))
'''

'''

def majority_ele(lst):
    count=0
    candidate=None

    for num in lst:
        if count==0:
            candidate=num

        if num == candidate:
            count+=1

        else:
            count -=1

    if lst.count(candidate)> len(lst)//2:
        return candidate
    return "No Majority Element"


print(majority_ele([5,2,1,5,5,5,5,1,45,21,5,12,35,1,2]))
        
'''
'''
def majority_ele(lst):
    result={}
    for i in lst:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1

    n=len(lst)
    for key,val in result.items():
        if val >n//2:
            return key
        print(result)
        return "NO Majority Element"

    


print(majority_ele([5,2,1,5,4,5,2,1,5,1,2,3,5,1,2]))
'''

'''
import random
def shuffle_lst(lst):
    random.shuffle(lst)
    print(lst)

shuffle_lst([2,15,12,1,1215,2])
'''

'''
def freq_ele(dict):
    result={}
    for i in dict:
        if i not in result:
            result[i]=1
        else:
            result[i]+=1
    return result
print(freq_ele({12,1,5,13,15,1,212,1,12,1}))
'''
'''
def merge_dict(dict1,dict2):
    dict1.update(dict2)
    print(dict1)

merge_dict({10:1,2:4,3:2,4:5},{5:6,1:2,3:5,5:6})
'''           
'''
def sort_dict(d):
    keys=list(d.keys())

    for i in range(len(keys)):
        for j in range(0,len(keys)-i-1):
            if keys[j]>keys[j+1]:
                keys[j], keys[j+1]=keys[j+1],keys[j]

    result={}
    for k in keys:
        result[k] = d[k]

    return result
print(sort_dict({"a":2,"b":5,"z":1,"s":4,"x":5}))
'''
'''
def sort_dict(d):
    values=list(d.items())

    for i in range(len(values)):
        for j in range(0,len(values)-i-1):
            if values[j][1]>values[j+1][1]:
                values[j],values[j+1]=values[j+1],values[j]
    result={}
    for k,v in values:
        result[k]=v

    return result
print(sort_dict({"a":2,"b":5,"z":1,"s":4,"x":5}))
'''
'''
def check_key(d):
    
    a=input("enter a stirng : ")
    if a in d.keys():
        print("value match")
    else:
        print("value does not match")
    
check_key({"a":2,"b":5,"z":1,"s":4,"x":5})
'''
'''
def check_key(d):
    
    a=input("enter a stirng : ")
    if a in d:
        d.pop(a)
        print(d)
    else:
        print("keys not found")
    
check_key({"a":2,"b":5,"z":1,"s":4,"x":5})
'''
'''
def find_key(dict):
    max_key=None
    max_value=0
    for i,j in dict.items():
        if j > max_value:
            max_value=j
            max_key=i
    print("maximum value:", max_value)
    print("maximum key :", max_key)
        
find_key({"a":2,"b":1,"d":4,"y":10,"c":2})
'''                
'''
def find_key(dict):
    min_value=float("inf")
    min_key=None
    for i, j in dict.items():
        if j < min_value:
            min_value=j
            min_key=i
    print("minimum value :", min_value)
    print("minimum key :", min_key)
        

find_key({"a":2,"b":1,"d":4,"y":10,"c":2})
'''
'''
def invert_dict(dict):
    result={}
    for i, j in dict.items():
        result[j]=i
    return result

print(invert_dict({"a":2,"b":1,"d":4,"y":10,"c":2}))
'''
'''
def count_ch(str):
    result={}
    for i in str:
        if i in result:
            result[i]+=1
        else:
            result[i]=1

    return result
print(count_ch("raja ram mohan rai"))
'''
'''
def combine_value(dict):
    result={}
    for i in dict:
        if i in result:
            result[i]

{'r': 3, 'a': 5, 'r': 1, 'm': 2, 'a': 1, 'h': 1, 'm': 1, 'i': 1}
'''
'''
def star(n):
    for i in range(0,n+1,1):
        print("*"*i)

star(int(input("enter a number :")))
'''
'''
def star(n):
    for i in range(n,0,-1):
        print("*"*i)

star(int(input("enter a number :")))
'''
'''
def star(n):
    for i in range(0,n+1,1):
        print(" "*(n-i)+"*"*(2*i-1))

star(int(input("enter a number :")))
'''
'''
def star(n):
    for i in range(0,n+1,1):
        print(" "*(n-i)+"*"*(2*i-1))

    for j in range(n-1,0,-1):
        print(" "*(n-j) + "*"*(2*j-1))

star(int(input("enter a number :")))
'''

'''
def star(n):
    for i in range(1,n+1):
        for j in range(1,2*n,1):
            if j==n-i+1 or j==n+i-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(n-1,0,-1):
        for j in range(1,2*n):
            if j== n-i+1 or j==n+i-1 :
                print("*", end="")
            else:
                print(" ", end="")
        print()

star(int(input("enter a number :")))    

'''

def triangele(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(j,end="")
        print()
triangele(int(input("enter a number : ")))







        
    
