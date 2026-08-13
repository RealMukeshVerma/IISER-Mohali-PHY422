a=0.1+0.2
c=0.3
d=c-a
absolute_error=abs(d)
rel_error=(absolute_error)/c
per_error=(rel_error)*100
print(f"Absolute error : {absolute_error}")
print(f"Relative error : {rel_error}")
print(f"Percentage error : {per_error}")

#for user input


f=float(input("Inpute the actual value:"))
e=float(input("Inpute the calculated value:"))
g=f-e
u_absolute_error=abs(g)
u_rel_error=(u_absolute_error)/(e)
u_per_error=(u_rel_error)*100
print(f"Absolute error : {u_absolute_error}")
print(f"Relative error : {u_rel_error}")
print(f"Percentage error : {u_per_error}")
