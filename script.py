import csv

with open('Breast_cancer_data.csv') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)
