import math
 # Initialize tax slabs as a list of tuples.
        # Each tuple represents a tax slab with the format (lower_bound, upper_bound, tax_rate).
        # For example, (0, 300000, 0) means the tax rate is 0% for income up to 300,000.
class TaxCalculator:
    def __init__(self):
        self.tax_slabs = [
            (0, 300000, 0), # 0% tax for income up to 300,000
            (300001, 400000, 0.10), # 10% tax for income between 300,001 to 400,000
            (400001, 650000, 0.15), # 15% tax for income between 400,001 to 650,000
            (650001, 1000000, 0.20),  # 20% tax for income between 650,001 to 1,000,000
            (1000001, 1500000, 0.25), # 25% tax for income between 1,000,001 to 1,500,000
            (1500001, math.inf, 0.30) # 30% tax for income above 1,500,000
        ]

    def calculate_tax_by_slab(self, taxable_income):
        tax = 0  # Initialize the tax to 0
        for slab in self.tax_slabs: # 15% tax for income between 400,001 to 650,000
            if taxable_income <= slab[1]:  # Check if the taxable income falls within the current slab
                tax += (taxable_income - slab[0]) * slab[2] # Calculate tax using the formula: (taxable_income - lower_bound) * tax_rate
                break
            tax += (slab[1] - slab[0]) * slab[2]    # Exit the loop since tax calculation is complete
        return tax

class Employee:
    def __init__(self, name, organization_type, salary, nppf_deductible, gis_deductible, num_children): # Initialize the employee attributes
        self.name = name  # Employee's name
        self.organization_type = organization_type  # Type of organization (e.g., Government, Private, Corporate)
        self.salary = salary # Annual salary of the employee.
        self.nppf_deductible = nppf_deductible # Deductible amount for Pension Scheme/Provident Fund (PF)
        self.gis_deductible = gis_deductible  # Deductible amount for Group Insurance Scheme (GIS)
        self.num_children = num_children  #Number of children the employee has.

    def calculate_tax(self, tax_calculator):
         # Calculate the taxable income by subtracting deductions from the salary
        taxable_income = self.salary - self.nppf_deductible - self.gis_deductible - self.num_children * 350000  
        # Use the TaxCalculator object to calculate tax based on the taxable income
        tax = tax_calculator.calculate_tax_by_slab(taxable_income) 
        # Apply a surcharge of 10% if the taxable income is greater than 1,000,000
        if taxable_income > 1000000:
            tax += tax * 0.1
        return tax

def main():
    # Prompt the user to input employee details
    name = input("Enter the employee's name: ")
    organization_type = input("Enter the employee's organization type (Government, Private, Corporate): ").lower() # Determine if the employee is a contract employee
    is_contract = input("Is the employee a contract employee? (yes/no): ").lower() in ['yes', 'y']
    salary = float(input("Enter the annual salary: ")) # Input the annual salary of the employee
    nppf_deductible = float(input("Enter the NPPF deductible: ")) # Input the NPPF deductible amount
    gis_deductible = float(input("Enter the GIS deductible: ")) # Input the GIS deductible amount
    num_children = int(input("Enter the number of children: ")) # Input the number of children the employee has.

    employee = Employee(name, organization_type, salary, nppf_deductible, gis_deductible, num_children) # Create an instance of the Employee class with the provided employee details
    tax_calculator = TaxCalculator() # Create an instance of the TaxCalculator class
    tax = employee.calculate_tax(tax_calculator) # Calculate the tax for the employee using the TaxCalculator object

    print(f"The tax for {employee.name} is: {tax}") # Print the calculated tax for the employee

if __name__ == "__main__":  # Call the main function to start the program execution
    main()
