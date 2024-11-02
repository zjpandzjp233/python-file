import numpy as np
import matplotlib.pyplot as plt
def test():
    print(np.array([1.,2.,3.]).dtype) # float64 自建指定的浮点类的数据类型的数组
    print(np.array([1.,2.,3.],dtype=float).dtype) # float64
    print(np.arange(10)) # [0 1 2 3 4 5 6 7 8 9]

    print(np.arange(10)**2) # [ 0  1  4  9 16 25 36 49 64 81]

    print(np.arange(10)+np.arange(10)) # [ 0  2  4  6  8 10 12 14 16 18]

    # numpy的array只能用一种类型的数据
    """
    array的属性
    ·shape：返回一个元组，表示array的维度
    ·ndim:一个数字，表示array的维度的数目
    ·size：一个数字表示array中所有数兀素的数目
    ·dtype：array中元素的数据类型

    """
    array2 = np.array([1,2,3,4,56])
    print(len(array2)) #5 len里面如果是一维数组，返回元素个数，二维数字返回行数
    m1=np.array(
        [[1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]]
    )

    m3 = np.array([
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11, 12]]
    ])


    print (m1)
    """
    [[ 1  2  3]
    [ 4  5  6]
    [ 7  8  9]
    [10 11 12]]
    """

    print(m1.shape)
    print(m1.ndim) # 它是一个二维数组（也称为矩阵），因为它由多个一维数组组成，每个一维数组代表矩阵的一行。
    print(m3.ndim)
    print(m1.size)
    print(m1.dtype)
    """
    (4, 3)
    2
    3
    12
    int64
    """
    print(np.arange(0,10,2)) # [0 2 4 6 8]
    print(np.ones(10)) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] # 默认情况下，np.ones 生成的数组元素类型是浮点数（float64）
    print(np.ones((10,3)))
    """
    [[1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]
    [1. 1. 1.]]
    """
    m4=np.array([[2,3],
                [4,5]
    ])
    print(np.ones_like(m4))
    """
    [[1 1]
    [1 1]]
    """

    # print(np.zeros_like(m4)) # 也一样 全0
    print(np.empty(5))
    print(np.empty_like(m4))
    """
    [0.e+000 1.e-323 2.e-323 3.e-323 4.e-323]
    [[2 4]
    [6 8]]
    """

    print(np.full((2,3),666))
    """
    [[666 666 666]
    [666 666 666]]
    """
    # np.full_like() 同理

    print(np.random.randn(3,3))
    """
    [[-2.1156365  -0.52361883  0.15945975]
    [-0.37919983  0.07410798 -1.66149086]
    [-0.35027301  0.28817188  2.92255012]]
    """
    """
    
    np.random.seed(6) # 随机数种子
    rand(d0, d1, ..., dn):
    创建一个指定形状的数组，其元素是从 [0, 1) 范围内的均匀分布中抽取的。
    示例：np.random.rand(3, 2)
    randn(d0, d1, ..., dn):
    创建一个指定形状的数组，其元素是从标准正态分布（均值为 0，标准差为 1）中抽取的。
    示例：np.random.randn(3, 2)
    randint(low, high=None, size=None, dtype=int):
    创建一个指定形状的数组，其元素是从 [low, high) 范围内的整数中抽取的。
    示例：np.random.randint(0, 10, size=(3, 2))
    choice(a, size=None, replace=True, p=None):
    从给定的一维数组 a 中随机抽取元素。
    示例：np.random.choice([1, 2, 3, 4, 5], size=3)
    shuffle(x):
    就地打乱一维数组 x 的顺序。
    示例：np.random.shuffle(arr)
    permutation(x):
    返回一个一维数组 x 的随机排列，或者如果 x 是一个整数，则返回 np.arange(x) 的随机排列。
    示例：np.random.permutation([1, 2, 3, 4, 5])
    """
    print(np.random.randn(3,2,4))
    """ 三行两列 每个元素是四个元素的一维数组
    [
    [[ 0.42774738 -0.61019591  0.12786103  0.22392662],[ 0.41444744 -0.90390455  0.9834124   0.84568329]]

    [[-1.86796943  0.01354836  1.01361372 -1.3544671 ],[-0.58273904 -0.77354251  0.16143327  0.29781084]]

    [[ 1.4705833  -0.71707848  1.38043479  0.06792316],[-1.29569951 -0.84001766 -0.21418446  0.04943167]]
    ]
    """

    m5=np.array([1,2,3,4,5,4])
    m6=np.ones((6))
    m7=np.array( # 相当于 一个两行一列的数组，其中这个数组的每个元素都是两行两列的数组，一个[]算作一行
        [
        [[1, 2], [3, 4]], 
        [[5, 6], [7, 8]]
        ]
    )
    print(m5.reshape(2,3))
    """
    [[1 2 3]
    [4 5 4]]
    """
    print(m5+10) # [11 12 13 14 15 14]
    print(np.sin(m5)) # [ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427 -0.7568025 ]
    print(m5+m6) # [2. 3. 4. 5. 6. 5.]
    print(m7)
    """
    [[[1 2]
    [3 4]]

    [[5 6]
    [7 8]]]
    """
    print(m7.reshape((4, 2))) # 对三维数组的reshape
    """
    [[1 2]
    [3 4]
    [5 6]
    [7 8]]
    """
    m8=np.array(
    [
    [1,5,9],
    [3,56,6],
    [453,6,2]
    ]
    )
    print('##############')
    print(m8[:,1]) # 取第二列，但结果是行的形式：[ 5 56  6]
    print(m8[[0,1],:])  # 取第一二行
    """
    [[ 1  5  9]
    [ 3 56  6]]
    """
    print(m8[[0,1],[0,1]]) # [ 1 56] 这种形式的索引会从 m8 中取出 (0, 0) 和 (1, 1) 位置的元素。

    print(m8[2,0]) # 453 取三行的第一个
    print(m8[-1,1]) # 6 取倒数第一行的第二个
    print(m8[-1])  # [453   6   2]
    print(m8[0:2,0:2]) 
    """
    [[ 1  5]
    [ 3 56]]
    """
    # 切片——局部选择原数组并修改的操作
    m8[1:3,0:2]=6666
    print(m8)
    """
    [[   1    5    9]
    [6666 6666    6]
    [6666 6666    2]]
    """

    # 数组对照表
    index=np.array([598,168,684,261,8945,3,5,48,0])
    准备映射=np.array(
        [[0,1,2],
        [3,4,5],
        [8,7,6]]
    )
    print(index[准备映射])
    """
    [[ 598  168  684]
    [ 261 8945    3]
    [   0   48    5]]
    """
    # 数组.argsort 可以排序数组，并返回序号
    print('##############')
    准备映射2=准备映射>3 # 利用True和False来筛选
    print(准备映射2)
    """
    [[False False False]
    [False  True  True]
    [ True  True  True]]
    """
    print(准备映射[准备映射2])# [4 5 8 7 6] 不是True不要


    m9=np.array(
        [[0,1,2],
        [3,4,5],
        [8,7,6]]
    )
    print(m9>2)
    """
    [[False False False]
    [ True  True  True]
    [ True  True  True]]
    """

    # 利用True和False的判断来修改数组的每个元素，类似遍历
    m9[m9>2]=3
    m9[m9<=2]=0
    print(m9)
    """ 
    [[0 0 0]
    [3 3 3]
    [3 3 3]]
    """
    m10=np.array(
        [[0,1,2],
        [3,4,5],
        [8,7,6]]
    )
    m10[m10>1]+=99
    print(m10) # 大于1的全加99
    """
    [[  0   1 101]
    [102 103 104]
    [107 106 105]]
    """

    #利用np的一维数组的True和False来选择一个数组的行和列
    print(m10[1,:]>102) # [False  True  True]
    print(m10[m10[1,:]>102]) 
    """
    [[102 103 104]
    [107 106 105]]
    """
    m10[m10[1,:]>102]=9999 # 按条件赋值
    print(m10)
    """
    [[   0    1  101]
    [9999 9999 9999]
    [9999 9999 9999]]
    """

    # 多重条件筛选数组
    m11=np.array([1,2,3,4,5,6,7,8,9,10])
    print((m11%2==0)|(m11>3)) # [False  True False  True  True  True  True  True  True  True]
    print(m11[(m11%2==0)&(m11>3)]) # [ 4  6  8 10]    |是或    &是且

    np.random.seed(65) # 随机数种子
    print(np.random.rand(10)) # [0.40247251 0.74651072 0.72407057 0.4061078  0.98937985 0.45049928 0.37380843 0.70962861 0.08245855 0.39837292]

    print(np.random.rand(2,3,4))
    """
    [
    [[0.89286015 0.33197981 0.82122912 0.04169663],[0.10765668 0.59505206 0.52981736 0.41880743],[0.33540785 0.62251943 0.43814143 0.73588211]]

    [[0.51803641 0.5788586  0.6453551  0.99022427],[0.8198582  0.41320093 0.87626766 0.82375943],[0.05447451 0.71863724 0.80217056 0.73640664]]
    ]
    """
    print(np.random.randint(1,10,size=(2,3)))
    """
    [[4 6 6]
    [3 8 9]]
    """
    print(np.random.choice(100,(2,3))) # 100等价于range(100)
    """
    [[69 70 90]
    [63 10 67]]
    """
    m12=np.array(
            [[0,1,2],
            [3,4,5],
            [8,7,6]]
        )
    np.random.shuffle(m12)
    print(m12)# 对于二维数组，默认情况下它只会打乱第一维度（即行）的顺序，而不会改变每个行内部的顺序。

    # 打乱二维数组的每一个数字
    import numpy as np
    def shuffle_and_reconstruct(array):
        # 获取原始二维数组的形状
        shape = array.shape
        # 将二维数组展平为一维数组
        flat_array = array.flatten() # 用于将多维数组转换为一维数组
        # 打乱一维数组
        np.random.shuffle(flat_array)
        # 将打乱后的一维数组重新填充回原来的二维数组形状
        shuffled_array = flat_array.reshape(shape)
        return shuffled_array
    # 示例用法
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print("原始二维数组:")
    print(array)
    shuffled_array = shuffle_and_reconstruct(array)
    print("打乱后的二维数组:")
    print(shuffled_array)
    """
    [[5 8 1]
    [6 7 9]
    [4 3 2]]
    """
    """
    注意事项
    flatten 返回的是一个新的数组，而不是原数组的视图。如果你只需要一个视图而不希望占用额外的内存，可以使用 ravel 方法，它返回的是一个视图。
    示例：使用 ravel
    python
    深色版本
    array = np.array([[1, 2, 3], [4, 5, 6]])
    flat_view = array.ravel()
    print("使用 ravel 展平后的数组:")
    print(flat_view)
    """
    # 也有log的数轴：logspace
    x=np.linspace(-10,10,100) # 一个在-10到10内的100个均匀排列的元素，一维数组
    y=np.sin(x)+np.random.rand(len(x))/10 # 第二项是噪声
    plt.plot(x,y)
    plt.show() # 画图，直角坐标系
    """
    np.sum	计算所有元素的总和
    np.prod	计算所有元素的乘积
    np.cumsum	计算元素的累积和  比如[1,2,3]-->[1,3,5]
    np.cumprod	计算元素的累积乘积
    np.min	计算最小值
    np.max	计算最大值
    np.percentile	计算0-100百分位数   
    np.quantile	计算0-1分位数
    np.median	计算中位数
    np.average	加权平均，可通过weights参数指定权重
    np.mean	计算平均值
    np.std	计算标准差
    np.var	计算方差
    """

    m13=np.array(
                [[90,1,2],
                [13,44,5],
                [8,71,6]]
            )
    print(np.percentile(m13,[20,50,90]))# [ 3.8  8.  74.8]  依次返回第0%和 50% 90% 位置的数
    # print(np.quantile(m13,[0.2,0.5,0.9]))#和上面差不多

    weights = np. random. rand(*m13.shape) # *arr.shape 是解包操作符，将 arr 的形状传递给 rand 函数。例如，如果 arr 的形状是 (3, 3)，那么 *arr.shape 相当于 3, 3。
    print(weights)
    """
    [[0.5213347  0.99726482 0.45100462]
    [0.88267209 0.53047247 0.11077855]
    [0.51011495 0.15355496 0.49296405]]
    """
    print(np. average(m13, weights=weights)) # 加权平均数 23.320944926981852

    print(m13.sum(axis=0)) # axis=0：沿着列方向求和，即对每一列的所有元素求和。axis=1：沿着行方向求和，即对每一行的所有元素求和。更高维度就axis跟着变大
    # [111 116  13]

    print(m13.sum(axis=1))
    # [93 62 85]

    bigArray=np.random.randint(100,1000,(3,3))
    print(bigArray)
    """
    [[524 357 130]
    [178 411 150]
    [721 745 112]]
    """
    smallArray=np.random.randint(1,10,(3,3))
    print(smallArray)
    """
    [[9 5 5]
    [9 1 6]
    [1 1 6]]
    """
    # 数组的标准化，方便不同单位的数组比较
    bResult=(bigArray-np.mean(bigArray,axis=0))/(np.std(bigArray,axis=0))
    sResult=(smallArray-np.mean(smallArray,axis=0))/(np.std(smallArray,axis=0))
    print(bResult,'\n',sResult)
    """
    [[ 0.22128805 -0.85859078 -0.04295368]
    [-1.32030253 -0.54390366  1.24565666]
    [ 1.09901448  1.40249445 -1.20270298]]
    
    [[ 0.70710678  1.41421356 -1.41421356]
    [ 0.70710678 -0.70710678  0.70710678]
    [-1.41421356 -0.70710678  0.70710678]]
    """

    # 求数组中满足条件的元素个数
    array3=np.array([
        [1,2,3],
        [7,8,9],
        [99,54,32]
    ])
    print(array3[array3>7].size) # 5

    # 升维度 

    arr4=np.array([1,2,3,4,5])
    print(arr4[np.newaxis,:]) # [[1 2 3 4 5]]
    print(arr4[:,np.newaxis]) 
    """
    [[1]
    [2]
    [3]
    [4]
    [5]]
    """
    print(np.expand_dims(arr4,axis=0)) #[[1 2 3 4 5]]
    #print(np.expand_dims(arr4,axis=1))  同理
    # squeeze降维

    arr5=np.array([1,2,3,4,5,6,7,8,9,10])
    array4=np.array([
            [1,2,3],
            [7,8,9],
            [99,54,32]
        ])
    print(np.reshape(arr5,(2,-1)))
    """   负一表示会自动识别
    [[ 1  2  3  4  5]
    [ 6  7  8  9 10]]
    """
    print(array4.reshape(-1)) # [ 1  2  3  7  8  9 99 54 32] 展平二维数组


    # 合并数组

    a=np.array([
        [1,2,3],
        [9,5,1]
    ])
    b=np.array([
        [5,9,2],
        [6,2,1]
    ])
    print(np.concatenate([a,b],axis=0))
    print(np.vstack([a,b]))
    """ 这两个结果一样
    [[1 2 3]
    [9 5 1]
    [5 9 2]
    [6 2 1]]
    """


    print(np.column_stack([a,b]))
    print(np.concatenate([a,b],axis=1))
    print(np.hstack([a,b]))
    """这三个结果一样
    [[1 2 3 5 9 2]
    [9 5 1 6 2 1]]
    """

    # 转置

    a=np.array([
            [1,2,3],
            [9,5,1]
        ])
    a2=np.array([
            [1,2,3],
            [9,5,1]
        ])
    a1=np.array(
            [1,2,3] # 也可以是[[1,2,3]]底下结果也一样
        )
    print(a.T)
    """
    [[1 9]
    [2 5]
    [3 1]]
    """

    # 广播
    print(a1+a)
    """
    [[ 2  4  6]
    [10  7  4]]
    """
    print(a**a2)
    """
    [[        1         4        27]
    [387420489      3125         1]]
    """


    a=np.array([
                [1,2,3],
                [9,5,1]
            ])
    arr3,index=np.unique(a,return_index=True)# 返回一个不含重复元素且排好序的数组 return_index=True会返回新的列表里的元素在原数组的列表
    print(arr3,'\n',index)
    """
    [1 2 3 5 9] 
    ,,,,,,,,,,,,,,,,,,,,,,,
    [0 1 2 4 3]
    """
    a2=np.array([
            [9,5,1],
            [1,2,3],
            [1,2,3]
        ])
    print(np.unique(a2,axis=0)) # 剔除垂直方向上的重复行
    """
    [[1 2 3]
    [9 5 1]]
    """


    # 数组的三目运算符

    a3=np.where(a2>3,a2+100,a2)
    print(a3)
    """
    [[109 105   1]
    [  1   2   3]
    [  1   2   3]]
    """

    # 矩阵乘法
    a=np.array([
        [1,2,3],
        [9,5,1]
    ])
    b=np.array([
    [1,2],
    [1,5],
    [1,1]
    ])
    print(np.dot(a,b))
    """
    [[ 6 15]
    [15 44]]
    """
    # 索引
    print(a[1,2]) # 索引到第二行的第三个元素 

    m333=np.array([[[1,5,9],
                    [2,4,8],
                    [5,2,1]],
                    [[1,2,6],
                    [5,8,6],
                    [5,9,6]],
                    [[8,9,1],
                    [4,6,3],
                    [8,4,6]]
    ])

    print(m333[0,1,1]) # 4

    # 高位数组切片
    print(m333[:,1,0]) #[2 5 4]
    print(m333[0,:,:])
    """
    [[1 5 9]
    [2 4 8]
    [5 2 1]]
    """
    print(m333[:,1,:])
    """
    [[2 4 8]
    [5 8 6]
    [4 6 3]]
    """
    print(m333[...,0])
    # 等价于 print(m333[:,:,0])
    """
    [[1 2 5]
    [1 5 5]
    [8 4 8]]
    """
    m333=np.array([[[1,5,9],
                    [2,4,8],
                    [5,2,1]],
                    [[1,2,6],
                    [5,8,6],
                    [5,9,6]],
                    [[8,9,1],
                    [4,6,3],
                    [8,4,6]]
    ])
    print(m333[:2,1:3,0:2])
    """
    [[[2 4]
    [5 2]]

    [[5 8]
    [5 9]]]
    """



    # 假设X是特征矩阵，y是标签向量
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])

    # 获取一个随机排列的索引列表
    indices = np.random.permutation(X.shape[0])
    print(X.shape[0])



    # 创建一个示例矩阵
    A = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    # 执行 SVD 分解
    U, s, VT = np.linalg.svd(A)

    # 输出结果
    print("U:")
    print(U)
    print("\nΣ (奇异值):")
    print(s)
    print("\nV^T:")
    print(VT)




    # 创建示例数据
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([0, 2, 4, 3, 2, -1])

    # 选择多项式的阶数
    degree = 2
    """
    不同阶数的比较
    一次多项式 (degree = 1)：直线拟合。
    二次多项式 (degree = 2)：抛物线拟合。
    三次多项式 (degree = 3)：立方曲线拟合。
    选择合适的阶数取决于你的数据特性和拟合需求。更高的阶数可以更好地拟合复杂的数据，但也可能导致过拟合（即模型过于复杂，对噪声敏感）。
    """
    # 执行多项式拟合
    coefficients = np.polyfit(x, y, degree)

    # 输出拟合得到的多项式系数
    print("多项式系数:", coefficients)

    # 使用拟合的多项式计算新的 y 值
    y_fit = np.polyval(coefficients, x)

    # 绘制原始数据点和拟合曲线
    plt.scatter(x, y, label='raw')
    plt.plot(x, y_fit, label='curve', color='red')
    plt.legend()
    plt.show()



    # numpy 数组保存到文件
    # 创建一个示例数组
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # 保存数组到文件
    np.save('array.npy', arr) # 支持高纬度
    # 加载数组从文件
    loaded_arr = np.load('array.npy')

    # 输出加载的数组
    print(loaded_arr)


    # 创建一个示例数组
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # 保存数组到文本文件
    np.savetxt('array.txt', arr, fmt='%g', delimiter=',')# 仅仅支持二维
    """
    1. 固定格式
    整数：
    fmt='%d'：输出整数。
    fmt='%i'：输出整数（等同于 %d）。
    fmt='%ld'：输出长整数。
    fmt='%lld'：输出长长整数。
    浮点数：
    fmt='%.f'：输出浮点数，不显示小数部分。
    fmt='%.1f'：输出浮点数，保留一位小数。
    fmt='%.2f'：输出浮点数，保留两位小数。
    fmt='%.3f'：输出浮点数，保留三位小数。
    fmt='%.6f'：输出浮点数，保留六位小数。
    科学记数法：
    fmt='%.2e'：输出浮点数，保留两位小数，使用科学记数法。
    fmt='%.2E'：输出浮点数，保留两位小数，使用大写的科学记数法。

    %g：自动选择最合适的格式（浮点数或科学记数法）。
    %s：字符串。
    """

    # 加载数组从文本文件
    loaded_arr = np.loadtxt('array.txt', delimiter=',')

    # 输出加载的数组
    print(loaded_arr)





