def breaknumber(number):
    numberList = []
    while number > 10:
        remainder = number % 10
        numberList.append(remainder)
        number = (number - remainder) // 10
    numberList.append(number)
    return numberList

#print(breaknumber(15))
#print(breaknumber(115))
#print(breaknumber(4))
#print(breaknumber(11145555000))

digit = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten','eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero','ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
units = ['', 'thousand', 'million']

def spell_hundred(number):
    if number == 0:
        return "zero"
    str = ""
    x = number // 100 # multiple of 100
    if x > 0:
        str = digit[x] + " hundred"
    # get rest of number following hundreds place
    x = number % 100
    if x > 0:
        y = x // 10
        if y > 1: #twenty...
            str = str + " " + tens[y]
            y = x % 10
            if y > 0:
                str = str + " " + digit[y]
        elif y > 0:#eleven...
            z = x % 10
            str = str + teens[z]
        else:
            str = str + " " + digit[x]
    return str

#print(spell_hundred(5))
#print(spell_hundred(10))
#print(spell_hundred(19))
#print(spell_hundred(20))
#print(spell_hundred(21))
#print(spell_hundred(29))
#print(spell_hundred(31))
#print(spell_hundred(99))
#print(spell_hundred(115))
#print(spell_hundred(999))

def spell_number(number):
    count = 0
    str = ''
    if number == 0:
        return "Zero"
    else:
        while number > 0:
            x = number % 1000
            str = spell_hundred(x) + " " + units[count] + " " + str
            count += 1
            number = number // 1000
        return str

print(spell_number(10100962))