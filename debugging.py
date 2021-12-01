"""
Below you will find broken pieces of code, do you think you can spot all the errors and fix them? Don't forget to use the debugging skills that you have learned so far!

If you think this stuff is too easy for you, you can try to see if you can master the VS Code debugger! Just click the link above and get started.
"""

# 1
""" 
used ) instead of ] 
-add () after if statements
-if there is only 2 if statements you use else: instead of elif
"""
greeting = "Arrr!"
if greeting == ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
                


# 2
"""
-authors is misspelled
-for loop needs to be outside the dictionary
-for integers can't be seperated 
-after in you just need the variable name of the thing you'll be itterating through
-print function is missing ()
"""
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}
for author, date in authors.items():
    print("%s" % author + " died in " + "%d." % int(date))


# 3
"""
- " instead of ' and erase one )
-only one = needed
- missing : after the if condition
-change the ' to " so the program doesnt get confused
-python uses and instead of &&
-the last if statement should be an else statement 
"""
year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")



# 4
"""
-class not classy
-print needs to be indented bc its part of the function
-seperate the speak function
-the + symbol needs to be outside the ""
-.name not .fname
"""
class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def speak(self):
        print("My name is " + self.first + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()



# 5
"""
-need to convert to an integer for exam_two
-need commas between the array
-keep every variable consistant
-grades not grade
-grades is misspelled
-need : after every if statement
-letter_grade not letter-grade
"""
exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_3 = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_3]

sum = 0

for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")