import json
import requests
from bs4 import BeautifulSoup

class Supervisor:
    def __init__(self):
        self.uid = "235097"
        self.avatar = "https://scdn.x-mol.com/css/images/tutorAvatar.png"
        self.name = "陈东岳"
        self.title = "教授"
        self.position = "博士生导师"
        self.school = "东北大学"
        self.department = "信息科学与工程学院"
        self.email = "chendongyue@ise.neu.edu.cn"
        self.website = "http://www.ise.neu.edu.cn/2019/0109/c5995a8227/page.htm"
        self.research_interests = ["机器学习", "计算机视觉", "模式识别", "图像处理", "视觉显著性检测", "多模态感知", "视频异常行为检测", "行人重识别", "人体三维重建"]
        self.project = ["基于多模态主动视觉的复杂动态场景智能感知，区域联合基金-重点项目，2021/10-2024/09，100万元。", "基于FPGA的工业产品表面缺陷智能视觉检测，教育部项目，ZX20210253，2021/04-2022/05，50万元"]
        self.article = ["Dongyue Chen, Lingyi Yue, Xingya Chang, Ming Xu, Tong Jia. NM-GAN: noise-modulated generative adversarial network for video anomaly detection[J]. Pattern Recognition, 2021, 116: 107969.", "Xingya Chang, Yuxin Zhang, Dingyu Xue, Dongyue Chen*.Multi-task learning for video anomaly detection[J]. Journal of Visual Communication and Image Representation, 2022, 87: 103547."]

    def save_to_json(self):
        data = {
            "uid": self.uid,
            "avatar": self.avatar,
            "name": self.name,
            "title": self.title,
            "position": self.position,
            "school": self.school,
            "department": self.department,
            "email": self.email,
            "website": self.website,
            "research_interests": self.research_interests,
            "project": self.project,
            "article": self.article
        }

        with open(self.uid + ".json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


def web_scraper(base_url, uid):
    # 目标网页URL
    url = base_url + uid
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


def main():
    # web_scraper("https://www.x-mol.com/university/faculty/", "235097")
    supervisor = Supervisor()
    supervisor.save_to_json()

if __name__ == "__main__":
    main()
