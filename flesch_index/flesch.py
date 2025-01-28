f=open('football.txt','r')
num_words=0
num_syllables=0
num_sentence=0
sentence_end=['.','!','?',':',';']
vowels=['a','e','i','o','u']
pair_vowels=[]
for i in vowels:
    for j in vowels:
        pair_vowels.append(i+j)
txt=f.read()
words=txt.split()
num_words+=len(words)
for i in txt:
    if i in sentence_end:
        num_sentence+=1
    if len(i)<=3:
       num_syllables+=1
    elif i in vowels:
        num_syllables+=1
    elif i in pair_vowels:
        num_syllables+=1
    elif i.endswith(('es','ed')):
        num_syllables-=1
    elif i.endswith('e') and not(i.endswith('le')):
        num_syllables-=1
#sentences=txt.split(sentence_end)
#num_sentence+=len(sentences)
#print("Pair Vowels : ",pair_vowels)
print("No of words =",num_words)
print("No of sentences =",num_sentence)
print("No of syllables =",num_syllables)

F_Index = 835.206 - (1.015*(num_words/num_sentence)) - (84.6*(num_syllables/num_words))
print("Flesch Index : ",F_Index)
Grade = 0.39*(num_words/num_sentence) + (11.8*(num_syllables/num_words)) - 15.59
print("Grade : ",Grade)
if 0<Grade<=30:
    print("College")
elif 50<Grade<=60:
    print("High School")
elif 90<Grade<=100:
    print("Fourth Grade")
else:
    print("Index out of range 0-100")