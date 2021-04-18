class Category:
  def __init__(self, category): 
        self.ledger =[]
        self.amount=0
        self.category = category 

# Creating a method that will help account for withdrawals and transfers
  def check_funds(self,amount):
    if self.amount< amount:
      return False
    else:
      return True

  # Creating a method that will account for deposits
  def deposit(self,amount, description=""):
    self.ledger.append({"amount":amount,"description":description})
    self.amount += amount

  # Creating a method that will account for withdrawals
  def withdraw(self,amount,description=""):
    if self.check_funds(amount) ==True:
      self.amount -=amount
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # Creating a method that will account for transfers
  def transfer(self,amount,category):
    if self.check_funds(amount)==True:
      self.amount-=amount
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False


  # Creating a method to show balance of budget for each category
  def get_balance(self):
    return self.amount

  # Creating a method that will help display the budget properly
  def __str__(self):
    result=""
    result+="--------------"+ str(self.category)+"--------------"+"\n"
    for transaction in self.ledger:
      amount=0
      description=""
      for key,value in transaction.items():
          if key=="amount":
            amount = value
          elif key=="description":
            description=value
      if len(description)>23:
        description=description[:23]
      amount = str(format(float(amount),'.2f'))
      if len(amount)>7:
        amount= amount[:7] 
      result+= description + str(amount).rjust(30-len(description))+"\n"
    result+="Total: "+str(format(float(self.amount),'.2f'))
    return result
    
       
#Examle Objects (Food, Clothing, Entertainment) to utilize the created methods
    
food = Category("Food")
food.deposit(500, "Food deposit")
food.withdraw(50, "Market shopping")

clothing = Category("Clothing")
clothing.deposit(400, "Clothing deposit")
clothing.withdraw(250, "Balenciaga T-shirt")
food.transfer(50, clothing)

entertainment = Category("Entertainment")
entertainment.deposit(300, "Entertainment deposit")
entertainment.withdraw(50, "For flexing")
entertainment.transfer(100, food)

# To display the transactions in each object category
print(food)
print(clothing)
print(entertainment)

# To display the balance of each object category properly
print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())
