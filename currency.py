__author__ = 'Magpie'

import web_utility
def convert(amount, home_currency_code, location_currency_code):
    url_string = ("https://www.google.com/finance/converter?a=" + amount + "&from=" + home_currency_code + "&to=" + location_currency_code)
    result = web_utility.load_page(url_string)
    result = (result[result.index('result'):])
    return result

def get_details(country_name):
    searchfile = open("currency_details.txt", "r", encoding="utf-8")
    for line in searchfile:
        if country_name in line:
            country_details = tuple(line.split(","))
    searchfile.close()
    country_name = ()
    country_name = country_name + country_details
    return country_name


amount = input('How much are you converting? ') #Obtains amount they wish to convert

country_name = input("What country's currency are you converting from? ") #Obtains what country the user is converting from
home_currency_code = get_details(country_name) #Runs the function to obtain the information required - The Symbol & Code for that countries currency
home_symbol = home_currency_code[2] #Applies the final tuple item, the currency symbol, as home_symbol)
home_symbol = home_symbol[0] #removes new line section from it to not disrupt any print statements using home_symbol
home_currency_code = home_currency_code[1] #Applies the middle tuple item, the currency code, as the home_currency_code

country_name = input("What country's currency are you converting to? ") #Same as previous code block, except for the country/currency the user is converting TO
location_currency_code = get_details(country_name)
location_symbol = location_currency_code[2]
location_symbol = location_symbol[0]
location_currency_code = location_currency_code[1]

conversionresult = convert(amount, home_currency_code, location_currency_code) #Uses obtained information to run convert function, which then runs another function to obtain the webpage info from google convert.

number = conversionresult.index("</span") #Finds out where </span begins in the string returned from google
conversionresult = conversionresult[0:number] #Wipes everything after </span, as it's useless information
conversionresult = conversionresult.replace("<span class=bld>", "") #removes unnecessary code block
conversionresult = conversionresult.replace("result>", "") #removes unnecessary code block

number = conversionresult.index("=")
number = number + 1
conversionresult = conversionresult[number:] #Cuts out last of unnecessary data

print("You wanted ", home_symbol, amount, " ", home_currency_code, " to be converted to ", location_currency_code, ". The result is ", home_symbol, amount, " ", home_currency_code, " = ", location_symbol, conversionresult, ".", sep="") #Prints result for the user
