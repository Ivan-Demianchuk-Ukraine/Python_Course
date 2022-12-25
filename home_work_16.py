class Employee:
    """Class Employee"""
    sphere = 'IT'

    def __init__(self, name, age, position, skill):
        self.name = name
        self.age = age
        self.position = position
        self.skill = skill

    def get_employee_info(self):
        """method to get all employee information"""
        return [self.name, self.age, self.position, self.skill]

    @classmethod
    def set_new_sphere(cls, new_sphere):
        """
            a method that allows you to change the scope of activities of employees belonging to this class.
        """
        cls.sphere = new_sphere

    @staticmethod
    def info_by_id(id: str):
        """
            a method that takes the id of employee as an argument.
            returns detailed info about this employee.
            First 4 indices(0,1,2,3) in id - this will be Year of joining the company of this employee.
            4,5,6,7 indices in id - Birth year of employee.
            last index(8) in id - first letter of country where this employee lives.
        """
        if id[8] == 'U':
            return f'Year of joining the company: {id[0:4]}', f'Birth year: {id[4:8]}', f'Country of living: {id[8]}SA'
        elif id[8:9] == 'C':
            return f'Year of joining the company: {id[0:4]}', f'Birth year: {id[4:8]}', f'Country of living: {id[8]}ANADA'


class Company:
    """Class Company"""
    sphere = 'technology'

    def __init__(self, name, amount_employee, holidays_in_year, year_salaries_from, main_office_in):
        self.name = name
        self.amount_employee = amount_employee
        self.holidays_in_year = holidays_in_year
        self.year_salaries_from = year_salaries_from
        self.main_office_in = main_office_in

    def get_company_info(self):
        """method to get all company information"""
        return [self.name, self.amount_employee, self.holidays_in_year, self.year_salaries_from, self.main_office_in]

    def salaries_for_hour_from(self):
        """
            a method that takes the minimum annual salary of employees in the company as an argument.
            returns the calculated minimum wage per hour.
            Holidays and weekends are not taken into account as working days during the calculation.
        """
        saturdays_and_sundays = 104
        return (self.year_salaries_from / ((365 - self.holidays_in_year) - saturdays_and_sundays)) / 8

    @classmethod
    def set_new_sphere(cls, new_sphere: str):
        """
            a method that allows you to change the scope of activities of companies belonging to this class.
        """
        cls.sphere = new_sphere

    @staticmethod
    def info_by_id(id: str):
        """
            a method that takes the id of employee as an argument.
            returns detailed info about this employee.
            First 4 indices(0,1,2,3) in id - this will be Year of joining the company of this employee.
            4,5,6,7 indices in id - Birth year of employee.
            last index(8) in id - first letter of country where this employee lives.
            Note: if index(8) is "H" letter - this means that id of this company belongs to hackers
             and their info about location(country) is absent.
        """
        if id[8] == 'H':
            return f'Company was created in the: {id[0:4]} year', f'The company went public in: {id[4:8]}',\
                   f'Direct of company: {id[8:9]}acking'
        elif id[8:9] == 'C':
            return f'Year of joining the company: {id[0:4]}', f'Birth year: {id[4:8]}',\
                   f'Country of living: {id[8]}ANADA'



Elon_Musk = Employee('Elon', 50, 'Python Dev', 'Posting of funny Tweets')
Bill_Gates = Employee('Bill', 67, 'Java Dev', 'Creating of vaccinations')
Richard_Branson = Employee('Richard', 71, 'Java Script Dev', 'Creating of troubles')

Edward_Snowden = Employee('Edward', 39, 'Hacker', 'Hacking')
Kaspersky = Employee('Johny', 45, 'Viruses Developer', 'Developing of the viruses')


Dev_Avengers = Company('Avengers', 3, 15, 1000000, 'USA')
Secure_Hackers = Company('Secure-Hackers', 2, 10, 250000, 'Secreted')


print(Secure_Hackers.salaries_for_hour_from())
print(Kaspersky.info_by_id('20121997C'))
print(Secure_Hackers.info_by_id('20022013HIT'))
