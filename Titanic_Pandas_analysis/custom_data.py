import pandas as pd

data = {
    "Name": [
        "Ali","Sara","John","Lina","David",
        "Marta","Samuel","Helen","Noah","Eva",
        "Daniel","Sophia","Lucas","Amir","Nora"
    ],
    "Age": [22,21,23,20,24,22,25,21,19,23,24,20,22,26,21],
    "Department": [
        "CS","IT","CS","SE","IT",
        "CS","SE","IT","CS","SE",
        "IT","CS","SE","CS","IT"
    ],
    "GPA": [
        3.2,3.8,3.0,3.5,3.1,
        3.6,3.3,3.9,2.9,3.4,
        3.2,3.7,3.0,3.1,3.6
    ],
    "Year": [
        "3rd","2nd","3rd","1st","4th",
        "2nd","3rd","1st","2nd","4th",
        "3rd","1st","2nd","4th","3rd"
    ]
}

labels=  [
    "S1","S2","S3","S4","S5",
    "S6","S7","S8","S9","S10",
    "S11","S12","S13","S14","S15"
]

df = pd.DataFrame(data, index = labels)

print("Student Dataset: \n")
print(df)