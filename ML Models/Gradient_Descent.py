import random
import numpy as np

def loss(w, points , i):
    x, y = points[i]
    return ((np.dot(w, np.array(x)) - y)**2)/len(points)



def slope(w, points):
    return sum(2 * (np.dot(w, np.array(x)) - y) * np.array(x) for x, y in points) / len(points)



    
true_weights = [7,2,3,4,1]
noise = 3


def generate_data():   
    for i in range(5):
        x = [random.randint(1, 50) for _ in range(5)]
        y = sum(w * xi for w, xi in zip(true_weights, x)) + noise
        points.append((x,y))
        
points = []
generate_data()



w = np.array([0,0,0,0,0])
alpha = 0.001


# for i in range(10001):
#     gradient = slope(w,points)
#     w = w - alpha*gradient
#     f = loss(w,points)
    
#     print(f'Iter={i} , w={w} , loss={f}')
   
for t in range(10):
    for i in range(len(points)):
        value = loss(w, points,i)
        gradient = slope(w, points)
        w = w - alpha * gradient
        print(f'epoch {t}: w = {w}, F(w) = {value}, gradientF = {gradient}')