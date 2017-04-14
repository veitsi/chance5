import cards

fo=open("base.js","w")
fo.write("var base=[")
for card in cards.base:
        # print(card)
        smiley = card['smiley'] if card['type']=='event' else ''
        text=card['type']+" "+smiley+" "+card['en_title']+": "+card['en']
        print(text)
        fo.write('"'+text+'",')
fo.write("];")
fo.close()

