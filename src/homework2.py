# Task 1
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

def extract_create(newd, mention):
    extracted = {}
    for key in mention:
        extracted[key] = newd[key]
    return extracted
# print(extract_create({
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}, ["name", "salary"]))

# Task 2
# Get the key of a minimum value from the following dictionary.

def key_minimum(given_dict):
    values = list(given_dict.values())
    min = values[0]
    for i in range(1,len(values)):
        if(min>values[i]):
            min = values[i]
    for key in given_dict.keys():
        if given_dict[key] == min:
            return key
print(key_minimum({'Physics': 82,
  'Math': 65,
  'history': 75
}))

# Task 3
# Write a Python program to copy the contents of a file to another file

def copy_file(real_path, copy_path):
    with open(real_path, 'r') as f:
        f = f.read()
    with open(copy_path, 'w') as f1:
        f1.write(f)
print(copy_file("real.txt", "another.txt"))

# Task 4
# Write a Python program to count the frequency of words in a file

def count_freq(f_path, w):
    with open(f_path, 'r') as f:
        f = f.read().split(" ")
        count = 0
        for i in f:
            if i == w:
                count+=1
    return count
print(count_freq("real.txt", 'be'))

# Task 5
# Write a Python program to read last n lines of a file

def rlast_lines(f_path, n):
    with open(f_path, 'r') as f:
        f = f.readlines()[n:]
        for i in f:
            print(i)
print(rlast_lines("real.txt", 4))

# Task 6
# Finish class work, which you started in class.
class Company:
    def __init__(self, c, f):
        self.company_name = c
        self.founded_at = f
        self.employees_count = 0

    def __repr__(self):
        return "{} {} {}".format(self.company_name, self.founded_at, self.employees_count)


class Job:
    def __init__(self, company: 'Company', salary, experience_year, position):
        self.company = company
        self.salary = salary
        self.experience_year = experience_year
        self.position = position

    def __repr__(self):
        return "{} {} {} {}".format(self.company, self.salary, self.experience_year, self.position)

    def change_salary(self, up):
        self.salary = up

    def change_experience_year(self, year):
        self.experience_year = year

    def change_postition(self, p):
        self.salary = p


class Person:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.friends = []
        self.job = []

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.surname, self.gender, self.friends)

    def add_friend(self, f: "Person"):
        self.friends.append(f)

    def remove_friend(self, f: 'Person'):
        self.friends.remove(f)

    def add_job(self, j: 'Job'):
        self.job.append(j)
        j.company.employees_count += 1

    def remove_job(self, j: 'Job'):
        self.job.remove(j)
        j.company.employees_count -= 1

    def display_job(self):
        for j in self.job:
            print(j)


company1 = Company("OpenAI", "2015")
company2 = Company("Google", "1998")

job1 = Job(company1, 80000, 4, "Software Engineer")
job2 = Job(company2, 120000, 6, "Senior Software Engineer")

person1 = Person("John", "Doe", "Male")
person2 = Person("Jane", "Doe", "Female")

person1.add_job(job1)
person1.add_friend("Elina")
person1.add_friend("Elin")
person1.remove_friend("Elin")
person2.add_job(job2)


print(company1)
print(company2)

print(person1)
print(person2)

print(job1)
print(job2)


# Task 7
# Write this classes.
class Date:
    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year
    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)
    def add_day(self, days):
        self.day+=days
        if self.day >=31:
            self.add_month(1)
        return self
    def add_month(self, month):
        self.month+=month
        if self.month >=12:
            self.add_year(1)
        return self
    def add_year(self, years):
        self.years += years
        return self
    def is_leap_year(self):
        if self.year %4 == 0:
            if self.year % 100 ==0:
                if self.year %400 ==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

class Date:
    def __init__(self, day, month, year):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def add_day(self, days):
        self.day += days
        return self

    def add_month(self, months):
        self.month += months
        return self

    def add_year(self, years):
        self.year += years
        return self

    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

date = Date(10,8,2000)
print(date.add_year(3))
print(date.is_leap_year())

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def add_second(self, seconds):
        self.second += seconds
        self.minute += self.second // 60
        self.second %= 60
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24
        return self

    def add_minute(self, minutes):
        self.minute += minutes
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24
        return self

    def add_hour(self, hours):
        self.hour += hours
        self.hour %= 24
        return self

    def sum(self, other):
        self.add_second(other.second)
        self.add_minute(other.minute)
        self.add_hour(other.hour)
        return self


time1 = Time(1, 30, 45)
time2 = Time(2, 45, 30)
print(Time.sum(time1, time2))