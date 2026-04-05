profile = { "name": "Vansh",
           "age": 21,
           "current_salary": 12000,
           "target_salary": 50000,
           "skills": ["Python","Sql","Power BI","Excel"],
           "employed": True}

print(f"Name: {profile['name']}")
print(f"current salary: {profile['current_salary']}")
print(f"target salary: {profile['target_salary']}")

print(f"current skills:{profile['skills']}")

# Adding a new skill
profile['skills'].append("Ai API")
print(f"Updated skills: {profile['skills']}")

# adding a new key-value pair
profile['github']="github.com/VanshMotla"
print(f"Github profile: {profile['github']}")

# Loop through all skills

print("\n-------MY Skills-------")
for skill in profile['skills']:
    print(f"- {skill}")

# What happens if key doesn't exist
#print(profile['twitter'])

# This is safe — returns None if key doesn't exist

print(profile.get('twitter'))

# Even better — return a default value if key doesn't exist
print(profile.get('twitter', 'Twitter profile not available'))