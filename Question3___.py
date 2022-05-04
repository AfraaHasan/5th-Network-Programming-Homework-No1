#creat a text file(question_answer)to use it as input for a python quiz program
def write_file(file_name,text):
    w=open(file_name, "w")
    text=[line+"\n" for line in text]
    w.writelines(text)
    w.close()

Q_A=["q1:What is the capitale city of Syria:;Damascus","q2 :What is the capitale city of Sudan:;Khartoum",
    "q3 :What is the capitale city of Iraq:;Baghdad","q4 :What is the capitale city of Jordan:;Amman",
    "q5 :What is the capitale city of Lebanon:;Beirut","q6 :What is the capitale city of Morocco:;Rabat",
    "q7 :What is the capitale city of Tunisia:;Tunis","q8 :What is the capitale city of United Arab Emirates:;Abudhabi",
    "q9 :What is the capitale city of Yemen:;Sana'a","q10:What is the capitale city of Algeria:;Algiers",
    "q11:What is the capitale city of Bahrain:;Manama","q12:What is the capitale city of Saudi Arabia:;Riyadh",
    "q13:What is the capitale city of Egypt:;Cairo","q14:What is the capitale city of Kuwait:;Kuwait",
    "q15:What is the capitale city of Libya:;Tripoli","q16:What is the capitale city of Mauritania:;Nouakchott",
    "q17:What is the capitale city of Qatar:;Doha","q18:What is the capitale city of palestain:;Alquds",
    "q19:What is the capitale city of Somalia:;Mogadishu","q20:What is the capitale city of Oman:;Muscat"]

write_file("question_answer_file.text",Q_A)

