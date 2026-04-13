# Print skills in numbered format
skills=['Python', 'Java', 'AI', 'SQL', 'RPA', 'Xceptor']

skills_to_add=['ML','Data Science','Deep Learning']

counter=1

for skill in skills_to_add:
    skills.append(skill)

skills_to_remove=['SQL','RPA','testing']
skills_Not_in_list=[]

for skill in skills_to_remove:
    if skill in skills:
        skills.remove(skill)
    else:
        skills_Not_in_list.append(skill)
        

print(f"Skills Not in List: ")
for index, skill in enumerate(skills_Not_in_list, start=1):
    print(f"{index} - {skill.capitalize()}")

print(f"My Skills are:")
for index , skill in enumerate(skills, start=1):
    # if counter==5:
    #     break
	
    print(f"{index} - {skill.capitalize()}")
    counter+=1