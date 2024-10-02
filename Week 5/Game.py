import random
import matplotlib.pyplot as plt
from collections import Counter

def game():
    
    count = 0
    results = []
        
    while count != 1000:
        prize = 0
        number = random.randint(1, 6)
        while number !=1 and number!=2:
            prize = prize+4
            number = random.randint(1, 6)
        results.append(prize)
        count = count+1
    return results


res = game()

value_counts = Counter(res)


values = list(value_counts.keys())
occurrences = list(value_counts.values())


plt.bar(values, occurrences)


plt.xlabel('Values')
plt.ylabel('Occurrences')
plt.title('Occurrences of Each Value')

max_value = max(values)
plt.xticks(range(0, max_value + 1, 4)) 


plt.show()