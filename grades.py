project=int(input("enter project marks:"))
internal=int(input("enter internal marks:"))
external=int(input("enter external marks:"))
failures = []
if project < 50:
   failures.append("Failed in project")
if external < 50:
   failures.append("Failed in external")
if internal < 50:
   failures.append("Failed in internal")
if failures:
   print(" ; ".join(failures))
else:
   total=(70/100)*project+(10/100)*internal+(20/100)*external
   print(f"total score:{total}")
   if total>90:
       print(" A grade")
   elif total>80:
       print("B grade")
   else:
       print("c grade")
