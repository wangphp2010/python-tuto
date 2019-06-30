# pytest - 自动化测试工具,
'''
# 一般测试

def add(x,y):
    return x+y
    
def test1():
    assert 2 == add(1,1)
    
def test2():
    assert 1 != add(1,1)

测试   test_func.py  
$ pytest -vv test_func.py 

测试所有文件
$ pytest

'''


#测试抛出异常
'''

import pytest

def func(x):
    if x == 0:
        raise ValueError('my value error')
    else:
        pass

#func(0)


def test_mytest1():
    with pytest.raises(ValueError):
        func(0)
        
def test_mytest2():
    assert func(1) == None
    
    
#$ pytest -vv
                
 '''       
        
#不同参数传递测试 为同一个函数传递不同参数测试
'''
def add(x,y):
    return x+y
    
import pytest

@pytest.mark.parametrize(
    "x,y,expeted",
    [
        (1,1,2),
        (2,2,4),
        (10,10,20),
    
    ]

)

def test_add(x,y,expeted):
    assert add(x,y) == expeted

'''


# 分组测试

'''
$ pytest --markers 查看指令

建立 pytest.ini 他的内容
    [pytest]
    markers = 
        g1:group1.
        g2:group2.
 '''   


import pytest


@pytest.mark.g1
def test_func1():
    pass

        
@pytest.mark.g2
def test_func2():
    pass
        
        
        
@pytest.mark.g1
def test_func3():
    pass

        
@pytest.mark.g2
def test_func4():
    pass
        
@pytest.mark.g1
def test_func5():
    pass       
        
        
        
'''
$ pytest -vv 
$ pytest -vv -m g1
$ pytest -vv -m g2

'''        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        