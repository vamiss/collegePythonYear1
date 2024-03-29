"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.
Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""

def scores(subjects):
    total_score = 0
    for i in range(subjects):
        score = int(input(f"Введите балл по предмету {i+1}: "))
        total_score += score
    print(f"Итоговый счёт: {total_score}")
    return total_score


def get_credential(score):
    if score > 80:
        return "Наградить дипломом."
    elif score > 50:
        return "Наградить похвальной грамотой."
    else:
        return "Выдать грамоту об участии."


while True:
    name = input("Введите имя студента (для выхода введите \"стоп\"): ")
    if name == "стоп":
        break
    num_subjects = int(input("Введите число предметов: "))
    score = scores(num_subjects)
    credential = get_credential(score)
    print(credential)

