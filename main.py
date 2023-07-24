#QAP4 Project1 Program 2
#Create a program to record monthly sales
#and plot them on a graph.
#Tina Rowe
#Program written July 23, 2023

#Import libraries
import matplotlib.pyplot as plt

# Create a graph to show monthly sales.
MthSales = []
Months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# Enter the sales for each month
January = float(input("Enter the total sales for January. If there are none enter 0: "))
MthSales.append(January)
February = float(input("Enter the total sales for February. If there are none enter 0: "))
MthSales.append(February)
March = float(input("Enter the total sales for March. If there are none enter 0: "))
MthSales.append(March)
April = float(input("Enter the total sales for April. If there are none enter 0: "))
MthSales.append(April)
May = float(input("Enter the total sales for May. If there are none enter 0: "))
MthSales.append(May)
June = float(input("Enter the total sales for June. If there are none enter 0: "))
MthSales.append(June)
July = float(input("Enter the total sales for July. If there are none enter 0: "))
MthSales.append(July)
August = float(input("Enter the total sales for August. If there are none enter 0: "))
MthSales.append(August)
September = float(input("Enter the total sales for September. If there are none enter 0: "))
MthSales.append(September)
October = float(input("Enter the total sales for October. If there are none enter 0: "))
MthSales.append(October)
November = float(input("Enter the total sales for November. If there are none enter 0: "))
MthSales.append(November)
December = float(input("Enter the total sales for December. If there are none enter 0: "))
MthSales.append(December)

plt.plot(Months, MthSales)

plt.xlabel("Months")
plt.ylabel("Monthly Sales")

plt.title("Sales Revenue by Month")
plt.grid(True)

plt.show()





