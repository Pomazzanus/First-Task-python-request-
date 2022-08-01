import requests
import json

def get_to_json(start_url):
    res = requests.get(start_url).json()
    to_json = json.dumps(res["data"]["cryptoCurrencyList"], indent=2)
    print(to_json)
    save_as_json(to_json)


def save_as_json(to_json):
    file = open("Task_1.json", "w")
    file.write(to_json)
    file.close()


if __name__ == "__main__":
    start_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_cap& sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,volume_60d'
    get_to_json(start_url)


