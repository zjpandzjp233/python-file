from typing import Callable

# begin_money=0 # 在包内定义全局变量容易被误操作修改导致程序错误

# 以下的Initial_deposit_for_account_opening则不可能被误操作修改

def ATMs(Initial_deposit_for_account_opening:int) -> Callable[[int], None]: 
    """
    Initial_deposit_for_account_opening:开户时存进去的钱
    """
    Current_money=Initial_deposit_for_account_opening
    def deposit_the_money_into_the_bank(num:int)->None:
        """
        num:存款金额
        """
        nonlocal Current_money# nonelocal保证可以引用并修改这些值，并且上一层函数的临时变量也会一直像全局变量一样存在着
        Current_money=Current_money+num
        print(f'你刚刚存入：{num},你现在拥有的存款共为：{Current_money}。')
    return deposit_the_money_into_the_bank

msg='今天天气真不错。'.encode("UTF-8")
print(msg)