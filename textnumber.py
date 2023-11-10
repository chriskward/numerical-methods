
# lookup tables for all the distinct word forms required
# to spell numbers in english

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
	"""
	textnumber(num: int/float) -> str

	textnumber(1052.9) -> "one thousand and fifty two point nine"

	Returns a text representation of a number in British English 
	"""


	# the largest number that can be parsed depends on the number of
	# entries in the iteration dict. At present 4 entries; 9,999,999,999

	max_value = 10**(3*len(iteration))
	if not (isinstance(num,int) or isinstance(num,float)) : raise TypeError('Number must be int or float')
	if num >= max_value : raise ValueError(f'Number must be less than {max_value}')

	num = list(str(num))
	dec = list()

	# if the number contains a decimal point, split into
	# whole number and fractional part

	if '.' in num :
		dec = num[num.index('.')+1 :]
		num = num[: num.index('.')]

	# we split whole number part into groupings of three as per the
	# usual British English pronunciation.
	#
	# eg 85,102,950 -> eighty five <MILLION> one hundred and two <THOUSAND> nine hundred and fifty

	# append leading zeros as padding if required

	while len(num)%3 != 0:
		num.insert(0,'0')

	segmented_num = list()

	# split str: num
	# noting that for any number less than 19 the digits must be grouped
	#
	# 124 - one / <hundred and> / twenty / four
	# 114 - one / <hundred and> / fourteen       NOT one hundred and ten four

	while len(num) > 0:

		units_part = int(num[-2]+num[-1])

		if units_part >=10 and units_part <=19:
			segmented_num.append(( num[-3] , '0' , num[-2]+num[-1] ))

		elif units_part <10:
			segmented_num.append(( num[-3] , '0' , num[-1] ))

		else:
			segmented_num.append(( num[-3] , num[-2] , num[-1] ))

		del num[-3:]

	# reverse the order of the list
	
	segmented_num = segmented_num[::-1]

	decimal_out = str()
	
	# if the number has a decimal part, parse that now. This is much
	# simpler as, for numbers after the decimal we just need to append the 
	# name of each digit to the output string
	#
	# 0.124 -> zero point one two four     NOT zero point one hundred and twenty four


	if len(dec)>0:
		decimal_out = ' point'
		for s in dec:
			decimal_out += ' ' + units_lookup[s]

	
	number_list = list()
	iterate_counter = 0
	segments = len(segmented_num)

	while len(segmented_num) > 0:

		temp_string = str()
		num_part = segmented_num.pop()

		hundreds,tens,units = units_lookup[num_part[0]] , tens_lookup[num_part[1]] , units_lookup[num_part[2]]

		# the logic of exactly how to parse the number is somewhat convoluted
		# the code below follows standard British English pronunciation rules
		# and adds 'and' in the correct places
		#
		# the positioning of 'and' depends on the surrounding digits
		# more illumiating and explanatory comments will be added here later

		if hundreds == 'zero':
			if tens == '':
				temp_string = units
			elif tens != '' and units == 'zero':
				temp_string = tens
			elif tens != '' and units != 'zero':
				temp_string = tens + ' ' + units
			if segments > 1 and iterate_counter ==0:
				if temp_string != 'zero' :
					temp_string = 'and ' + temp_string
				else: temp_string = ''
				
		if hundreds != 'zero':
			if tens == '' and units == 'zero':
				temp_string = hundreds + ' hundred'
			elif tens == '' and units != 'zero':
				temp_string = hundreds + ' hundred and ' + units
			elif tens != '' and units == 'zero':
				temp_string = hundreds + ' hundred and ' + tens
			elif tens != '' and units != 'zero':
				temp_string = hundreds + ' hundred and ' + tens + ' ' + units
		
		if temp_string == 'zero' and segments > 1 : temp_string = ''
		
		if temp_string != '' and iterate_counter >0 : temp_string += ' ' + iteration[str(iterate_counter)]        
		
		number_list.append(temp_string)    
		iterate_counter +=1
		
	number_out = str()
	
	# number_list is in reverse order and will, as a byproduct of the 
	# code above, contain a number of extra spaces (elimiating this at source
	# would lead to much less readable code above).

	while len(number_list)>0:
		x = number_list.pop()
		if x != '': 
			number_out += x
			if len(number_list)>0 : number_out += ' '
	
	return number_out + decimal_out









	   


	
