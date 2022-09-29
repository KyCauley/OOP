import EmployeeClass as E
import PayrollDeductionClass as P

employee = E.Employee('Jimmy Smith',58475,'Informations Systems','Developer',6800.00)

transaction1 = P.Payroll("food court","8/14/2022",22.50,39119)
transaction2 = P.Payroll("gift contribution","8/12/2022",25.00,58475)
transaction3 = P.Payroll("food court","8/17/2022",15.25,21547)
transaction4 = P.Payroll("vending machine","8/22/2022",3.00,58475)
transaction5 = P.Payroll("vending machine","8/5/2022",2.75,58475)

transactions = [transaction1,transaction2,transaction3,transaction4,transaction5]

totaldeduct = 0
for record in transactions:
    if record.return_id() == employee.emp_id():
        totaldeduct = totaldeduct + record.return_charge()

NetPay = employee.emp_salary() - totaldeduct
    
employee.report_1()
print("Net Pay: ",'$',format(NetPay,',.2f'))