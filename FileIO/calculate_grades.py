def calculate_grades(row):
    row = row[:-1]
    name, q1, q2, q3 = row.split(",")
    avg = (int(q1) + int(q2) + int(q3))/3
    if avg > 50:
        mystr = "{} -> {}-{}-{}: {} | PASSED!".format(name,q1,q2,q3,avg)
        print(mystr)
        wfile = open("passed.txt","a",encoding="utf-8")
        wfile.write(mystr+"\n")
        wfile.close()
    else:
        mystr = "{} -> {}-{}-{}: {} | FAILED!".format(name,q1,q2,q3,avg)
        print(mystr)
        wfile = open("failed.txt", "a", encoding="utf-8")
        wfile.write(mystr+"\n")
        wfile.close()


with open("dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        calculate_grades(i)
