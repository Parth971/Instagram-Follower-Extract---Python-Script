import json
import requests


def main(max_id=None):
    url = "https://www.instagram.com/api/v1/friendships/52861090536/followers/?count=12&search_surface=follow_list_page"
    if max_id:
        url += f"&max_id={max_id}"

    headers = {
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cookie": 'datr=UNRVZZXFSQBg99UIq7K6n-S8; fbm_124024574287414=base_domain=.instagram.com; mid=Zf17swAEAAHGbOVn4bJLdzqEIs4p; ig_did=B159080C-14FA-4705-AD51-97D4AC1DF67E; ig_nrcb=1; ps_n=1; ps_l=1; ds_user_id=5708848487; csrftoken=GbZ3Uk08oZEin9uPLpZkA3jXWFzkTjBx; shbid="4642\0545708848487\0541757582904:01f7fe9d9b81b6cb646c9485e2c9a0c6cc20cbc429e9b2f09466166f6092e8302bd84ba2"; shbts="1726046904\0545708848487\0541757582904:01f793967a799b987fb9b58fc79be2239bc64a31375779245fc2f4049da5cb990e02fafb"; sessionid=5708848487%3AL79YjFVlTOpSx9%3A4%3AAYfS8QskU1GWosAp2RxKjL29_opqnyqnDU968ir-nA; fbsr_124024574287414=XxMaIFV4QZ_k4DapTYb9IJHbBG1zAghwdsbTtbRMOkI...',
        "priority": "u=1, i",
        "referer": "https://www.instagram.com/rohee.meme/followers/",
        "sec-ch-prefers-color-scheme": "dark",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        "sec-ch-ua-full-version-list": '"Chromium";v="128.0.6613.84", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.84"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Linux"',
        "sec-ch-ua-platform-version": '"6.2.0"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "x-asbd-id": "129477",
        "x-csrftoken": "GbZ3Uk08oZEin9uPLpZkA3jXWFzkTjBx",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "hmac.AR3yucgffXdXi2giuNffxW_byd9_Bn9-xX5q5x2ymMkL73y1",
        "x-requested-with": "XMLHttpRequest",
    }

    response = requests.get(url, headers=headers)

    return response.json()


if __name__ == "__main__":
    count = 1
    while True:
        response = main()
        print(f"Extracted count : {count}")
        with open(f"data/{count}.json", "w") as f:
            json.dump(response, f)
        count += 1

        next_max_id = response["next_max_id"]
        if next_max_id is None:
            break
