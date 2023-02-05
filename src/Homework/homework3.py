
class Date:
    def __init__(self, day, month, year):
        if year>=0:
            self.__year = year
        else:
            raise ValueError
            print("Invalid year")
        if 0<month<=12:
            self.__month = month
        else:
            raise ValueError
            print("Invalid month")
        if 1<=day<=31:
            self.__day = day
        else:
            raise ValueError
            print("Invalid days")
    @property
    def get_year(self):
        return self.__year
    @get_year.setter
    def set_year(self, val):
        self._year = val
        return self
    @get_year.deleter
    def delete_year(self):
        del self.__year

    @property
    def get_month(self):
        return self.__month
    @get_month.setter
    def set_month(self, val):
        self.__month = val
        return self
    @get_month.deleter
    def delete_month(self):
        del self.__month

    @property
    def get_day(self):
        return self.__day
    @get_day.setter
    def set_day(self, val):
        self.__day = val
        return self
    @get_day.deleter
    def delete_day(self):
        del self._day
    @get_day.deleter
    def delete_day(self):
        del self.__day
    def __repr__(self):
        return "{}.{}.{}".format(self.__day, self.__month, self.__year)

    def add_day(self, days):
        self.__day += days
        self.__month += self.__day // 31
        self.__month = self.__month % 12
        self.__day = self.__day % 31
        self.__year += self.__month // 12
        if self.__month == 2 and self.__day > 29 and self.is_leap_year():
            self.__day = 29
        elif self.__month == 2 and self.__day > 28:
            self.__day = 28
        return self

    def add_month(self, months):
        self.__month += months
        self.__year = self.__year + self.__month // 12

        self.__month = self.__month % 12

        return self

    def add_year(self, years):
        self.__year += years
        return self
    def sub_day(self, days):
        self.__day-=days
        self.__month -=(self._day//31)
        self.__day %=31
        self.__year -= (self._month//12)
        self.__month %=12
        if self.__month == 2 and self._day > 29 and self.is_leap_year():
            self.__day = 29
        elif self.__month == 2 and self._day > 28:
            self.__day = 28
        return self
    def sub_year(self, years):
        self.__year-=years
        return self
    def sub_month(self, months):
        self.__month-=months
        self.__year-=self._month//12
        self.__month%=12
        return self


    def is_leap_year(self):
        if self.__year % 4 == 0:
            if self.__year % 100 == 0:
                if self.__year % 400 == 0:
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
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self):
        return "{}:{}:{}".format(self._hour, self._minute, self._second)

    def add_second(self, seconds):
        self.__second += seconds
        self.__minute += self._second // 60
        self.__second %= 60
        self.__hour += self._minute // 60
        self.__minute %= 60
        self.__hour %= 24
        return self

    def add_minute(self, minutes):
        self.__minute += minutes
        self.__hour += self._minute // 60
        self.__minute %= 60
        self.__hour %= 24
        return self

    def add_hour(self, hours):
        self.__hour += hours
        self.__hour %= 24
        return self
    def sub_second(self, seconds):
        self.__second-=seconds
        self.__minute-=self.__second//60
        self.__second%=60
        self.__hour -=self.minute//60
        self.__minute%=60
        return self
    def sub_minute(self, minutes):
        self.__minute-=minutes
        self.__hour-=self._minute//60
        self.__minute%=60
        return self
    def sub_hour(self, hours):
        self.__hour -= hours
        self.__minute -= self._hour // 60
        self.__hour = self._hour % 60
        self.__second -= self._minute // 60
        self.__minute = self._minute % 60
        return self


    def __add__(self, other):
        new_hour = self.__hour + other._hour
        new_minute = self.__minute + other._minute
        new_second = self.__second + other._second
        return Time(new_hour, new_minute, new_second)

    def __sub__(self, other):
        new_hour = self.__hour - other._hour
        new_minute = self.__minute - other._minute
        new_second = self.__second - other._second
        return Time(new_hour, new_minute, new_second)

time1 = Time(1, 30, 45)
time2 = Time(2, 45, 30)
result = time2+time1
print(result)
substition = time2-time1
print(substition)
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
#

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
        for j in self._job:
            print(j)
# Class Money
# Some Logic:
# If we have 2 objects with different currency we need to have some conversation
# method. Try to come up with some exchange logic. Here is some note for you.
class MoneyError(Exception):
    pass

class Money:
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def __init__(self, amount: int, currency: str):
        if not type(amount) is int:
            raise Exception("Amonunt must be int type")
        else:
            self._amount = amount
        if not type(currency) is str:
            raise Exception("Amonunt must be int type")
        else:
            self._currency = currency

    def __repr__(self):
        return "{} {}".format(self._amount, self._currency)

    @property
    def get_amount(self):
        return self._amount

    @get_amount.setter
    def set_amount(self, value):
        self._amount = value
        return self

    @property
    def get_currency(self):
        return self._currency

    @get_currency.setter
    def set_currency(self,value):
        self._currency = value
        return self
    def convert(self, new_currency):
        if self._currency == new_currency:
            return self._amount
        if self._currency not in Money.exchange:
            raise MoneyError("this currency doesn;t exist in our system")
        rate = self.exchange[self._currency]/self.exchange[new_currency]
        return self._amount * rate


    def __add__(self, other):
        if self._currency != other._currency:
            raise MoneyError("Currencies don't match")
        return Money(self._amount + other._amount, self._currency)


    def __sub__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        if(self._amount< other._amount):
            raise MoneyError("The current value is less than the other")
        return Money(self._amount - other._amount, self._currency)


    def __truediv__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        if(other._amount==0):
            raise MoneyError("you can't devide on zero")
        return Money(self._amount / other._amount, self._currency)


    def __eq__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        return self._amount == other._amount


    def __ne__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        return self._amount != other._amount


    def __lt__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        return self._amount < other._amount


    def __gt__(self, other):
        if (self._currency != other._currency):
            raise ValueError("Currenciens don't match")
        return self._amount > other._amount


    def __le__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        return self._amount <= other._amount


    def __ge__(self, other):
        if (self._currency != other._currency):
            raise MoneyError("Currenciens don't match")
        return self._amount >= other._amount

# budget1 = Money(10000, "AMD")
# budget2 = Money(12000, "AMD")
# print(budget1.convert("USD"))
# print(budget1.get_amount)
# total = budget1 + budget2
# # sub = budget1-budget2
# not_eq = budget1 !=budget2
# greater_equal = budget1>budget2
# print(budget1.get_amount)
# print(budget2.get_amount)
# print(total)
# #print(sub)
# print(not_eq)
# print(greater_equal)


def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@call_counter
def my_function():
    print("Function called")

for i in range(5):
    my_function()

print("Number of times called:", my_function.count)
class MyrangeError(Exception):
    pass
class MyRange:
    def __init__(self, current, end, step):
        self._current = current
        self._end = end
        self._step = step
    def __repr__(self):
        return "{} {} {}".format(self._current, self._end, self._step)

    def __iter__(self):
        return self
    def __next__(self):
        print("######################")
        if self._current == self._end:
            raise MyrangeError("you reached the end")
        result = self._current
        self._current += self._step
        return result
    def __len__(self):
        return(self._end-self._current)//self._step+1
    def __getitem__(self, item):
        if item>len(self):
            raise MyrangeError("out of range")
        return self._current + (item-1)* self._step
    def __reversed__(self):
        return MyRange(self._end-self._step, self._current-self._step, -self._step)
# r = MyRange(2,12, 2)
# print(len(r))
# print(r)
# for i in r:
#     print(i)
# print(r[6])
# print(reversed(r))
# try:
#     for i in range(len(r)):
#         print(r.__next__())
# except MyrangeError as e:
#     print(e)

class DoctorError(Exception):
    pass
class Doctor(Person):
    def __init__(self, name, surname, gender, department: str, profession: str, patronymic: str, salary: int):
        super().__init__(name, surname, gender)
        if type(department) is not str:
            raise DoctorError("the type must be string")
        else:
            self._department = department
        if type(profession) is not str:
            raise DoctorError("the type must be string")
        else:
            self._profession = profession
        if type(patronymic) is not str:
            raise DoctorError("the type must be string")
        else:
            self._patronymic = patronymic
        if type(salary) is not int:
            raise DoctorError("the type must be int")
        else:
            self._salary = salary
    def __repr__(self):
        return "{} {} {} {} {} {} {}".format(self.name, self.surname, self.gender, self._department, self._profession, self._patronymic, self._salary)
    @property
    def get_department(self):
        return self._department
    @get_department.setter
    def set_department(self, dep):
        self._department = dep
        return self

    @get_department.deleter
    def delete_department(self):
        del self._department
    @property
    def get_profession(self):
        return self._profession
    @get_profession.setter
    def set_profession(self, prof):
        self._profession = prof
        return self

    @get_profession.deleter
    def delete_profession(self):
        del self._profession

    @property
    def get_patoronymic(self):
        return self._patronymic

    @get_patoronymic.setter
    def set_patronymic(self, patro):
        self._patronymic = patro
        return self

    @get_patoronymic.deleter
    def delete_patronymic(self):
        del self._patronymic
    @property
    def get_salary(self):
        return self._salary
    @get_salary.setter
    def set_salary(self, sal):
        self._salary = sal
        return self
    @get_salary.deleter
    def delete_salary(self):
        del self._salary

doctor1 = Doctor("Paul", "Smith", "male", "surgery", "neurologist", "undefined", 10000000)
print(doctor1)

# set the salary using the set_salary method


# check the value of the salary property
print(doctor1.get_salary)

class CityError(Exception):
    pass
class City:
    def __init__(self, name:str, mayor:Person, population:int, language:str):
        if type(name) != str:
            raise CityError("the name must be string")
        else:
            self._name = name
        if not isinstance(mayor,Person):
            raise CityError("the mayor must be person's instance")
        else:
            self._mayor = mayor
        if type(population) != int:
            raise CityError("population must be int type")
        else:
            self._population = population
        if type(language) !=str:
            raise CityError("the language must be str type")
        else:
            self._language = language
    def __repr__(self):
        return "{} {} {} {}".format(self._name, self._mayor, self._population, self._language)
    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, val):
        self._name = val
        return self
    @property
    def get_mayor(self):
        return self._mayor
    @get_mayor.setter
    def set_mayor(self, mayor:"Person"):
        if not isinstance(mayor, Person):
            raise CityError("Must be Person instance")
        self._mayor = mayor
        return self
    @property
    def get_population(self):
        return self._population
    @get_population.setter
    def set_population(self, pop):
        self._population = pop
        return self
    @property
    def get_language(self):
        return self._language
    @get_language.setter
    def set_language(self, lang):
        self._language = lang


