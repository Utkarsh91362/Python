from datetime import date
#today= date.today()
name = input(" Enter your Name: ")
letter ='''Dear  <|Name|>
                You are  selected!
                <|Date|>'''

print(letter.replace("<|Name|>", name).replace("<|Date|>", str(date.today())))

