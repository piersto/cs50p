d = {
	"data": {
		"id": "bitcoin",
		"priceUsd": "95472.4767167458286341",
		"explorer": "https://blockchain.info"
	},
	"timestamp": 1746387034815
}

# From dictionary "d" take "data" as dictionary
list_from_dictionary = d["data"]
# From "data" dic take value of the key "priceUsd" as float
price_usd = float(list_from_dictionary["priceUsd"])

# The same but in one line
p_usd_one_line = d["data"]["priceUsd"]

# Print price_usd with 4 digits after decimal
print(f"${price_usd:,.4f}")
print(p_usd_one_line)
print(d["timestamp"])
