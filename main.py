import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

movies = []


def fetch_page(url):
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        return res.text
    except Exception as e:
        print("❌ 请求失败：", e)
        return None


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")

    for item in soup.select(".item"):
        try:
            title = item.select_one(".title").text
            rating = item.select_one(".rating_num").text
            quote = item.select_one(".inq")
            quote = quote.text if quote else "无"

            link = item.select_one("a")["href"]

            movies.append({
                "title": title,
                "rating": rating,
                "quote": quote,
                "link": link
            })
        except Exception as e:
            print("⚠️ 解析出错：", e)


def main():
    for start in range(0, 250, 25):
        url = f"https://movie.douban.com/top250?start={start}"
        print(f"正在爬取：{url}")

        html = fetch_page(url)
        if html:
            parse_page(html)

        time.sleep(1)

    df = pd.DataFrame(movies)
    df.to_csv("movies.csv", index=False, encoding="utf-8-sig")

    print("✅ 爬取完成！")


if __name__ == "__main__":
    main()