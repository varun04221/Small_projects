def questionnaire():
    emotions={"Happy":0,"Sad":0,"Angry":0,"Neutral":0}
    d=list(emotions.keys())
    final_emotion=""
    q1=int(input("On a scale of 1-10 how would you rate your day today, 10 being very nice and 1 being very sad:"))
    if q1>=8:
        emotions["Happy"]+=4
        emotions["Sad"] +=0
        emotions["Angry"]+=0
        emotions["Neutral"] +=1
    elif q1 >=5 and q1<8:
        emotions["Happy"]+=2
        emotions["Sad"] +=0
        emotions["Angry"]+=2
        emotions["Neutral"] +=2
    elif q1<5 and q1>=3:
        emotions["Happy"]+=1
        emotions["Sad"] +=2
        emotions["Angry"]+=2
        emotions["Neutral"] +=1
    else:
        emotions["Happy"]+=0
        emotions["Sad"] +=4
        emotions["Angry"]+=2
        emotions["Neutral"] +=1
    
    q3=int(input("Did something happen wtih you today which made you upset. Rate on a scale of 1-10 where 10 being very upset and 1 being happy:"))
    if q3>=8:
        emotions["Happy"]+=0
        emotions["Sad"] +=4
        emotions["Angry"]+=0
        emotions["Neutral"] +=0
    elif q3 >=5 and q3<8:
        emotions["Happy"]+=0
        emotions["Sad"] +=2
        emotions["Angry"]+=2
        emotions["Neutral"] +=2
    elif q3<5 and q3>=3:
        emotions["Happy"]+=2
        emotions["Sad"] +=1
        emotions["Angry"]+=1
        emotions["Neutral"] +=1
    else:
        emotions["Happy"]+=4
        emotions["Sad"] +=0
        emotions["Angry"]+=1
        emotions["Neutral"] +=2

    q4=int(input("Did something happen with you today which made you angry. Rate on a scale of 1-10 where 10 being very angry and 1 being not at all angry:"))
    if q4>=8:
        emotions["Happy"]+=0
        emotions["Sad"] +=0
        emotions["Angry"]+=4
        emotions["Neutral"] +=0
    elif q4 >=5 and q4<8:
        emotions["Happy"]+=0
        emotions["Sad"] +=1
        emotions["Angry"]+=2
        emotions["Neutral"] +=2
    elif q4<5 and q4>=3:
        emotions["Happy"]+=1
        emotions["Sad"] +=1
        emotions["Angry"]+=2
        emotions["Neutral"] +=2
    else:
        emotions["Happy"]+=2
        emotions["Sad"] +=1
        emotions["Angry"]+=0
        emotions["Neutral"] +=4

    q5=int(input("Did something happen with you today which made you feel happy. Rate on a scale of 1-10 where 10 being very happy and 1 being not at all:"))
    if q5>=8:
        emotions["Happy"]+=4
        emotions["Sad"] +=0
        emotions["Angry"]+=0
        emotions["Neutral"] +=2
    elif q5 >=5 and q5<8:
        emotions["Happy"]+=2
        emotions["Sad"] +=1
        emotions["Angry"]+=1
        emotions["Neutral"] +=2
    elif q5<5 and q5>=3:
        emotions["Happy"]+=1
        emotions["Sad"] +=2
        emotions["Angry"]+=2
        emotions["Neutral"] +=1
    else:
        emotions["Happy"]+=0
        emotions["Sad"] +=4
        emotions["Angry"]+=2
        emotions["Neutral"] +=1

    emotion_index_list=list(emotions.values())
    emotion_index_list.sort(reverse=True)
    emo_var=emotion_index_list[0]

    for i in emotions:
        if emotions[i] == emo_var:
            final_emotion=i

    return final_emotion

def mmenu():
    print("""Please Select from the following options which best describes your mood right now
    1.Happy
    2.Sad
    3.Angry
    4.Neutral
    5.I don't know
    """)
    while True:
        n=int(input("Please Enter the number corresponding to selected choice:"))
        if 1<=n<=5:
            break
        else:
            print("Please Enter a valid Input!!!")
    if n==1:
        return "Happy"
    elif n==2:
        return "Sad"
    elif n==3:
        return "Angry"
    elif n==4:
        return "Neutral"
    else:
        return 5

def smenu():
    print("""Since you didn't give an apporopiate input, would you like to choose from the following options 
    1. Fill up a questionnaire
    2. Click a photograph
    """)
    while True:
        n=int(input("Please Enter the number corresponding to selected choice:"))
        if 1<=n<=2:
            break
        else:
            print("Please Enter a valid Input!!!")
    return n