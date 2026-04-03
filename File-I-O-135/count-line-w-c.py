with open('textfile.txt','r') as file:
    sum_texted_line = 0
    sum_word = 0
    sum_character = 0
    sum_alpha_only = 0
    sum_digit = 0
    is_angram = False
    
    print()
    for line in file:

        if line.strip():
            sum_texted_line +=1
            sum_character += len(line)
            for word in line.split():
                sum_word += 1
                for ch in word:
                    if ch.isalpha():

                        sum_alpha_only +=1
                    elif ch.isdigit():
                        sum_digit += 1
    data = f"""
        Total genuine line = {sum_texted_line}
        Total word = {sum_word}
        All charcter number = {sum_character}
        Total alphabet = {sum_alpha_only}
        Total digit = {sum_digit}
        """
print(data)
#using generator
with open('textfile.txt','r') as file:
    line = sum(1 for line in file)
    print(line)
#improvements
with open('textfile.txt','r') as file:
    sum_texted_line = 0
    sum_word = 0
    sum_character = 0
    sum_alpha_only = 0
    sum_digit = 0

    for line in file:

        if line.strip():
            sum_texted_line += 1
            sum_character += len(line.rstrip('\n'))
            sum_word += len(line.split())

            for ch in line:
                if ch.isalpha():
                    sum_alpha_only += 1
                elif ch.isdigit():
                    sum_digit += 1

data = f"""
Total genuine line = {sum_texted_line}
Total word = {sum_word}
All character number = {sum_character}
Total alphabet = {sum_alpha_only}
Total digit = {sum_digit}
"""

print(data)
#
sum_alpha_only += sum(ch.isalpha() for ch in line)
sum_digit += sum(ch.isdigit() for ch in line)