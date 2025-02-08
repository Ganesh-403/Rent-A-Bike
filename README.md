# Bike Rental System  

# Overview  
The **Bike Rental System** is a Python-based terminal application that allows users to rent and return bikes on a **daily** or **weekly** basis. It includes features like stock management, rental cost calculation, and a **family discount** for renting multiple bikes.  

# Features  
- **Check Stock Availability** – View available bikes before renting.  
- **Rent Bikes** – Choose the number of bikes and rental duration.  
- **Return Bikes** – Calculate the total bill and update stock.  
- **Discounts** – Get a **30% family discount** when renting 3 to 5 bikes.  
- **Error Handling** – Ensures valid input for rental details.  
- **Exit Option** – Allows users to quit the system anytime.  

# How It Works  
1. The system starts with an **initial stock** of bikes.  
2. Users can **rent bikes** by specifying:  
   - The number of bikes.  
   - The rental basis (**daily** or **weekly**).  
   - The duration of the rental.  
3. Users can **return bikes**, and the system will:  
   - Calculate the total bill.  
   - Apply the **family discount** if applicable.  
   - Update the available stock.  
4. Users can **exit the system** at any time.  

# Installation  
No external dependencies are required. Simply run the Python script in a terminal.  

```
python bike_rental.py
```  

# Usage  
1. **Run the script** in a terminal or VS Code.  
2. **Follow the prompts** to rent, return, or exit the system.  

# Example  
```
Would you like to rent or return bikes? (rent/return/exit): rent  
Enter the number of bikes to rent: 3  
Enter the rental basis (daily/weekly): daily  
Enter the number of days for the rental: 2  

You have successfully rented 3 bikes.  
```

```
Would you like to rent or return bikes? (rent/return/exit): return  
Enter the number of bikes to return: 3  
Enter the rental basis (daily/weekly): daily  
Enter the number of days the bikes were rented: 2  

Family rental discount applied: 30%  
Total bill: ₹2100  
3 bikes have been returned. Current stock: 100  
```

# License  
This project is open-source and free to use.  
