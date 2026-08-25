# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 17:28:22 2026

@author: shrih
"""

import re

chat1='Hello, I am having an issue with my order # 412889912'
pattern="order[^\d]*(\d*)"
matches=re.findall(pattern,chat1)
matches

#######

chat2=' I have a problem with my order number 412889912'
pattern='order number (\d*)'
matches=re.findall(pattern, chat2)
matches
###############

chat3='My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
pattern='order (\d*)'
matches=re.findall(pattern,chat3)
matches
############

import re
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)    

##########
chat1 = 'you ask lot of questions   1235678912, abc@xyz.com'
chat2 = 'here it is: (123)-567-8912, ab_c@xyz.com'
chat3 = 'yes, phone: 1235678912 email: ab.c@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*', chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#############
import re

def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
chat1 = 'Hi: you ask lot of questions   1235678912, abc@xyz.com'
chat2 = 'Hi: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Hi: yes, phone: 1235678912 email: abc@xyz.com'
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)

###########

text='''
Born	Elon Reeve Musk
June 28, 1971 (age 53)
Pretoria, South Africa
Citizenship	
South Africa
Canada
United States (from 2002)
Political party	Independent
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Domestic partner	Grimes (2018–2021)
Children	at least 14, including Vivian Wilson[1]
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)
Occupation	
Co-Founder and CEO of xAI
CEO and product architect of Tesla
Founder, CEO, and chief engineer of SpaceX
Founder of the Boring Company, X Corp., and
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
President of the Musk Foundation
De facto leader of the Department of Government 
Efficiency'''

get_pattern_match(r"age(\d+)",text)

'''
Born	Elon Reeve Musk
June 28, 1971 (age 53)
Pretoria, South Africa
Citizenship	
South Africa
Canada'''

get_pattern_match(r"Born(.*)\n",text).strip()
# after born word match all character
#dot(.) - matches any one character except a newline
#'elon reeve musk'

get_pattern_match(r"Born.*\n(.*)\(age",text).strip()
#after Born all the character and new line before\ age match all char 
#june 28 1971

get_pattern_match(r"\(age.*\n(.*)",text)
#########

def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name= get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }
extract_personal_information(text)
############

text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''

get_pattern_match(r"age(\d+)",text)
#

get_pattern_match(r"Born(.*)\n",text).strip()
#
get_pattern_match(r"Born.*\n(.*)\(age",text).strip()
#
get_pattern_match(r"\(age.*\n(.*)",text)

############

def extract_personal_information(text):
    age= get_pattern_match('age (\d+)',text)
    full_name= get_pattern_match('Born(.*)\n',text)
    birth_date= get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place= get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }
extract_personal_information(text)
##########

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern ="https://twitter.com/([a-zA-Z0-9]+)"
re.findall(pattern, text)
######
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern= 'Concentration of Risk: ([^\n]*)'
re.findall(pattern ,text)
###########

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern= "FY(\d{4} (?:Q[1-4]|S[1-2]))"
matches =re.findall(pattern ,text)
matches
##
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern= "\(\d{3}\)-\d{3}-\d{4}|\d{10}"

matches=re.findall(pattern ,text)
matches
####
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern= "Note \d - ([^\n]*)"
matches=re.findall(pattern,text)
matches
########

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern= "FY\d{4} Q[1-4]"
matches=re.findall(pattern,text)
matches
####
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern= "FY\d{4} Q[1-4]"
matches=re.findall(pattern ,text)
matches

##############
