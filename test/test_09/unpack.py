def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins_as_list = [100, 50, 25]

print(total(coins_as_list[0], coins_as_list[1], coins_as_list[2]))
print(total(galleons=100, sickles=50, knuts=25))

#  * will unpack the list in 3 arguments
print(total(*coins_as_list))

coins_as_tuple = (300, 400, 500)
print(total(*coins_as_tuple))

coins_as_dict = {'galleons': 111, 'sickles': 222, 'knuts': 333}
print(total(coins_as_dict["galleons"], coins_as_dict["sickles"], coins_as_dict['knuts']))
#  Double ** will unpack dict
print(total(**coins_as_dict))