# Numpy的结构化数组
# 定义结构化数组的数据类型
dt = np.dtype([('name', 'S10'), ('age', 'i4'), ('height', 'f8')])

# 创建结构化数组
data = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0), ('Charlie', 22, 5.8)], dtype=dt)

# 输出结构化数组
print(data) # [(b'Alice', 25, 5.5) (b'Bob', 30, 6. ) (b'Charlie', 22, 5.8)]
# 访问 'name' 字段
names = data['name']
print(names) #[b'Alice' b'Bob' b'Charlie']

# 访问 'age' 字段
ages = data['age']
print(ages) # [25 30 22]

# 访问 'height' 字段
heights = data['height']
print(heights) # [5.5 6.  5.8]

from numpy.lib.recfunctions import append_fields

# 添加一个新的字段 'weight'
new_data = append_fields(data, 'weight', [65.0, 70.0, 68.0], usemask=False, asrecarray=True)
#：使用 numpy.lib.recfunctions.append_fields 添加新字段。注意参数 usemask=False 和 asrecarray=True，这些参数确保返回的结果是一个普通的 NumPy 结构化数组。

# 输出新的结构化数组
print(new_data,'###########') # [(b'Alice', 25, 5.5, 65.) (b'Bob', 30, 6. , 70.) (b'Charlie', 22, 5.8, 68.)]
from numpy.lib.recfunctions import drop_fields

# 删除 'height' 字段
new_data = drop_fields(data, 'height')

# 输出新的结构化数组
print(new_data) # [(b'Alice', 25) (b'Bob', 30) (b'Charlie', 22)]

# 按 'age' 字段排序
sorted_data = np.sort(data, order='age')

# 输出排序后的结构化数组
print(sorted_data) # [(b'Charlie', 22, 5.8) (b'Alice', 25, 5.5) (b'Bob', 30, 6. )]

# 筛选出年龄大于25的人
filtered_data = data[data['age'] > 25]

# 输出筛选后的结构化数组
print(filtered_data) # [(b'Bob', 30, 6.)]