mayor1 = Person("Teodor", "Ruzvelt", "male")
city1 = City("USA", mayor1, 1123456789, "English")
city1.set_population = 4567890
print(city1)
print(city1.get_population)
print(city1.get_language)


class UniversityError(Exception):
    pass
class University(Person):
    def __init__(self, name:str, founded_at:Date, rector:Person, city:City):
        if type(name) is not str:
            raise UniversityError("name is str")
        else:
            self._name = name
        if not isinstance(founded_at, Date):
            raise UniversityError("must be date instance")
        else:
            self._founded_at = founded_at
        if not isinstance(rector, Person):
            raise UniversityError("must be person instance")
        else:
            self._rector = rector
        if not isinstance(city, City):
            raise UniversityError("must be city isntance")
        else:
            self._city = city
    def __repr__(self):
        return "{} {} {} {}".format(self._name, self._founded_at, self._rector, self._city.get_name)
    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, name):
        self.name = name
    @property
    def get_founded_at(self):
        return self._founded_at
    @property
    def get_rector(self):
        return self._rector
    @get_rector.setter
    def set_rector(self, rector:Person):
        if not isinstance(rector, Person):
            raise UniversityError("not person")
        self._rector = rector
    @property
    def get_city(self):
        return self._city
rector = Person("Bob", "Stuart", "male")
date = Date(8,5,1923)
harward = University("Harward", date, rector, city1)
print(harward)

