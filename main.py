import time
import random
import os

clear = lambda: os.system("cls")

class main():

    def start(self):
        self.LargestNumber = int(input('Largest number: '))
        self.LargestNumber2 = self.LargestNumber
        self.YourNumber = random.randint(0, self.LargestNumber)
        print(f'Randomly selected number: {self.YourNumber}')
        time.sleep(1)
        clear()
        self.median = round(self.LargestNumber/2)
        self.ComputerGuess = self.median
        self.NumberOfTrys = 1
        self.StartTime = time.time()

    def guess(self):
        while True:
            if self.ComputerGuess == self.YourNumber:
                self.StopTime = time.time()
                self.SearchTime = self.StopTime - self.StartTime
                print(f'Binary search \nRange of numbers: 1 - {self.LargestNumber2} \nRandom number: {self.ComputerGuess} \nSearch time: {str((self.SearchTime))[:4]} seconds \nAttempts: {self.NumberOfTrys}')
                break

            elif self.ComputerGuess < self.YourNumber:
                self.median = round((self.median + self.LargestNumber)/2)
                self.ComputerGuess = self.median

            elif self.ComputerGuess > self.YourNumber:
                self.LargestNumber = self.median
                self.median = round(self.median/2)
                self.ComputerGuess = self.median

            else:
                break

            self.NumberOfTrys += 1

    def count(self):
        self.StartTime = time.time()
        self.ComputerGuess = 0
        self.NumberOfTrys = 1

        while True:
            if self.ComputerGuess == self.YourNumber:
                self.StopTime = time.time()
                self.SearchTime = self.StopTime - self.StartTime
                print(f'\nLinear search \nRange of numbers: 1 - {self.LargestNumber2} \nRandom number: {self.ComputerGuess} \nSearch time: {str((self.SearchTime))[:4]} seconds \nAttempts: {self.NumberOfTrys}')
                break

            else:
                self.ComputerGuess += 1
                self.NumberOfTrys += 1


app = main()
app.start()
app.guess()
app.count()
