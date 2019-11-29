#find the total amount driver need to pay

gas_price = int(input("($)gas price per litre: "))
gas_used_per_km = int(input("(lt)gas used per km: "))
total_distance = int(input("(km)total distance: "))

print("Total amount you need to pay is {}".format(total_distance*gas_used_per_km*gas_price),"$", sep="")