'''
import matplotlib.pyplot as plt

x = [1,3,6,9]
y = [5,7,5,10]

plt.plot(x,y,color = 'r')

plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

random_x = np.linspace(0,1,10) #从0到1返回10个等差数
random_y = np.random.randint(10,20,10) #从[10,20)中取10个随机整数

plt.plot(random_x,random_y,color = 'r',label = "radom_demo1")

plt.xlabel('this is for X value') #X轴标签
plt.ylabel('this is for Y value') #Y轴标签
plt.title("this is random demo!!!") #标题

plt.legend() #显示图例

plt.show()
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2 * x +1
y2 = x ** 2 #x的平方

plt.plot(x,y1,color = 'g',label = "demo1",linewidth = '5.0') #label设置图例；linewidth加宽显示
plt.plot(x,y2,color = 'r',label = "demo2",linestyle = '--') #linestyle显示为虚线

plt.xlabel('this is for X value') #X轴标签
plt.ylabel('this is for Y value') #Y轴标签
plt.title("this is random demo!!!") #标题

plt.legend() #显示图例

plt.show()
