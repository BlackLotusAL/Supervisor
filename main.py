import requests
from bs4 import BeautifulSoup

def main():
    uid = 235097

    # 目标网页URL
    url = "https://www.x-mol.com/university/faculty/" + str(uid)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # 发送HTTP请求获取网页内容
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取网页标题
        title = soup.title.string
        print(f"Title: {title}")

        # 提取所有段落内容
        paragraphs = soup.find_all('p')
        for idx, paragraph in enumerate(paragraphs, start=1):
            print(f"Paragraph {idx}: {paragraph.text}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


if __name__ == "__main__":
    main()
