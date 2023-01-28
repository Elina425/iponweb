# # Task 1
# # Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
#
# def extract_create(newd, mention):
#     extracted = {}
#     for key in mention:
#         extracted[key] = newd[key]
#     return extracted
# # print(extract_create({
# #     "name": "Kelly",
# #     "age": 25,
# #     "salary": 8000,
# #     "city": "New york"}, ["name", "salary"]))
#
# # Task 2
# # Get the key of a minimum value from the following dictionary.
#
# def key_minimum(given_dict):
#     values = list(given_dict.values())
#     min = values[0]
#     for i in range(1,len(values)):
#         if(min>values[i]):
#             min = values[i]
#     for key in given_dict.keys():
#         if given_dict[key] == min:
#             return key
# print(key_minimum({'Physics': 82,
#   'Math': 65,
#   'history': 75
# }))
#
# # Task 3
# # Write a Python program to copy the contents of a file to another file
#
# def copy_file(real_path, copy_path):
#     with open(real_path, 'r') as f:
#         f = f.read()
#     with open(copy_path, 'w') as f1:
#         f1.write(f)
# print(copy_file("real.txt", "another.txt"))
#
# # Task 4
# # Write a Python program to count the frequency of words in a file
#
# def count_freq(f_path):
#     with open(f_path, 'r') as f:
#         empty = {}
#         f = f.read().split(" ")
#         count = 0
#         for i in f:
#             if i not in empty:
#                 empty[count]=1
#             else:
#                 empty[count]+=1
#     return count
# print(count_freq("real.txt"))
#
# # Task 5
# # Write a Python program to read last n lines of a file
#
# def rlast_lines(f_path, n):
#     with open(f_path, 'r') as f:
#         f = f.readlines()[n:]
#         for i in f:
#             print(i)
# print(rlast_lines("real.txt", 4))
#
# # Task 6
# # Finish class work, which you started in class.
# class Company:
#     def __init__(self, c, f):
#         self.company_name = c
#         self.founded_at = f
#         self.employees_count = 0
#
#     def __repr__(self):
#         return "{} {} {}".format(self.company_name, self.founded_at, self.employees_count)
#
#
# class Job:
#     def __init__(self, company: 'Company', salary, experience_year, position):
#         self.company = company
#         self.salary = salary
#         self.experience_year = experience_year
#         self.position = position
#
#     def __repr__(self):
#         return "{} {} {} {}".format(self.company, self.salary, self.experience_year, self.position)
#
#     def change_salary(self, up):
#         self.salary = up
#
#     def change_experience_year(self, year):
#         self.experience_year = year
#
#     def change_postition(self, p):
#         self.salary = p
#
#
# class Person:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.friends = []
#         self.job = []
#
#     def __repr__(self):
#         return '{} {} {} {}'.format(self.name, self.surname, self.gender, self.friends)
#
#     def add_friend(self, f: "Person"):
#         self.friends.append(f)
#
#     def remove_friend(self, f: 'Person'):
#         self.friends.remove(f)
#
#     def add_job(self, j: 'Job'):
#         self.job.append(j)
#         j.company.employees_count += 1
#
#     def remove_job(self, j: 'Job'):
#         self.job.remove(j)
#         j.company.employees_count -= 1
#
#     def display_job(self):
#         for j in self.job:
#             print(j)
#
#
# company1 = Company("OpenAI", "2015")
# company2 = Company("Google", "1998")
#
# job1 = Job(company1, 80000, 4, "Software Engineer")
# job2 = Job(company2, 120000, 6, "Senior Software Engineer")
#
# person1 = Person("John", "Doe", "Male")
# person2 = Person("Jane", "Doe", "Female")
#
# person1.add_job(job1)
# person1.add_friend("Elina")
# person1.add_friend("Elin")
# person1.remove_friend("Elin")
# person2.add_job(job2)
#
#
# print(company1)
# print(company2)
# def count_freq(f_path):
#     with open(f_path, 'r') as f:
#         empty = {}
#         f = f.read().split(" ")
#         for i in f:
#             if i not in empty:
#                 empty[i]=1
#             else:
#                 empty[i]+=1
#     return empty
# print(count_freq("real.txt"))
# print(person1)
# print(person2)
#
# print(job1)
# print(job2)


