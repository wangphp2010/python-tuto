import tensorflow as tf

import numpy as np 

# create data 
x_data = np.random.rand(100).astype(np.float32)
# astype函数用于array中数值类型转换  

y_data = x_data *0.1 + 0.3

### create tensorflow structure start ### 

Weights = tf.Variable(tf.random_uniform([1] , -1.0 , 1.0 )) # 初始值坐标 -1 , 1 

biases = tf.Variable(tf.zeros([1]) ) # 定义初始值 0 

y = Weights* x_data + biases # 定义预测的y


loss = tf.reduce_mean(tf.square(y-y_data) ) #计算y与要求的y的差

optimizer = tf.train.GradientDescentOptimizer(0.5) # 建立优化器 0.5 代表学习效率 ,一般为小于1的数
train = optimizer.minimize(loss) # 让优化器减少loss

init = tf.global_variables_initializer() 


### create tensorflow structure end ###


sess = tf.Session()
sess.run(init) # 激活 init 


for step in range(201):
    sess.run(train)
    if step % 20 == 0 :
        print(step , sess.run(Weights) , sess.run(biases) )
        
        
     