import os
import requests
import re

# Lấy token và thông tin repo từ biến môi trường
TOKEN = os.getenv('GH_TOKEN')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')

if not TOKEN or not REPO_OWNER or not REPO_NAME:
    print("Lỗi: Thiếu biến môi trường (GH_TOKEN, REPO_OWNER, REPO_NAME).")
    exit(1)

headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Lấy số lượt xem (Views)
try:
    views_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/traffic/views'
    views_response = requests.get(views_url, headers=headers)
    views_response.raise_for_status() # Báo lỗi nếu request thất bại
    views_data = views_response.json()
    total_views = views_data.get('count', 0)
    unique_views = views_data.get('uniques', 0)
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi lấy lượt xem: {e}")
    total_views = "N/A"
    unique_views = "N/A"

# Lấy số lượt clone (Clones)
try:
    clones_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/traffic/clones'
    clones_response = requests.get(clones_url, headers=headers)
    clones_response.raise_for_status() # Báo lỗi nếu request thất bại
    clones_data = clones_response.json()
    total_clones = clones_data.get('count', 0)
    unique_clones = clones_data.get('uniques', 0)
except requests.exceptions.RequestException as e:
    print(f"Lỗi khi lấy lượt clone: {e}")
    total_clones = "N/A"
    unique_clones = "N/A"

# Cập nhật README
readme_path = 'README.md'
try:
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Định dạng chuỗi để chèn vào README
    stats_string = f"""
  # Sử dụng biểu thức chính quy để tìm và thay thế nội dung giữa các comment
    # Đảm bảo các thẻ và có trong README.md
    updated_content = re.sub(
        r'().*?()',
        f'\\1\n{stats_string}\n\\2',
        readme_content,
        flags=re.DOTALL | re.IGNORECASE
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("README.md đã được cập nhật thành công!")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp README.md tại {readme_path}")
    exit(1)
except Exception as e:
    print(f"Đã xảy ra lỗi khi cập nhật README: {e}")
    exit(1)

```
