# employee_details={
# 	"name":"Veeresh",
# 	"role":"AI Engineer",
# 	"exp":11,
# 	"location":"Banglaore"
	
# }
# print(f"My Name is {employee_details['name']}")

# for key, value in employee_details.items():
#     print(f"My {key} is {value}")  

team=[

{
	"name":"Veeresh",
	"role":"AI Engineer",
	"experience":11,
	"location":"Bangalore"
},
{
	"name":"Hari",
	"role":"Developer",
	"experience":5,
	"location":"Bangalore"
},
{
	"name":"Krishna",
	"role":["Tester","Developer"],
	"experience":8,
	"location":"Chennai"
},
{
	"name":"Raju",
	"role":["BA","Developer","Tester"],
	"experience":13,
	"location":"Bangalore"
},
{
	"name":"Thanuja",
	"role":["Developer"],
	"experience":3,
	"location":"Hyderabad"
}
]

seniorCount=0
midLevelCount=0
juniorCount=0

print("Employee Details\n")
for member in team:
    exp=member["experience"]
    if exp>=10:
        member["level"] = "Senior"
        seniorCount+=1
    elif exp>=5:
        member["level"] = "Mid-Level"
        midLevelCount+=1
    else:
        member["level"] = "Junior"
        juniorCount+=1
    if member["location"]=="Bangalore":
        for key, value in member.items():
            if isinstance(value, list):
                print(f"{key} : {', '.join(value)}")
            else:
            	print(f"{key} : {value}")
print("-"*30)		


print(f"Total Employees: {len(team)}")
print(f"Total Senior Employees: {seniorCount}")
print(f"Total Mid-Level Employees: {midLevelCount}")
print(f"Total Junior Employees: {juniorCount}")
