actual_value = float(input('Enter the actual Value of property'))
assessment_value = 0.6*actual_value
assessment_tax_rate = 72/10000
total_assessment_tax = assessment_tax_rate* assessment_value
print('The assessment value is',assessment_value)
print('Total property tax is %.2f' %total_assessment_tax)