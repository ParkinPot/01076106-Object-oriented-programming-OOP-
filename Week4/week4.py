class User:
    def __init__(self, citizen_id: str, name: str):
        self.__citizen_id = citizen_id
        self.__name = name
        self.__accounts = []

    def get_citizen_id(self):
        return self.__citizen_id
    
    def get_name(self):
        return self.__name
    
    def get_accounts(self):
        return self.__accounts
    
    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
        else:
            return "Error"
    
class Account:
    def __init__(self, account_number: str, atm_card: str, card_pin: str, balance : float):
        self.__account_number = account_number
        self.__atm_card = atm_card
        self.__card_pin = card_pin
        self.__balance = balance
        self.__transactions = []

    def get_account_number(self):
        return self.__account_number
    
    def get_atm_card(self):
        return self.__atm_card

    def get_card_pin(self):
        return self.__card_pin
    
    def get_balance(self):
        return self.__balance
    
    def get_transactions(self):
        return self.__transactions
    
    def print_transactions(self):
        for transaction in self.__transactions:
            print(f"Type: {transaction.get_type()}, Amount: {transaction.get_amount()}, Transfer Account: {transaction.get_transfer_account_number()}")    
    # TODO 3
    def deposit(self, atm_machine, amount: float):
        if amount <= 0 or not isinstance(atm_machine, ATMMachine):
            return "Error"
        
        self.__balance += amount
        self.__transactions.append(Transaction("D", amount, atm_machine.get_machine_id(), None))
        return "Success"

    # TODO 4
    def withdraw(self, atm_machine, amount: float, max_withdraw_limit: float):
        if amount <= 0:
            return "Error"

        if amount > self.__balance:
            return "Error"

        if amount > max_withdraw_limit:
            return "Error"

        if not isinstance(atm_machine, ATMMachine):
            return "Error"

        self.__balance -= amount
        self.__transactions.append(Transaction("W", amount, atm_machine.get_machine_id(), None))
        return "Success"
    
    # TODO 5
    def transfer_to(self, atm_machine, target_account, amount: float):
        if amount <= 0 or self.__balance < amount:
            return "Error"
        
        if not isinstance(target_account, Account):
            return "Error"
        
        if not isinstance(atm_machine, ATMMachine):
            return "Error"
        
        self.__balance -= amount
        self.__transactions.append(Transaction("TW", amount, atm_machine.get_machine_id(), target_account.get_account_number()))

        target_account.__balance += amount
        target_account.get_transactions().append(Transaction("TD", amount, atm_machine.get_machine_id(), self.get_account_number()))

        return "Success"
        
class ATMCard:
    def __init__(self, card_number: str, account: Account, pin: str):
        self.__card_number = card_number
        self.__pin = pin
        self.__account = account
        self.__annual_fee = 150
        self.__max_withdraw_limit = 40000

    def get_account(self):
        return self.__account

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin

    def get_annual_fee(self):
        return self.__annual_fee

    def get_max_withdraw_limit(self):
        return self.__max_withdraw_limit
    
class ATMMachine:
    def __init__(self, machine_id: str, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__initial_amount = initial_amount
        pass# Class Code

    def get_machine_id(self):
        return self.__machine_id
    
    def get_balance(self):
        return self.__initial_amount
    
    # TODO 2
    def insert_card(self, bank, atm_card: ATMCard, pin: str):
        if not isinstance(bank, Bank):
            return None
        for user in bank.get_users():
            for account in user.get_accounts():
                if account.get_account_number() == atm_card.get_account().get_account_number():
                    if atm_card.get_pin() == pin:
                        return account
        return None
    
    # TODO 3
    def deposit_atm(self, account, amount: float):
        if amount <= 0:
            return "Error"
                 
        deposit_status = account.deposit(self, amount)

        if deposit_status == "Success":
            self.__initial_amount += amount
            return "Success"
        else:
            return "Error"
        
    # TODO 4
    def withdraw(self, account, amount: float, atm_card: ATMCard):
        if amount > self.__initial_amount:
            return "Insufficient Funds"
            
        withdraw_status = account.withdraw(self, amount, atm_card.get_max_withdraw_limit())
        
        if withdraw_status == "Success":
            self.__initial_amount -= amount
            return "Success"
        else:
            return "Error"
    
    # TODO 5
    def transfer_atm(self, account, target_account, amount: float):
        if amount < 0:
            return "Error"
        
        transfer_status = account.transfer_to(self, target_account, amount)

        if transfer_status == "Success":
            return "Success"
        else:
            return "Error"

class Bank:
    def __init__(self):
        self.__atms = []
        self.__users = []
    
    def add_atms(self, atm: ATMMachine):
        self.__atms.append(atm)

    def add_users(self, user: User):
        self.__users.append(user)

    def get_atm(self, atm_id: str):
        for atm in self.__atms:
            if atm.get_machine_id() == atm_id:
                return atm
        return None
    
    def get_users(self):
        return self.__users
    

class Transaction:
    def __init__(self, type : str, amount : float, atm_id : str, transfer_account_number : str):
        self.__type = type
        self.__amount = amount
        self.__atm_id = atm_id
        self.__transfer_account_number = transfer_account_number

    def get_type(self):
        return self.__type
    
    def get_amount(self):
        return self.__amount
    
    def get_atm_id(self):
        return self.__atm_id
    
    def get_transfer_account_number(self):
        return self.__transfer_account_number


##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM ]}
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','1234',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','1234',1000]}

