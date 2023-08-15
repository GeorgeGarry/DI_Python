class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property  # getter
    def email(self):
        return f"{self.__first_name}.{self.__last_name}@gmail.com"

    @email.setter
    def email(self, name):
        self.__first_name = name


bob = Person("Bob", "Jummy")

print(bob.email)

bob.email = "Bob1"
print(bob.email)


class MyClass(object):
    count = 0

    def __init__(self, val):
        self.val = val
        MyClass.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

object_1 = MyClass(111)
print("\nValue of object : %s" % object_1.get_val())
print(MyClass.get_count())

object_2 = MyClass(20)
print("\nValue of object : %s" % object_2.get_val())
print(MyClass.get_count())



# class MyClass(object):
#     count = 0

#     def __init__(self, val):
#         self.val = self.filterint(val)
#         MyClass.count += 1

#     @staticmethod
#     def filterint(value):
#         if not isinstance(value, int):
#             print("Entered value is not an INT, value set to 0")
#             return 0
#         else:
#             return value


# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)

# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint("dd"))
# print(a.val)



from datetime import datetime, timedelta

# Replace these values with your actual birthday
birthday_year = 1991
birthday_month = 12
birthday_day = 31
birthday_time = "00:00:00"  # Replace with your birthday time

# Get the current date and time
current_datetime = datetime.now()

# Construct the birthday datetime object
birthday_datetime = datetime(birthday_year, birthday_month, birthday_day)
birthday_datetime = birthday_datetime.replace(hour=int(birthday_time[:2]), minute=int(birthday_time[3:5]), second=int(birthday_time[6:]))

# Calculate the time difference
time_difference = birthday_datetime - current_datetime

# Calculate days, hours, minutes, and seconds
days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

# Format the countdown message
countdown_message = f"My birthday is in {days} days, and {hours:02d}:{minutes:02d}:{seconds:02d}"

print(countdown_message)
