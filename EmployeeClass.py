class Employee:
    def __init__(self,name,id,department,title,salary):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
        self.__salary = salary

    def emp_name(self):
        return self.__name

    def emp_id(self):
        return self.__id

    def emp_depart(self):
        return self.__department

    def emp_title(self):
        return self.__title
    
    def emp_salary(self):
        return self.__salary

    def report_1(self):
        print("*** Employee Pay ***")
        print("ID Number: ",self.__id)
        print("Department: ",self.__department)
        print("Gross Pay: ",'$',format(self.__salary,',.2f'))


    