class Payroll:
    def __init__(self,desc,date,charge,id):
        self.__desc = desc
        self.__date = date
        self.__charge = charge
        self.__id = id

    def return_desc(self):
        return self.__desc

    def return_date(self):
        return self.__date

    def return_charge(self):
        return self.__charge

    def return_id(self):
        return self.__id


        