graduated_students =["Afraa Hasan","Reem Ali","Ali Ahmad","Ruba Mahmoud","Alaa Zedan","Karam Ammar"]
student_name =input("please enter your name :")
student_name =student_name.title()
if student_name in graduated_students:
    print("congratuatios ,you graduate")
else:
    print("you did not graduate ")
