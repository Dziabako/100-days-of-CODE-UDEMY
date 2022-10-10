# string.ascii_letters - randomowe litery ascii duze i male
# string.ascii_lowercase - tylko male litery
# string.ascii_uppercase - tylko duze litery
# string.digits - randomowe liczby od 0 do 9
# string.punctuation - randomowe znaki interpunkcyjne

def zad1():
    student_heights = input("Input a list of student heights: ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    print(student_heights)

    count = 0
    total = 0
    for student in student_heights:
        total += student
        count += 1

    average_height = round(total / count)
    print(f"Average height of students is {average_height}")


def zad2():
    student_scores = input("Input a list of student scores: ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)

    max_value = student_scores[0]
    for i in range(len(student_scores)):
        if max_value < student_scores[i]:
            max_value = student_scores[i]
    print(f"The highest score in the class is: {max_value}")

    print("\nRozwiązanie z kursu\n")

    highest_score = 0
    for score in student_scores:
        if score > highest_score:
            highest_score = score
    print(f"The highest score in the class is: {max_value}")


def zad3():
    total = 0
    # pierwszy argument w range jest opcjonalny
    # jezeli nie podamy zacznie sie od 0 tak jak to jest wyzej
    for n in range(1, 101):
        if n % 2 == 0:
            total += n
    print(total)

    print("\nRozwiazanie z kursu\n")

    total = 0
    for n in range(2, 101, 2):
        total += n
    print(total)


def zad4():
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


def password_generator():
    import string
    import random
    print("Welcome to the PyPassword Generator!")
    letters = int(input("How many letters would you like in your password?\n"))
    symbols = int(input("How many symbols would you like?\n"))
    numbers = int(input("How many numbers would you like?\n"))
    password = ""

    for l in range(letters):
        # musi byc random.choice bo inaczej wyswietli wszystki znaki a tak wybiera kilka z podanego zakresu
        password += random.choice(string.ascii_letters)
    for s in range(symbols):
        password += random.choice(string.punctuation)
    for n in range(numbers):
        password += random.choice(string.digits)

    print(password)

    # sposób na wymieszanie str
    # shuffle nie dziala na string wiec musi byc wczesniej zmienione na liste
    # "".join(lista) - laczenie listy, krotek itp w string z podanym na poczatku separatorem
    # .join trzeba przypisac do zmiennej jezeli chcemy ja wyswietlic lub od razu dac w print()
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    # inna zamiana wymieszanej listy na string
    # for char in password_list:
    #     password += char

    print(f"Here is your password: {password}")


zad4()

