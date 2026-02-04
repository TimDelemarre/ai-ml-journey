# Week 1: Python basics

skills = ["Python", "Git", "Immunology"]

def describe_skill(skill):
    if skill == "Python":
        return "essential for AI/ML"
    else:
        return "useful background skill"

for skill in skills:
    description = describe_skill(skill)
    print(f"{skill}: {description}")
