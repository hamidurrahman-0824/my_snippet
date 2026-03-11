string = 'we li"ve in a country where only syncdicate live"s!'
fresh = ' '.join(''.join(ch for ch in w if ch.isalpha()) for w in string)
print(fresh)
