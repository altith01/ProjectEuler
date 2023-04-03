# Returns number in word format (no spaces/hyphens)
# Works up to nonillions

def num_to_word(n):
    group = 1
    num = n
    string = ''
    while num != 0:
        part = num % 1000
        if group == 2:
            string = 'thousand' + string
        elif group == 3:
            string = 'million' + string
        elif group == 4:
            string = 'billion' + string
        elif group == 5:
            string = 'trillion' + string
        elif group == 6:
            string = 'quadrillion' + string
        elif group == 7:
            string = 'quintillion' + string
        elif group == 8:
            string = 'sextillion' + string
        elif group == 9:
            string = 'septillion' + string
        elif group == 10:
            string = 'octillion' + string
        elif group == 11:
            string = 'nonillion' + string
        if (part//10) % 10 == 1:
            if part % 10 == 0:
                string = 'ten' + string
            elif part % 10 == 1:
                string = 'eleven' + string
            elif part % 10 == 2:
                string = 'twelve' + string
            elif part % 10 == 3:
                string = 'thirteen' + string
            elif part % 10 == 4:
                string = 'fourteen' + string
            elif part % 10 == 5:
                string = 'fifteen' + string
            elif part % 10 == 6:
                string = 'sixteen' + string
            elif part % 10 == 7:
                string = 'seventeen' + string
            elif part % 10 == 8:
                string = 'eighteen' + string
            elif part % 10 == 9:
                string = 'nineteen' + string
        else:
            if part % 10 == 1:
                string = 'one' + string
            elif part % 10 == 2:
                string = 'two' + string
            elif part % 10 == 3:
                string = 'three' + string
            elif part % 10 == 4:
                string = 'four' + string
            elif part % 10 == 5:
                string = 'five' + string
            elif part % 10 == 6:
                string = 'six' + string
            elif part % 10 == 7:
                string = 'seven' + string
            elif part % 10 == 8:
                string = 'eight' + string
            elif part % 10 == 9:
                string = 'nine' + string
            if (part//10) % 10 == 2:
                string = 'twenty' + string
            elif (part // 10) % 10 == 3:
                string = 'thirty' + string
            elif (part // 10) % 10 == 4:
                string = 'forty' + string
            elif (part // 10) % 10 == 5:
                string = 'fifty' + string
            elif (part // 10) % 10 == 6:
                string = 'sixty' + string
            elif (part // 10) % 10 == 7:
                string = 'seventy' + string
            elif (part // 10) % 10 == 8:
                string = 'eighty' + string
            elif (part // 10) % 10 == 9:
                string = 'ninety' + string
        if part//100 != 0:
            if part % 100 != 0:
                string = 'and' + string
            string = 'hundred' + string
        if part//100 == 1:
            string = 'one' + string
        elif part//100 == 2:
            string = 'two' + string
        elif part//100 == 3:
            string = 'three' + string
        elif part//100 == 4:
            string = 'four' + string
        elif part//100 == 5:
            string = 'five' + string
        elif part//100 == 6:
            string = 'six' + string
        elif part//100 == 7:
            string = 'seven' + string
        elif part//100 == 8:
            string = 'eight' + string
        elif part//100 == 9:
            string = 'nine' + string
        num = num//1000
        group += 1
    return string