atm ={'1001':1000000,'1002':200000}
# TODO 1 : จากข้อมูลใน user ให้สร้าง instance โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

bank = Bank()

user_1 = User('1-1101-12345-12-0', 'Harry Potter')
user_1.add_account(Account('1234567890', '12345', '1234', 20000))
user_2 = User('1-1101-12345-13-0', 'Hermione Jean Granger')
user_2.add_account(Account('0987654321', '12346', '1234', 1000))

atm_1 = ATMMachine('1001', 1000000) 
atm_2 = ATMMachine('1002', 200000)

bank.add_users(user_1)
bank.add_users(user_2)
bank.add_atms(atm_1)
bank.add_atms(atm_2)

atm_card_1 = ATMCard('12345', user_1.get_accounts()[0], '1234')
atm_card_2 = ATMCard('12346', user_2.get_accounts()[0], '1234')


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) atm_card เป็นหมายเลขของ atm_card 3) pin
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM




# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0



#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

atm_machine = bank.get_atm('1001'); 
account = atm_machine.insert_card(bank, atm_card_1, '1234'); 
print(f"{account.get_account_number()}, {atm_card_1.get_card_number()}, Success" if account else "Invalid card or PIN")
print()

# # Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# # ให้เรียกใช้ method ที่ทำการฝากเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# # Hermione account before test : 1000
# # Hermione account after test : 2000

atm_machine = bank.get_atm('1002'); 
account = atm_machine.insert_card(bank, atm_card_2, '1234'); 
balance_before = account.get_balance(); atm_machine.deposit_atm(account, 1000); 
print(f"Hermione account before test: {balance_before}")
print(f"Hermione account after test: {account.get_balance()}")
print()

# # Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# # ผลที่คาดหวัง : แสดง Error

atm_machine = bank.get_atm('1002'); 
account = atm_machine.insert_card(bank, atm_card_2, '1234'); 
result = atm_machine.deposit_atm(account, -1); 
print(result)
print()

# # Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# # ให้เรียกใช้ method ที่ทำการถอนเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# # Hermione account before test : 2000
# # Hermione account after test : 1500

atm_machine = bank.get_atm('1002'); 
account = atm_machine.insert_card(bank, atm_card_2, '1234'); 
balance_before = account.get_balance(); atm_machine.withdraw(account, 500, atm_card_2); 
print(f"Hermione account before test: {balance_before}")
print(f"Hermione account after test: {account.get_balance()}")
print()

# # Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# # ผลที่คาดหวัง : แสดง Error

atm_machine = bank.get_atm('1002'); 
account = atm_machine.insert_card(bank, atm_card_2, '1234'); 
result = atm_machine.withdraw(account, 2000, atm_card_2); 
print(result)
print()

# # Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# # ให้เรียกใช้ method ที่ทำการโอนเงิน
# # ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# # Harry account before test : 20000
# # Harry account after test : 10000
# # Hermione account before test : 1500
# # Hermione account after test : 11500

atm_machine = bank.get_atm('1002'); 
account_harry = atm_machine.insert_card(bank, atm_card_1, '1234'); 
account_hermione = atm_machine.insert_card(bank, atm_card_2, '1234'); 
balance_harry_before = account_harry.get_balance(); 
balance_hermione_before = account_hermione.get_balance(); 
atm_machine.transfer_atm(account_harry, account_hermione, 10000); 
print(f"Harry account before test: {balance_harry_before}")
print(f"Harry account after test: {account_harry.get_balance()}")
print(f"Hermione account before test: {balance_hermione_before}")
print(f"Hermione account after test: {account_hermione.get_balance()}")
print()

# # Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# # ผลที่คาดหวัง
# # Hermione transaction : D-ATM:1002-1000-2000
# # Hermione transaction : W-ATM:1002-500-1500
# # Hermione transaction : TD-ATM:1002-10000-11500

atm_machine = bank.get_atm('1002')
account_hermione = atm_machine.insert_card(bank, atm_card_2, '1234')

account_hermione.print_transactions()
print()

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_card(bank, atm_card_1, '9999')  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN
if test_result is None:
    print("Invalid PIN")  
else:
    print(test_result.get_account_number())

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
atm_machine = bank.get_atm('1001')
account = atm_machine.insert_card(bank, atm_card_1, '1234')  # PIN ถูกต้อง
harry_balance_before = account.get_balance()

print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
result = atm_machine.withdraw(account, 45000, atm_card_1)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.get_balance()}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
account = atm_machine.insert_card(bank, atm_card_1, '1234')

print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.get_balance()}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(account, 250000, atm_card_1)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.get_balance()}")
print("-------------------------")



