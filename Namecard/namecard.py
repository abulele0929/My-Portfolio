def name_card(full_name, job_title, city, skills):
    return f"""
    =============================================
    {full_name.upper()}
    {job_title.title()}
    {city.title()}
    ---------------------------------------------
    Top Skill = {skills.capitalize()}
    =============================================
    """

full_name = input("Enter your full name: ")
job_title = input("Enter your job title: ")
city = input("Enter your city: ")
skills = input("Enter your top skill: ")

print(name_card(full_name, job_title, city, skills))
