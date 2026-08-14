# ============================================================
# Python Practice Program Day6
# Topic: Dictionary Operations - Indexing and Methods
# ============================================================


Profile={"name": "Vinod", "age": 46, "city": "Chennai"}
Profile["name"]="Vinod Kumar"


Profile["Skills"]="Python"

print(Profile)

# ------------------------------------------------------------
# Assignments ::create multiple dictionary in python and perform merge 
#------------------------------------------------------------   

dict_Login = {'user_id': 101, 'name': 'Alice', 'role': 'Admin'}
dict_profile = {'role': 'Manager', 'skill': 'Python'}
dict_company = {'country': 'myCompany', 'Location': 'Chennai'}

merged_dict = dict_Login | dict_profile | dict_company
print(merged_dict)
