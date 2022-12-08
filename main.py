import requests
import random
import json

def collect_data():
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    }
    offset = 0
    batch_size = 60 
    result = []
    count = 0
    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=35&isStore=true&limit=60&maxPrice=10000&minPrice=2003.0646889741304&offset={item}&sort=botFirst&type=4&withStack=true'
            response = requests.get(
                url = url,
                headers = {'User-Agent':'Accept'}
            )
            offset += batch_size
            data = response.json()
            items = data.get('items')
            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_overprice = i.get('overprice')
                    result.append({
                        'fullName':item_full_name,
                        '3d':item_3d,
                        'price':item_price,
                        'overprice':item_overprice
                    })
        count += 1
        print(f'Page #{count}')
        print(url)
        if len(items) < 60:
            break

    with open('result3.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))



def main():
    collect_data()

if __name__ == "__main__":
    main()
