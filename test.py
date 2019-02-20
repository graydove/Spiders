import matplotlib.pyplot as plt
from pylab import *    #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


p = [inf, 2.0153, 1.8163, 1.7394, 1.6818, 1.6586, 1.6180, 1.6118, 1.6000, 1.5715, 1.5574,
     1.5438, 1.5382, 1.5201, 1.5117, 1.5028, 1.4890, 1.4781, 1.4649, 1.4517, 1.4393,
     1.4270, 1.4150, 1.3992, 1.3955, 1.3942, 1.3811, 1.3608, 1.3491, 1.3219, 1.3083]
m = [inf, 2.4501, 2.0779, 2.1307, 2.0082, 1.9936, 1.8801, 1.9678, 2.2192, 2.0440, 1.8301,
     1.9005, 1.8939, 1.8096, 1.8074, 1.8176, 1.8229, 1.8182, 1.8337, 1.8144, 1.8294,
     1.8125, 1.8321, 1.8240, 1.8067, 2.0346, 1.9209, 1.9005, 1.8496, 1.9085, 2.0488]
x = [i for i in range(0, 31)]
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
          'size'   : 12,
        }
#设置坐标轴的刻度值
x_ticks = np.linspace(0, 30, 7)
plt.xticks(x_ticks)
y_ticks = np.linspace(0, 4, 21)
plt.yticks(y_ticks)
# cross_line = (5/9)* x_ticks
# plt.plot(p, cross_line, '-.g', label=u'Chance', linewidth=1.2)  #画对角线

plt.plot(x, p, marker="*", label=u'Train')
plt.plot(x, m, marker="*", label=u'Valid')
plt.legend()
plt.xlabel(u"Epoch", font1)
plt.ylabel("Cross-entropy Loss", font1)
plt.title("DenseNet201 in AVA_tag", font1)
plt.margins(0)  #横坐标和纵坐标没有空余
plt.grid(True, linestyle="--")   #设置网格线为虚线
plt.axis("tight")
plt.show()

result_str = []

