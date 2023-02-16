import emotion,menu,songs

a=menu.mmenu()
if a==5:
    sel=menu.smenu()
    if sel==1:
        emo=menu.questionnaire()
    else:
        img=emotion.image()
        emo=emotion.imotion(img)
else:
    emo=a
print('*'*50)
print("Detected Emotion:",emo)
print('*'*50)
emo=emo.lower()
print("We made playlist for your mood. Hope you will enjoy it :)\n")
songs.suggest(emo)
print('*'*50)
print("THANK YOU!")