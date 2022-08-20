
units_lookup = {'0' : 'zero',   '1'  : 'one',   '2'  : 'two',
        '3' : 'three',  '4'  : 'four',  '5'  : 'five',
        '6' : 'six',    '7'  : 'seven', '8'  : 'eight',
        '9' : 'nine',   '10' : 'ten',   '11' : 'eleven',
        '12': 'twelve',         '13' :'thirteen',
        '14' : 'fourteen',      '15' : 'fifteen',
        '16' : 'sixteen',       '17' : 'seventeen',
        '18' : 'eighteen',      '19' : 'nineteen'}

tens_lookup = {'0':'', '1' : '', '2' : 'twenty', '3' : 'thirty',
        '4' : 'fourty',  '5' : 'fifty',  '6' : 'sixty',
        '7' : 'seventy', '8' : 'eighty', '9' : 'ninety'}

iteration = {'0' : '', '1': 'thousand', '2' : 'million', '3' : 'billion'}


def textnumber(num):

    max_value = 10**(3*len(iteration))
    if not (isinstance(num,int) or isinstance(num,float)) : raise TypeError('Number must be int or float')
    if num >= max_value : raise ValueError(f'Number must be less than {max_value}')

    num = list(str(num))
    dec = list()

    if '.' in num :
        dec = num[num.index('.')+1 :]
        num = num[: num.index('.')]

    while len(num)%3 != 0:
        num.insert(0,'0')

    segmented_num = list()

    while len(num) > 0:

        units_part = int(num[-2]+num[-1])

        if units_part >=10 and units_part <=19:
            segmented_num.append(( num[-3] , '0' , num[-2]+num[-1] ))

        elif units_part <10:
            segmented_num.append(( num[-3] , '0' , num[-1] ))

        else:
            segmented_num.append(( num[-3] , num[-2] , num[-1] ))

        del num[-3:]


    decimal_string = str()
    for s in dec:
        decimal_string += units_lookup[s] + ' '


    number_string = str()
    iterate_counter = 0

    while len(segmented_num) > 0:

        temp_string = str()
        num_part = segmented_num.pop()

        hundreds,tens,units = units_lookup[num_part[0]] , tens_lookup[num_part[1]] , units_lookup[num_part[2]]

        if hundreds == 'zero':
            temp_string = tens + units

            if iterate_counter == 0 and len(segmented_num) >=0:
                temp_string = ' and ' + temp_string

        else:
            temp_string = hundreds + ' hundred and'
            temp_string += ' ' + tens + ' ' + units
        
        temp_string += ' ' + iteration[ str(iterate_counter) ]
        number_string = temp_string + ' ' + number_string

        iterate_counter +=1 











       


    
