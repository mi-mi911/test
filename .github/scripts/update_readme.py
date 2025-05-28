# File: .github/scripts/update_readme.py
import os
import requests
import re # Để tìm kiếm và thay thế trong README

# Lấy token và thông tin repo từ biến môi trường
TOKEN = os.getenv('GH_TOKEN')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')

if not TOKEN or not REPO_OWNER or not REPO_NAME:
    print("Thiếu biến môi trường. Vui lòng kiểm tra GH_TOKEN, REPO_OWNER, REPO_NAME.")
    exit(1)

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Lấy số lượt xem (Views)
views_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/traffic/views'
views_response = requests.get(views_url, headers=headers)
views_data = views_response.json()
total_views = views_data.get('count', 0)
unique_views = views_data.get('uniques', 0)

# Lấy số lượt clone (Clones)
clones_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/traffic/clones'
clones_response = requests.get(clones_url, headers=headers)
clones_data = clones_response.json()
total_clones = clones_data.get('count', 0)
unique_clones = clones_data.get('uniques', 0)

# Cập nhật README
readme_path = 'README.md'
try:
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Định dạng chuỗi để chèn vào README
    stats_string = f"""
### 📊 Thống kê Repo

| Loại     | Tổng cộng | Duy nhất |
| :------- | :--------: | :-------: |
| Lượt xem | {total_views}   | {unique_views}  |
| Lượt clone| {total_clones}   | {unique_clones}  |
"""

    # Sử dụng biểu thức chính quy để tìm và thay thế nội dung giữa các comment
    # Ví dụ: ... # Bạn có thể tự định nghĩa các thẻ comment này trong README của mình.
    updated_content = re.sub(
        r'.*?',
        f'\n{stats_string}\n',
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("README.md đã được cập nhật thành công!")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp {readme_path}")
except Exception as e:
    print(f"Đã xảy ra lỗi khi cập nhật README: {e}")