# Task 7
# Write this classes.
class Date:
    def __init__(self, day, month, year):
        if year>=0:
            self._year = year
        else:
            raise ValueError
            print("Invalid year")
        if 0<month<=12:
            self._month = month
        else:
            raise ValueError
            print("Invalid month")
        if 1<=day<=31:
            self._day = day
        else:
            raise ValueError
            print("Invalid days")
    @property
    def get_year(self):
        return self._year
    @get_year.setter
    def set_year(self, val):
        self._year = val
        return self
    @get_year.deleter
    def delete_year(self):
        del self._year

    @property
    def get_month(self):
        return self._month
    @get_month.setter
    def set_month(self, val):
        self._month = val
        return self
    @get_month.deleter
    def delete_month(self):
        del self._month

    @property
    def get_day(self):
        return self._day
    @get_day.setter
    def set_day(self, val):
        self._day = val
        return self
    @get_day.deleter
    def delete_day(self):
        del self._day
    @get_day.deleter
    def delete_day(self):
        del self._day
    def __repr__(self):
        return "{}.{}.{}".format(self._day, self._month, self._year)

    def add_day(self, days):
        self._day += days
        self._month += self._day // 31
        self._month = self._month % 12
        self._day = self._day % 31
        self._year += self._month // 12
        if self._month == 2 and self._day > 29 and self.is_leap_year():
            self._day = 29
        elif self._month == 2 and self._day > 28:
            self._day = 28
        return self

    def add_month(self, months):
        self._month += months
        self._year = self._year + self._month // 12

        self._month = self._month % 12

        return self

    def add_year(self, years):
        self._year += years
        return self
    def sub_day(self, days):
        self._day-=days
        self._month -=(self._day//31)
        self._day %=31
        self._year -= (self._month//12)
        self._month %=12
        if self._month == 2 and self._day > 29 and self.is_leap_year():
            self._day = 29
        elif self._month == 2 and self._day > 28:
            self._day = 28
        return self
    def sub_year(self, years):
        self._year-=years
        return self
    def sub_month(self, months):
        self._month-=months
        self._year-=self._month//12
        self._month%=12
        return self


    def is_leap_year(self):
        if self._year % 4 == 0:
            if self._year % 100 == 0:
                if self._year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

date = Date(10,8,2023)
print(date.add_month(6))
print(date.get_month)
print(date.add_day(50))
#print(date.delete_day)
print(date.get_day)
class Time:
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __repr__(self):
        return "{}:{}:{}".format(self._hour, self._minute, self._second)

    def add_second(self, seconds):
        self._second += seconds
        self._minute += self._second // 60
        self._second %= 60
        self._hour += self._minute // 60
        self._minute %= 60
        self._hour %= 24
        return self

    def add_minute(self, minutes):
        self._minute += minutes
        self._hour += self._minute // 60
        self._minute %= 60
        self._hour %= 24
        return self

    def add_hour(self, hours):
        self._hour += hours
        self._hour %= 24
        return self
    def sub_second(self, seconds):
        self._second-=seconds
        self._minute-=self._second//60
        self._second%=60
        self.hour -=self.minute//60
        self._minute%=60
        return self
    def sub_minute(self, minutes):
        self._minute-=minutes
        self._hour-=self._minute//60
        self._minute%=60
        return self
    def sub_hour(self, hours):
        self._hour -= hours
        self._minute -= self._hour // 60
        self._hour = self._hour % 60
        self._second -= self._minute // 60
        self._minute = self._minute % 60
        return self


    def __add__(self, other):
        new_hour = self._hour + other._hour
        new_minute = self._minute + other._minute
        new_second = self._second + other._second
        return Time(new_hour, new_minute, new_second)

    def __sub__(self, other):
        new_hour = self._hour - other._hour
        new_minute = self._minute - other._minute
        new_second = self._second - other._second
        return Time(new_hour, new_minute, new_second)

time1 = Time(1, 30, 45)
time2 = Time(2, 45, 30)
result = time2+time1
print(result)
substition = time2-time1
print(substition)
