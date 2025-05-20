students =[
    {"name": "Ajay","house": "Fullstack", "type":'Senior'},
    {"name":"Vinod","house":"Fullstack","type":'MidSenior'},
    {"name": "Aditya", "house": "Fullstack", "type": None},
]

for student in students:
      print(student["name"], student["house"], student["type"], sep=", ")