class TeacherError(Exception):
    pass
class Teacher(Person):
    def __init__(self, name, surname, gender,university:University, faculty:str, experience:int, start_work_at:Date, subject:str, salary:int):
        if not isinstance(university, University):
            raise TeacherError("not univer")
        else:
            self._university = university
        super().__init__(name, surname, gender)
        if type(faculty) is not str:
            raise TeacherError("must be str faculty")
        else:
            self._faculty = faculty
        if type(experience) is not int:
            raise TeacherError("must be experience int ")
        else:
            self._experience = experience
        if not isinstance(start_work_at, Date):
            raise TeacherError("not valid date")
        else:
            self._start_work_at = start_work_at
        if type(subject) is not str:
            raise TeacherError("must be str subject")
        else:
            self._subject = subject
        if type(salary) is not int:
            raise TeacherError("must be int salary")
        else:
            self._salary = salary
    def __repr__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.name, self.surname, self.gender, self._university,
self._faculty,self._experience, self._start_work_at, self._subject, self._salary)

    @property
    def get_experince(self):
        return self._experience
    @get_experince.setter
    def set_experience(self, experience):
        self._experience = experience
    @property
    def get_start_work_at(self):
        return self._start_work_at
    @property
    def get_salary(self):
        return self._salary
    @get_salary.setter
    def set_salary(self, salary):
        self._salary = salary
    @property
    def get_subject(self):
        return self._subject
    @property
    def get_faculty(self):
        return self._faculty
    @get_faculty.setter
    def set_faculty(self, faculty):
        self._faculty = faculty
