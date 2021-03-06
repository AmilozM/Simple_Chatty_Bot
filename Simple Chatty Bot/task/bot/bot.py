def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    
    question = "Why do we use methods?"
    print(question)
    
    answer_1 = "1. To repeat a statement multiple times."
    answer_2 = "2. To decompose a program into several small subroutines."
    answer_3 = "3. To determine the execution time of a program."
    answer_4 = "4. To interrupt the execution of a program."
    
    print(answer_1)
    print(answer_2)
    print(answer_3)
    print(answer_4)

    answer = int(input())
    correct_answer = 2

    while answer != correct_answer:
        print("Please, try again.")
        answer = int(input())
    
    print('Completed, have a nice day!')
    print('Congratulations, have a nice day!')


greet('Aid', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()

# my first branch test
