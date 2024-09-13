class Person:
    def __init__(self, name, surname, father, nums):
        self.name = name
        self.surname = surname
        self.father = father
        self.nums = nums

    def get_phone(self):
        flag = False
        for k, v in self.nums.items():
            if k == 'private':
                flag = True
                return v
        if not flag:
            return None

    def get_name(self):
        return f'{self.name} {self.surname} {self.father}'

    def get_work_phone(self):
        flag = False
        for k, v in self.nums.items():
            if k == 'work':
                flag = True
                return v
        if not flag:
            return None

    def get_sms_text(self):
        return f'Dear {self.name} {self.father}! Take part in our win-win competition for individuals'


class Company:
    def __init__(self, names, typ, nums, *count):
        self.names = names
        self.typ = typ
        self.nums = nums
        self.count = count

    def get_phone(self):
        flag = False
        for k, v in self.nums.items():
            if 'contact' == k:
                flag = True
                return v
        for i in self.count:
            if i.get_work_phone() is not None:
                flag = True
                return i.get_work_phone()
        if not flag:
            return None


    def get_name(self):
        return self.names

    def get_sms_text(self):
        return f'For company {self.names} there is a super offer! Take part in our win-win competition for {self.typ}'


def send_sms(*args):
    for i in args:
        if i.get_phone() is not None:
            print(f'SMS sent to the number {i.get_phone()} with text: {i.get_sms_text()}')
        else:
            print(f'Failed to send message to: {i.get_name()}')


person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "LP", {"contact": 111}, person3, person4)
company2 = Company("Cell", "LLP", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)