date_teacher = Date(2,4,2016)
teacher1 = Teacher("john", "Smith", "male",  harward,"math", 10, date, "Linear", 123456789)
print(teacher1)

class StudentError(Exception):
    pass
class Student(Person):
    def __init__(self, name, surname, gender, university:University, faculty:str, course:int, started_at:Date):
        super().__init__(name, surname, gender)
        if not isinstance(university, University):
            raise StudentError("must be university inst")
        else:
            self._university = university
        if type(faculty) is not str:
            raise StudentError("type must be str")
        else:
            self._faculty  = faculty
        if type(course) is not int:
            raise StudentError("course must be int type")
        else:
            self._course = course
        if not isinstance(started_at, Date):
            raise StudentError("Must be instance of date")
        else:
            self._started_at = started_at
    def __repr__(self):
        return "{} {} {} {} {} {} {}".format(self.name, self.surname, self.gender, self._university.get_name,
self._faculty, self._course, self._started_at)
    @property
    def get_university(self):
        return self._university
    @get_university.setter
    def set_university(self, univer):
        if not isinstance(univer, University):
            raise UniversityError("Must be university isntance")
        self._university = univer

    @property
    def get_faculty(self):
        return self._faculty
    @get_faculty.setter
    def set_faculty(self, faculty):
        self._faculty = faculty
    @property
    def get_course(self):
        return self._course
    @get_course.setter
    def set_course(self, course):
        self._course=course
    @property
    def get_started_at(self):
        return self._started_at
date_uni = Date(24, 8, 2022)
student1 = Student("Elina", "melkonyan", "female", harward, "CS", 1,date_uni)
print(student1)