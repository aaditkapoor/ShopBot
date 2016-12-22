# Main processing file

import random


positive_texts = ["This product is the best in the world!", "Many of your friends also like it", "Give it a try! It also has replacement gurantee",
"Don't be shy! Trust me", "I have seen the reviews of it.Will provide you comparison chart shortly.", "The best quality at the best price","Buy it before it is finished!"]


convincing_methods = [

"Buy this product! I have analysed my sources and this product is best in class.",
"Come on! Don't be shy!",
"30 day replacement gurrantee",
"Buy before it is finished",
"Buy at a discount! Take it",
"Your friends also have bought this."
"The sentiment analysis of the reviews are positive."
]






def get_combined_text():
	global positive_texts
	global convincing_methods


	s = positive_texts[random.randint(0,len(positive_texts))]
	s+=" "
	s+=convincing_methods[random.randint(0, len(convincing_methods))]

	return s
