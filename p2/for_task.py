estimate_list = [{
					'school_class': '4a', 
					'scores': [3,4,4,5,2]
				}, 
				{
					'school_class': '8б',
					'scores': [4,5,4,3,5]
				},
				{
					'school_class': '1a',
					'scores': [3,5,4,2,4]
				},
				{	'school_class': '9в',
					'scores': [3,3,2,3,3]
					}]

general_score_list = []


for i in estimate_list:
	t = i['scores']
	avarage_estimate = sum(t)/len(t)
	print("Средний балл по классу ", i['school_class'], avarage_estimate)




for l in estimate_list:
	general_score_list += l['scores']
	# t = l['scores']
print("Средний бал по школе: ", sum(general_score_list) / len(general_score_list))



