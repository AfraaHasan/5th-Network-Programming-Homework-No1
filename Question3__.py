#python quiz program that takes a text file ("question_answer_file.text")as input

import Question3___
def read_file(file_name):
    r= open("question_answer_file.text","r")
    list_r=[line.rstrip().split(";") for line in r]
    return list_r
    r.close()

Q_A=read_file("question_answer_file.text")

print ("welcom^-^\nQuiz the capitale city of Arabic contries\nenter (stop) if you get bored\n")
print("(help box:Mogadishu,Cairo,Muscat,Riyadh,Nouakchott,Damascus,Doha,Khartoum,Amman,Alquds\n,"
      "Sana'a,Kuwait,Tunis,Manama,Tripoli,Beirut,Baghdad,Algiers,Abudhabi,Rabat)\n")
print("Let's start:")
user_name =input("please enter your name :")

User_result_file = open("User_result_file.text","w")
User_result_file . write(user_name+"\n")
User_result_file = open("User_result_file.text", "a")

points=0
for i in range(0,20):
    answ=input(Q_A[i][0])
    answ= answ.capitalize()
    if answ=="Stop":
        break

    if answ==Q_A[i][1]:
        points=points+1
        User_result_file.write("{}\n the answeris:{}\n your answer is correct\n".format(Q_A[i][0], Q_A[i][1]))

    else:
        User_result_file.write("{}\nyour answer {} is wrong,the right answer is:{}\n".format(Q_A[i][0],answ, Q_A[i][1]))

User_result_file.write("you scord {} points".format(points))
User_result_file.close()
print(open("User_result_file.text","r").read())
User_result_file.close()















