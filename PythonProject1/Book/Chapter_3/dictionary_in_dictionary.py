import pprint # красиво друкує данні

people = {}
people['Ford'] = {'name':'Genry Ford', 'Gender':'Male', 'Country':'USA','Occupation':'Driver'}
people['Mercedes'] = {'name':'Mercedes Benz', 'Gender':'Male', 'Country':'Germany','Occupation':'Driver'}
people['BMW'] = {'name':'BMW M3', 'Gender':'Male', 'Country':'Germany','Occupation':'Driver'}
people['Toyota'] = {'name':'Toyota Corolla', 'Gender':'Female', 'Country':'Japan','Occupation':'Driver'}
people['Honda'] = {'name':'Honda Civic', 'Gender':'Male', 'Country':'USA','Occupation':'Driver'}
people['Nissan'] = {'name':'Nissan Skyline', 'Gender':'Female', 'Country':'Japan','Occupation':'Driver'}
people['Volvo'] = {'name':'Volvo V80', 'Gender':'Male', 'Country':'Russia','Occupation':'Driver'}
people['Kia'] = {'name':'Kia Rio', 'Gender':'Male', 'Country':'India','Occupation':'Driver'}

pprint.pprint(people)
print()

pprint.pprint(people['Ford'])
print()
pprint.pprint(people['Ford']['Gender'])
