stocks = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 200,   # Google
    "MSFT": 450,   # Microsoft
    "AMZN": 220 ,   # Amazon
    "TCS": 3500,
    "INFY": 1600,
    "RELIANCE": 1450,
    "HDFCBANK": 1900,
    "ITC": 450
}
Continue=True
total_investment=0
portfolio=" "
while Continue:
    stock_name=input("Enter the stock name: ").upper()
    quantity=int(input(" Enter how many stocks you wanna buy: "))
    if stock_name in stocks:
        price=stocks[stock_name]
        investment=price* quantity
        total_investment+=investment
        portfolio += f"{stock_name} - {quantity} shares - {investment}\n"
        print(f"Investment for {stock_name}:",investment)
        print("Your total investment is ",total_investment)
        repeat=input("Do you want to continue with next stock['yes' or 'no']: ")
        if repeat=="no":
            Continue=False
    else:
        print("Enter valid stock name.")
with open("portfolio.txt", "w") as file:
    file.write(portfolio)
    file.write(f"\nTotal Investment: {total_investment}")
print("Portfolio saved to portfolio.txt")
        


