a=0.1+0.2
c=0.3
d=c-a
absolute_error=abs(d)
rel_error=(absolute_error)/c
per_error=(rel_error)*100
print(f"Absolute error : {absolute_error}")
print(f"Relative error : {rel_error}")
print(f"Percentage error : {per_error}")
