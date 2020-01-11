import random
import Questions300_208
import os
# from PIL import Image


qaList = Questions300_208.qaList
corrCount = 0
qnumber = 1
random.shuffle(qaList)
os.system('color')
qCorrectColor = '\033[92m'
qWrongColor = '\033[91m'
endColor = '\033[0m'
corrAnsws = '\033[4m'

print('\nHow many questions would you like to answer?')
numOfQs = input(f'Enter a number from 1 to {len(qaList)}: ')
while not numOfQs.isdigit():
    print('That was not a number. Please try again:')
    numOfQs = input(f'Enter a number from 1 to {len(qaList)}: ')

for qaItem in qaList[:int(numOfQs)]:
    print(f'\nQuestion {qnumber}\n' + qaItem.question)
    if qaItem.corrAnsw5 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + [qaItem.corrAnsw3] + \
            [qaItem.corrAnsw4] + [qaItem.corrAnsw5]
    elif qaItem.corrAnsw4 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + \
            [qaItem.corrAnsw3] + [qaItem.corrAnsw4]
    elif qaItem.corrAnsw3 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2] + [qaItem.corrAnsw3]
    elif qaItem.corrAnsw2 is not None:
        possible = qaItem.otherAnsw + \
            [qaItem.corrAnsw] + [qaItem.corrAnsw2]
    else:
        possible = qaItem.otherAnsw + [qaItem.corrAnsw]

    random.shuffle(possible)
    count = 0    # list indexes start at 0 in python
    while count < len(possible):
        print(f'{count + 1}: {possible[count]}')
        count += 1

    if qaItem.corrAnsw5 is not None:
        print('\nPlease enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        print('Please enter the number of your fourth answer:')
        userAnsw4 = input()
        while not userAnsw4.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw4 = input()
        userAnsw4 = int(userAnsw4)
        print('Please enter the number of your fifth answer:')
        userAnsw5 = input()
        while not userAnsw5.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw5 = input()
        userAnsw5 = int(userAnsw5)
        if (
            possible[userAnsw - 1] == qaItem.corrAnsw or possible[
                userAnsw - 1] == qaItem.corrAnsw2 or possible[
                    userAnsw - 1] == qaItem.corrAnsw3 or possible[
                        userAnsw - 1] == qaItem.corrAnsw4 or possible[
                            userAnsw - 1] == qaItem.corrAnsw5) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or possible[
                userAnsw2 - 1] == qaItem.corrAnsw2 or possible[
                    userAnsw2 - 1] == qaItem.corrAnsw3 or possible[
                        userAnsw2 - 1] == qaItem.corrAnsw4 or possible[
                            userAnsw2 - 1] == qaItem.corrAnsw5) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or possible[
                    userAnsw3 - 1] == qaItem.corrAnsw2 or possible[
                        userAnsw3 - 1] == qaItem.corrAnsw3 or possible[
                            userAnsw3 - 1] == qaItem.corrAnsw4 or possible[
                                userAnsw3 - 1] == qaItem.corrAnsw5) and \
            (possible[userAnsw4 - 1] == qaItem.corrAnsw or possible[
                userAnsw4 - 1] == qaItem.corrAnsw2 or possible[
                    userAnsw4 - 1] == qaItem.corrAnsw3 or possible[
                        userAnsw4 - 1] == qaItem.corrAnsw4 or possible[
                            userAnsw4 - 1] == qaItem.corrAnsw5) and \
                (possible[userAnsw5 - 1] == qaItem.corrAnsw or possible[
                    userAnsw5 - 1] == qaItem.corrAnsw2 or possible[
                        userAnsw5 - 1] == qaItem.corrAnsw3 or possible[
                            userAnsw5 - 1] == qaItem.corrAnsw4 or possible[
                                userAnsw5 - 1] == qaItem.corrAnsw5):
            print(f'{qCorrectColor}Your answer was correct.{endColor}')
            corrCount += 1
        else:
            print(f'{qWrongColor}Your answer was wrong.{endColor}')
            print('Correct answers were: '
                  f'{corrAnsws + qaItem.corrAnsw + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw2 + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw3 + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw4 + endColor}, and '
                  f'{corrAnsws + qaItem.corrAnsw5 + endColor}')
        print('')
    elif qaItem.corrAnsw4 is not None:
        print('\nPlease enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        print('Please enter the number of your fourth answer:')
        userAnsw4 = input()
        while not userAnsw4.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw4 = input()
        userAnsw4 = int(userAnsw4)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or
            possible[userAnsw - 1] == qaItem.corrAnsw2 or
            possible[userAnsw - 1] == qaItem.corrAnsw3 or
            possible[userAnsw - 1] == qaItem.corrAnsw4) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or
             possible[userAnsw2 - 1] == qaItem.corrAnsw2 or
             possible[userAnsw2 - 1] == qaItem.corrAnsw3 or
             possible[userAnsw2 - 1] == qaItem.corrAnsw4) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or
                 possible[userAnsw3 - 1] == qaItem.corrAnsw2 or
                 possible[userAnsw3 - 1] == qaItem.corrAnsw3 or
                 possible[userAnsw3 - 1] == qaItem.corrAnsw4) and \
                (possible[userAnsw4 - 1] == qaItem.corrAnsw or
                 possible[userAnsw4 - 1] == qaItem.corrAnsw2 or
                 possible[userAnsw4 - 1] == qaItem.corrAnsw3 or
                 possible[userAnsw4 - 1] == qaItem.corrAnsw4):
            print(f'{qCorrectColor}Your answer was correct.{endColor}')
            corrCount += 1
        else:
            print(f'{qWrongColor}Your answer was wrong.{endColor}')
            print('Correct answer was: '
                  f'{corrAnsws + qaItem.corrAnsw + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw2 + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw3 + endColor}, and '
                  f'{corrAnsws + qaItem.corrAnsw4 + endColor}')
        print('')
    elif qaItem.corrAnsw3 is not None:
        print('\nPlease enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        print('Please enter the number of your third answer:')
        userAnsw3 = input()
        while not userAnsw3.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw3 = input()
        userAnsw3 = int(userAnsw3)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or
            possible[userAnsw - 1] == qaItem.corrAnsw2 or
            possible[userAnsw - 1] == qaItem.corrAnsw3) and \
            (possible[userAnsw2 - 1] == qaItem.corrAnsw or
             possible[userAnsw2 - 1] == qaItem.corrAnsw2 or
             possible[userAnsw2 - 1] == qaItem.corrAnsw3) and \
                (possible[userAnsw3 - 1] == qaItem.corrAnsw or
                 possible[userAnsw3 - 1] == qaItem.corrAnsw2 or
                 possible[userAnsw3 - 1] == qaItem.corrAnsw3):
            print(f'{qCorrectColor}Your answer was correct.{endColor}')
            corrCount += 1
        else:
            print(f'{qWrongColor}Your answer was wrong.{endColor}')
            print('Correct answer was: '
                  f'{corrAnsws + qaItem.corrAnsw + endColor}, '
                  f'{corrAnsws + qaItem.corrAnsw2 + endColor}, and '
                  f'{corrAnsws + qaItem.corrAnsw3 + endColor}')
        print('')
    elif qaItem.corrAnsw2 is not None:
        print('\nPlease enter the number of your first answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        print('Please enter the number of your second answer:')
        userAnsw2 = input()
        while not userAnsw2.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw2 = input()
        userAnsw2 = int(userAnsw2)
        if (possible[userAnsw - 1] == qaItem.corrAnsw or
            possible[userAnsw - 1] == qaItem.corrAnsw2) and \
                (possible[userAnsw2 - 1] == qaItem.corrAnsw or
                 possible[userAnsw2 - 1] == qaItem.corrAnsw2):
            print(f'{qCorrectColor}Your answer was correct.{endColor}')
            corrCount += 1
        else:
            print(f'{qWrongColor}Your answer was wrong.{endColor}')
            print('Correct answer was: '
                  f'{corrAnsws + qaItem.corrAnsw + endColor}, and '
                  f'{corrAnsws + qaItem.corrAnsw2 + endColor}')
        print('')
    else:
        print('\nPlease enter the number of your answer:')
        userAnsw = input()
        while not userAnsw.isdigit():
            print('That was not a number. '
                  'Please enter the number of your answer:')
            userAnsw = input()
        userAnsw = int(userAnsw)
        if possible[userAnsw - 1] == qaItem.corrAnsw:
            print(f'{qCorrectColor}Your answer was correct.{endColor}')
            corrCount += 1
        else:
            print(f'{qWrongColor}Your answer was wrong.{endColor}')
            print('Correct answer was: '
                  f'{corrAnsws + qaItem.corrAnsw + endColor}')
        print('')
    qnumber += 1

print(
    f'You answered {str(corrCount)} out of {int(numOfQs)} questions correctly.'
)
print(f'An approximate score of {int(corrCount/int(numOfQs)*1000)}')
