import os
import json
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ========== CẤU HÌNH ==========

script_dir = os.path.dirname(os.path.abspath(__file__))
chromedriver_path = os.path.join(script_dir, "..", "set_up", "chromedriver-win64", "chromedriver.exe")
news_data_path = os.path.join(script_dir, "..", "data", "news_data.json")

os.makedirs(os.path.dirname(news_data_path), exist_ok=True)

domain = "https://vtv.vn/"
categories = [
    "chinh-tri", "xa-hoi", "phap-luat", "the-gioi", "kinh-te", "the-thao",
    "truyen-hinh", "giai-tri", "suc-khoe", "doi-song", "cong-nghe", "giao-duc"
]

# ========== HỖ TRỢ ==========

def click_load_more(driver, max_clicks=20):
    """Click vào nút 'Xem thêm' tối đa max_clicks lần và chờ bài mới load ra"""
    try:
        old_articles = driver.find_elements(By.CSS_SELECTOR, 'a[data-linktype="newsdetail"]')
        old_count = len(old_articles)
        clicks = 0

        while clicks < max_clicks:
            load_more_button = driver.find_element(By.CSS_SELECTOR, "div.loadmore a")
            driver.execute_script("arguments[0].click();", load_more_button)
            print(f"   🔄 Đã click 'Xem thêm' lần {clicks + 1}...")
            clicks += 1

            # Chờ bài mới load ra
            WebDriverWait(driver, 10).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, 'a[data-linktype="newsdetail"]')) > old_count
            )
            sleep(random.uniform(1.5, 3.5))
            
            # Kiểm tra nếu không còn nút "Xem thêm" thì dừng
            if len(driver.find_elements(By.CSS_SELECTOR, "div.loadmore a")) == 0:
                break

        return True

    except Exception as e:
        print(f"   ⚠️ Lỗi khi click 'Xem thêm': {e}")
        return False

def extract_article_data(driver, link, title, category):
    """Truy cập từng bài và lấy dữ liệu chi tiết"""
    try:
        driver.get(link)
        sleep(random.uniform(1, 2))

        try:
            author_text = driver.find_element(By.CSS_SELECTOR, 'p.author').text
            author = author_text.split("-")[0].strip()
        except:
            author = ""

        try:
            short_description = driver.find_element(By.CSS_SELECTOR, 'h2.sapo').text[9:]
        except:
            short_description = ""

        content = ""
        try:
            paragraphs = driver.find_element(By.ID, 'entry-body').find_elements(By.TAG_NAME, 'p')
            for p in paragraphs:
                text = p.text.strip()
                if not text.startswith("* Mời quý độc giả"):
                    content += text + " "
            content = content.strip()
        except:
            content = ""

        return {
            "title": title,
            "category": category,
            "news_link": link,
            "author": author,
            "short_description": short_description,
            "content": content
        }
    except Exception as e:
        print(f"   ❌ Lỗi khi lấy dữ liệu bài {link}: {e}")
        return None

# ========== KHỞI TẠO DRIVER ==========

options = Options()
# options.add_argument("--headless")  # Nếu muốn chạy ẩn trình duyệt
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# ========== CRAWLING ==========

news_links = []
all_data = []

for category in categories:  # Crawl thử 2 category đầu tiên
    print(f"\n▶ Chủ đề: {category}")
    category_url = f"{domain}{category}.htm"
    driver.get(category_url)
    sleep(random.uniform(1, 2))

    # Ấn "Xem thêm" tối đa 20 lần
    if not click_load_more(driver, max_clicks=20):
        print("   ⚠️ Không thể tiếp tục click 'Xem thêm'. Dừng lại.")
        break

    # Lấy danh sách bài viết sau khi load hết
    article_elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-linktype="newsdetail"]')
    print(f"   🔎 Tổng số bài tìm thấy: {len(article_elements)}")

    for article in article_elements:
        try:
            link = article.get_attribute("href")
            title = article.get_attribute("title")
            if link and (link, title) not in news_links:
                news_links.append((link, title, category))
        except Exception as e:
            print(f"   ⚠️ Lỗi đọc link: {e}")
            continue

# Crawl chi tiết từng bài viết
print("\n▶ Bắt đầu vào từng bài viết để lấy thông tin...")
for link, title, category in news_links:
    print(f"→ Đang lấy: {title}")
    article_data = extract_article_data(driver, link, title, category)
    if article_data:
        all_data.append(article_data)
    sleep(random.uniform(1, 2))

# ========== LƯU FILE ==========

with open(news_data_path, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f"\n✅ Đã lưu {len(all_data)} bài viết vào {news_data_path}")

driver.quit()
