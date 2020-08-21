

        


customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

for idx in range(len(customers)):
    tax_rate = taxes[idx]/salary[idx]
    high_salary = salary[idx]>555000
    low_tax = tax_rate<0.3
    if high_salary and low_tax:
        print(customers[idx])

# This_customer = "james"    
# This_salary = 155000
# This_taxes = 55800

# tax_rate = This_taxes/This_salary
# high_salary = this_salary>555000
# low_tax = tax_rate<0.3
# if high_salary and low_tax:
#     print(this_customers)




