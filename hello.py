name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет? "))
city = input("Из какого ты города?" )

ageDifference = 0
if age < 100:
    ageDifference = 100 - age
    print(f"Тебя зовут {name}, ты из города {city}, тебе {age} лет. До 100 лет тебе осталось {ageDifference}")
else:
    print(f"Тебя зовут {name}, ты из города {city}, тебе {age} лет. Тебе уже давно за сотку лет!")

