from MDSCApp.models import Guess
import datetime
import pytz
import csv


def run():
    tz = pytz.timezone("Australia/Melbourne")
    recordStart = tz.localize(datetime.datetime(2022, 6, 27, 9, 0))
    recordEnd = tz.localize(datetime.datetime(2022, 6, 27, 21, 0))
    allGuesses = Guess.objects.filter(correct=True)
    studentIds = sorted(list(set([i.studentId for i in allGuesses])))

    header = ['Student ID', 'Name', 'Puzzle 1', 'Puzzle 2', 'Puzzle 3', 'Puzzle 4', 'Total']

    with open('cumulative.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for studentId in studentIds:
            student = allGuesses.filter(studentId=studentId)
            infoToWrite = [studentId, student[0].name]
            for puzzleId in (1,2,3,4):
                infoToWrite.append(student.filter(puzzle=puzzleId)[0].points*500 if puzzleId in [i.puzzle for i in student] else 0)
            infoToWrite.append(sum([int(i) for i in infoToWrite[-4:]]))
            writer.writerow(infoToWrite)

    allGuesses = [i for i in allGuesses if recordStart <= i.submitTime < recordEnd]
    studentIds = sorted(list(set([i.studentId for i in allGuesses])))
    with open('update.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for studentId in studentIds:
            student = allGuesses.filter(studentId=studentId)
            infoToWrite = [studentId, student[0].name]
            for puzzleId in (1,2,3,4):
                infoToWrite.append(student.filter(puzzle=puzzleId)[0].points*500 if puzzleId in [i.puzzle for i in student] else 0)
            infoToWrite.append(sum([int(i) for i in infoToWrite[-4:]]))
            writer.writerow(infoToWrite)

