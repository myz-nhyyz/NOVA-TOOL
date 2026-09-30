import builtins
import os
import re

LANGUAGE = os.environ.get("NOVA_LANGUAGE", "en")

TRANSLATIONS = {
    "vi": {
        "Dox name?": "Tên dox?",
        "What is the victim's name?": "Tên nạn nhân là gì?",
        "What is the victim's surname?": "Họ nạn nhân là gì?",
        "What is the victim's age?": "Tuổi nạn nhân là bao nhiêu?",
        "What is the victim's date of birth?": "Ngày sinh nạn nhân là ngày nào?",
        "What is the victim's country?": "Quốc gia của nạn nhân là gì?",
        "What is the victim's city?": "Thành phố của nạn nhân là gì?",
        "What is the victim's address?": "Địa chỉ của nạn nhân là gì?",
        "Victim's school or professional situation?": "Trường học hoặc nghề nghiệp của nạn nhân?",
        "Other information about the victim?": "Thông tin khác về nạn nhân?",
        "What is the victim's nickname on online sites?": "Biệt danh của nạn nhân trên mạng là gì?",
        "What is the victim's email address?": "Email của nạn nhân là gì?",
        "What is the victim's phone number?": "Số điện thoại của nạn nhân là gì?",
        "What is the victim's YouTube account name?": "Tên tài khoản YouTube của nạn nhân là gì?",
        "What is the victim's Instagram account name?": "Tên tài khoản Instagram của nạn nhân là gì?",
        "What is the victim's Discord account name?": "Tên tài khoản Discord của nạn nhân là gì?",
        "What is the victim's Twitter account name?": "Tên tài khoản Twitter của nạn nhân là gì?",
        "What is the victim's Facebook account name?": "Tên tài khoản Facebook của nạn nhân là gì?",
        "What is the father's name?": "Tên cha là gì?",
        "What is the father's surname?": "Họ cha là gì?",
        "What is the father's age?": "Tuổi cha là bao nhiêu?",
        "What is the father's residence location?": "Nơi ở của cha là đâu?",
        "What is the father's profession?": "Nghề nghiệp của cha là gì?",
        "Additional information about the father?": "Thông tin thêm về cha?",
        "What is the mother's name?": "Tên mẹ là gì?",
        "What is the mother's surname?": "Họ mẹ là gì?",
        "What is the mother's age?": "Tuổi mẹ là bao nhiêu?",
        "What is the mother's residence location?": "Nơi ở của mẹ là đâu?",
        "What is the mother's profession?": "Nghề nghiệp của mẹ là gì?",
        "What are the mother's interests/hobbies?": "Sở thích của mẹ là gì?",
        "Additional information about the mother?": "Thông tin thêm về mẹ?",
        "What is the PC name?": "Tên máy tính là gì?",
        "What is the PC brand?": "Hãng máy tính là gì?",
        "What is the PC model?": "Mẫu máy tính là gì?",
        "What is the PC operating system?": "Hệ điều hành máy tính là gì?",
        "What is the PC MAC address?": "Địa chỉ MAC của máy tính là gì?",
        "What is the PC IP address?": "Địa chỉ IP của máy tính là gì?",
        "Other PC information?": "Thông tin khác về máy tính?",
        "Enter the person's username:": "Nhập tên người dùng:",
        "Enter the person's full name:": "Nhập họ tên:",
        "Enter the person's age:": "Nhập tuổi:",
        "Enter the person's address:": "Nhập địa chỉ:",
        "Enter the person's phone number:": "Nhập số điện thoại:",
        "Enter the person's IP address:": "Nhập địa chỉ IP:",
        "Enter the DOX name:": "Nhập tên DOX:",
        "Enter email:": "Nhập email:",
        "Enter the username to search:": "Nhập tên người dùng cần tìm:",
        "Open found links in browser?": "Mở các liên kết tìm được trong trình duyệt?",
        "Select the option:": "Chọn tùy chọn:",
        "Select the email (copy-paste):": "Chọn email (sao chép-dán):",
        "Send to:": "Gửi đến:",
        "Subject:": "Chủ đề:",
        "Message:": "Tin nhắn:",
        "Letter sending speed (1-5):": "Tốc độ gửi thư (1-5):",
        "Number of emails to send (1-99):": "Số email cần gửi (1-99):",
        "Press Enter to continue...": "Nhấn Enter để tiếp tục...",
        "Press Enter to continue...": "Nhấn Enter để tiếp tục...",
        "Enter the IP address": "Nhập địa chỉ IP",
        "Enter the number": "Nhập số",
        "Enter a URL": "Nhập URL",
        "Save results": "Lưu kết quả",
        "yes/no": "có/không",
        "How many codes to generate:": "Số mã cần tạo:",
        "Number of IPs to generate:": "Số IP cần tạo:",
        "Discord Webhook URL (leave empty to skip):": "URL Discord Webhook (để trống để bỏ qua):",
        "Save to file?": "Lưu vào tệp?",
        "Option:": "Tùy chọn:",
        "IP Address:": "Địa chỉ IP:",
        "Phone number (with country code, e.g. +33612345678):": "Số điện thoại (kèm mã quốc gia, ví dụ +33612345678):",
        "Search term:": "Từ khóa tìm kiếm:",
        "URL:": "URL:",
    },
    "zh": {
        "Dox name?": "Dox 名称？",
        "What is the victim's name?": "受害者的名字是什么？",
        "What is the victim's surname?": "受害者的姓氏是什么？",
        "What is the victim's age?": "受害者的年龄是多少？",
        "What is the victim's date of birth?": "受害者的出生日期是什么？",
        "What is the victim's country?": "受害者所在国家是什么？",
        "What is the victim's city?": "受害者所在城市是什么？",
        "What is the victim's address?": "受害者的地址是什么？",
        "Victim's school or professional situation?": "受害者的学校或职业情况？",
        "Other information about the victim?": "关于受害者的其他信息？",
        "What is the victim's nickname on online sites?": "受害者在网站上的昵称是什么？",
        "What is the victim's email address?": "受害者的邮箱地址是什么？",
        "What is the victim's phone number?": "受害者的电话号码是什么？",
        "What is the victim's YouTube account name?": "受害者的 YouTube 账号是什么？",
        "What is the victim's Instagram account name?": "受害者的 Instagram 账号是什么？",
        "What is the victim's Discord account name?": "受害者的 Discord 账号是什么？",
        "What is the victim's Twitter account name?": "受害者的 Twitter 账号是什么？",
        "What is the victim's Facebook account name?": "受害者的 Facebook 账号是什么？",
        "What is the father's name?": "父亲的名字是什么？",
        "What is the father's surname?": "父亲的姓氏是什么？",
        "What is the father's age?": "父亲的年龄是多少？",
        "What is the father's residence location?": "父亲的居住地在哪里？",
        "What is the father's profession?": "父亲的职业是什么？",
        "Additional information about the father?": "关于父亲的其他信息？",
        "What is the mother's name?": "母亲的名字是什么？",
        "What is the mother's surname?": "母亲的姓氏是什么？",
        "What is the mother's age?": "母亲的年龄是多少？",
        "What is the mother's residence location?": "母亲的居住地在哪里？",
        "What is the mother's profession?": "母亲的职业是什么？",
        "What are the mother's interests/hobbies?": "母亲的兴趣爱好是什么？",
        "Additional information about the mother?": "关于母亲的其他信息？",
        "What is the PC name?": "电脑名称是什么？",
        "What is the PC brand?": "电脑品牌是什么？",
        "What is the PC model?": "电脑型号是什么？",
        "What is the PC operating system?": "电脑操作系统是什么？",
        "What is the PC MAC address?": "电脑 MAC 地址是什么？",
        "What is the PC IP address?": "电脑 IP 地址是什么？",
        "Other PC information?": "其他电脑信息？",
        "Enter the person's username:": "输入用户名：",
        "Enter the person's full name:": "输入姓名：",
        "Enter the person's age:": "输入年龄：",
        "Enter the person's address:": "输入地址：",
        "Enter the person's phone number:": "输入电话号码：",
        "Enter the person's IP address:": "输入 IP 地址：",
        "Enter the DOX name:": "输入 DOX 名称：",
        "Enter email:": "输入邮箱：",
        "Enter the username to search:": "输入要搜索的用户名：",
        "Open found links in browser?": "在浏览器中打开找到的链接？",
        "Select the option:": "选择选项：",
        "Select the email (copy-paste):": "选择邮箱（复制粘贴）：",
        "Send to:": "发送至：",
        "Subject:": "主题：",
        "Message:": "消息：",
        "Letter sending speed (1-5):": "邮件发送速度（1-5）：",
        "Number of emails to send (1-99):": "发送邮件数量（1-99）：",
        "Press Enter to continue...": "按 Enter 继续...",
        "Enter the IP address": "输入 IP 地址",
        "Enter the number": "输入数字",
        "Enter a URL": "输入 URL",
        "Save results": "保存结果",
        "yes/no": "是/否",
        "How many codes to generate:": "要生成多少个代码：",
        "Number of IPs to generate:": "要生成多少个 IP：",
        "Discord Webhook URL (leave empty to skip):": "Discord Webhook URL（留空跳过）：",
        "Save to file?": "保存到文件？",
        "Option:": "选项：",
        "IP Address:": "IP 地址：",
        "Phone number (with country code, e.g. +33612345678):": "电话号码（包含国家代码，例如 +33612345678）：",
        "Search term:": "搜索词：",
        "URL:": "URL：",
    },
}

def translate_prompt(prompt):
    if LANGUAGE not in TRANSLATIONS or not isinstance(prompt, str):
        return prompt
    translated = prompt
    for source, target in sorted(TRANSLATIONS[LANGUAGE].items(), key=lambda item: len(item[0]), reverse=True):
        translated = translated.replace(source, target)
    return translated

def install():
    original_input = builtins.input

    def localized_input(prompt=""):
        return original_input(translate_prompt(prompt))

    builtins.input = localized_input
    try:
        from rich.console import Console
        original_console_input = Console.input

        def localized_console_input(self, prompt="", password=False, stream=None):
            return original_console_input(self, translate_prompt(prompt), password=password, stream=stream)

        Console.input = localized_console_input
    except ImportError:
        pass