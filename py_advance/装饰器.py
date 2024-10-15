

def patch(original_function):
    def inner():
        print('Patch for the original function, needs to be added before the original function.')
        original_function()
    return inner

def patch2(original_function):
    def inner():
        original_function()
        print('Patch for the original function, needs to be added after the original function.')
        print('Function has finished executing.')
    return inner

# 给原函数加补丁
# 在使用多个装饰器时，装饰器的执行顺序是从下到上的。也就是说，离目标函数最近的装饰器会最先执行。
@patch2
@patch
def original_function():
    print('Implementation of some basic requirements')

original_function()