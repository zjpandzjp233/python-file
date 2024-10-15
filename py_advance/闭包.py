import ATM

# ATM.begin_money=99 # 可修改包内变量
# print(ATM.begin_money)

my_atm=ATM.ATMs(1000) 
my_atm(3000) # 你刚刚存入：3000,你现在拥有的存款共为：4000。
my_atm(2000) # 你刚刚存入：2000,你现在拥有的存款共为：6000。
my_atm(1000) # 你刚刚存入：1000,你现在拥有的存款共为：7000。