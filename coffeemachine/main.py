MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
coin = 0

def is_resourse(order_ingredients):
    # 재료를 파악한 후 부족한지 아닌지 반환
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("음료 재료 부족")
            return False
        else:
            return True

def process_coin():
    # 투입된 동전의 총 합 계산 후 반환
    print("동전을 넣으세요")
    total = int(input("guartars : "))* 0.25
    total += int(input("dimes : "))* 0.1
    total += int(input("mickles : ")) * 0.05
    total += int(input("pennies : ")) * 0.01
    return total
def is_change(money_received, drink_cost):
    # 돈이 부족한지 확인하고 거스름돈 계산
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global coin
        coin += drink_cost
        print("거스름돈 : ",change)
        return True
    else:
        print("돈 부족")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(drink_name , "음료 나왔습니다")

# TODO : What would you like? (espresso/latte/cappuccino)
while is_on:
    choice = (input('어떤걸 주문? (espresso/latte/cappuccino)'))
# TODO : off를 입력하면 커피머신 종료
    if choice =="off":
        is_on = False
# TODO : 커피자판기의 재료 현황 보고서 출력
    elif choice == "report":
        print(resources, "coin : ", coin)
    else :
        drink = MENU[choice]
        # TODO : 음료를 만들기 위한 재료 파악
        if is_resourse(drink["ingredients"]): # 재료 파악
            # TODO : 코인 처리
            payment = process_coin()   #돈 계산 후 반환
            if is_change(payment, drink["cost"]) :
            # TODO : 거래 성공여부 파악
                make_coffee(choice, drink["ingredients"])

