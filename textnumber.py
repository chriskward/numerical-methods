
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
        if not (isinstance(a,int) or isinstance(a,float)) : raise TypeError('Number must be int or float')
        if num >= max_value : raise ValueError(f'Number must be less than {max_value}')

        num = [int(i) for i in list(str(num))]
        dec = list()

        if '.' in num :
                dec = num[num.index('.')+1: ]
                num = num[:num.index('.')]

        
