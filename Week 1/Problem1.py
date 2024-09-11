#PART A
def cube(n):
    return n**3

num = 3

cube = cube(num);

print(f"Cube is {cube}")


#PART B
def factorial(n):
    if n<0:
        return 'Number must be positive'
    if n==0:
        return 1
    
    return n * factorial(n-1)


print(factorial(3))



#PART C
def findAlphabeticallyLastWord(n):
    a  =  n.split(' ')
    a.sort()
    return a[-1]


print(findAlphabeticallyLastWord("What is the last word in this sentence"))



#PART D
def count_pattern(pattern , list):
    
    length = len(pattern)
    count = 0
    idx =0 
    for i in list:
        
        if pattern == list[idx:length+idx]:
            count = count+1
        
        
        idx = idx+1
            
       
                
    return count
                
           


print(count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))
print(count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')))   