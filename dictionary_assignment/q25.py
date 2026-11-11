print("Given a nested dictionary of students and their subject marks, calculate each student's total marks and find the topper.")
student = {
    'a':{
        'm1':50,
        'm2':60
    },
    'b' : {
        'm1':70,
        'm2':80
    }
}
max = 0
topper = ""
for key in student:
    total = 0
    for keys in student[key]:
        total+=student[key][keys]
    #print(total)

    if total >max:
        max = total
        topper = key
print(max)
print(topper)
