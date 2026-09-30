# NOVA Tools (English)

NOVA Tools is a Python command-line toolkit with a colorful terminal interface and a menu organized by feature groups. The project also includes a Node.js Discord bot for testing server administration actions in an authorized environment.

> **Safety and legal warning**
>
> Several modules can query public data, scan ports, send email/SMS, generate sample data, or perform bulk actions on Discord. Use them only on assets, accounts, servers, and data that you own or are explicitly authorized to test. Do not use this project for doxxing, spam, phishing, disruption, privilege abuse, or tracking people. You are responsible for complying with applicable laws and terms of service.
>
> Do not run the Discord bot on a production server. Use a separate test server, a dedicated bot account, and the minimum permissions required.

## Features

### Main interface

- Interactive terminal menu with startup effects, ASCII art, progress bars, and randomized color themes.
- English, Français, 简体中文, and Tiếng Việt are available from Home > Language.
- Menu labels and feature names follow the selected language. Common interactive prompts in tools are translated where a translation is available; untranslated tool output remains in its source language.
- Start tools from the main menu to use the shared prompt localization in `NOVA/tools/localizer.py`. Running a tool script directly bypasses the shared launcher localization.
- The default language and menu color are saved locally for future launches. Menu colors stay synchronized while navigating; Random selects a new color only when opening a tool.
- Home > Color provides Random and fixed color themes.
- Module paths are resolved relative to `main.py`.
- Utility entries can open selected external services in a browser.

### OSINT and lookup tools

- Name Finder: checks a username across multiple websites and can open found results.
- Email Info: checks email formatting, DNS/domain details, and selected reputation data through external APIs.
- Number Info: analyzes phone numbers, carrier information, regions, and time zones with `phonenumbers`.
- IP Lookup: retrieves IP information through an external service.
- IP Localisation: retrieves country, region, city, coordinates, ISP, and organization data.
- IP Operator: looks up the network operator.
- IP Open Ports: checks a set of common ports.
- IP Pinger: pings an address using the operating system command.
- IP All Lookup: combines domain, HTTP status, IP, IP information, and selected port results.
- Search Database: searches for a string in local data stored in the project directory.
- Dox Creator and Simple Dox: create text forms from user input. Use only with fictional data, your own data, or data for which you have permission.
- Reference links such as OSINT Framework, Doxbin, and other external services are opened from the menu; they are not internal project modules.

### Email, SMS, and load-testing modules

- Email Bomber: repeatedly sends email through SMTP.
- Email Bomber Reset: automates a browser flow for an email reset process.
- SMS Bomber: the menu entry calls an external integration when the required configuration is available.
- Some DDoS/stresser entries only open external websites; they are not an internal DDoS implementation.

These functions can cause spam, violate terms of service, or disrupt other people. Do not use them against systems you do not control.

### Discord bot

The bot is located at `NOVA/bot/index.js`, reads configuration from `NOVA/config/discord-nuker.json`, and uses `!` as the default prefix. The commands currently present in the source are:

- `mchannel`: creates multiple text channels.
- `mspam`: creates channels and repeatedly sends pings.
- `mrole`: creates multiple roles.
- `dchannel`: deletes channels.
- `drole`: deletes roles.
- `de`: deletes emojis.
- `demoji`: deletes stickers.
- `mban`: bans members in bulk.
- `mkick`: kicks members in bulk.
- `stop`: stops the bot.

The bot checks Discord permissions such as `MANAGE_CHANNELS`, `MANAGE_ROLES`, `MANAGE_EMOJIS_AND_STICKERS`, `BAN_MEMBERS`, and `KICK_MEMBERS`. Actions are still subject to role hierarchy, API limits, and Discord permissions.

> The bot is currently designed with destructive and spam behavior. Do not invite it to someone else's server, do not use a personal account token, do not commit tokens to Git, and keep permissions as limited as possible.

### Generators and utilities

- Generates random strings and codes.
- Generates strings labeled by the menu for gift cards from several services.
- Discord Nitro generator/checker functionality that connects to the Discord API and webhooks according to the source code.
- Generates random public IP addresses; some flows can send results to a webhook.
- Generates passwords.
- Hash cracker and crypto utilities shown in the main menu.
- Temporary mail and temporary email service links.

Randomly generated output does not represent a valid code, access, or real-world value. Do not send sensitive data to a webhook you do not control.

## Requirements

- Windows 10/11 is supported directly by `setup.bat` and `start.bat`.
- Python 3.10 or newer is recommended.
- Node.js and npm are required for the Discord bot.
- Internet access is required for API, DNS, SMTP, Selenium, and external-service modules.
- Google Chrome/Chromium and a compatible driver are required for `email-bomber-reset`.

## Installation

### Quick Windows setup

Open Command Prompt or PowerShell in the directory containing this README and run:

```bat
setup.bat
```

The script installs the required Python packages and runs `npm install` inside `NOVA/bot`.

### Manual setup

Install Python dependencies:

```powershell
python -m pip install rich colorama requests selenium webdriver-manager deep-translator twilio phonenumbers geopy aiohttp==3.7.4 pystyle==2.9 fake-useragent==1.2.1 discord.py dnspython pyfiglet
```

Install the bot dependencies:

```powershell
cd NOVA\bot
npm install
cd ..\..
```

`discord.py` is included for Python modules that may use it; the main Discord bot itself uses `discord.js`.

## Running

### Main menu

```bat
start.bat
```

Or run it directly:

```powershell
python .\NOVA\main.py
```

Choose a language and a menu entry, then follow the prompts for the selected module. The module mapping is defined in `NOVA/main.py`.

To change the interface language, open **Home > Language**, select English, French, Simplified Chinese, or Vietnamese, and return to the menu. The selection is saved locally. Use the main menu to launch tools so their supported prompts use the selected language.

### Discord bot

1. Create a bot in the Discord Developer Portal.
2. Enable the required intents and grant only the minimum permissions in a test server.
3. Open `NOVA/config/discord-nuker.json`.
4. Replace the sample values with your local configuration:

```json
{
  "prefix": "!",
  "userID": "your_user_id",
  "disableEveryone": true,
  "token": "YOUR_BOT_TOKEN"
}
```

5. Run it from the project directory:

```powershell
node .\NOVA\bot\index.js
```

Never upload a configuration file containing a token to GitHub or share it publicly. If a token is exposed, reset it immediately in the Developer Portal.

## Project structure

```text
.
├── setup.bat                         # Installs Python and Node.js dependencies
├── start.bat                         # Starts the Python menu
└── NOVA/
    ├── main.py                       # Menu, UI, and module dispatcher
    ├── bot/
    │   ├── index.js                  # Discord bot
    │   ├── package.json              # Node.js dependencies
    │   └── package-lock.json
    ├── config/
    │   └── discord-nuker.json        # Local bot prefix and token configuration
    └── tools/
        ├── dox/
        ├── email-bomber/
        ├── email-bomber-reset/
        ├── email-info/
        ├── generator/
        ├── ip-all-lookup/
        ├── ip-generator/
        ├── ip-localisation/
        ├── ip-lookup/
        ├── ip-open-ports/
        ├── ip-operator/
        ├── ip-pinger/
        ├── localizer.py              # Shared translations for supported tool prompts
        ├── name-tracker/
        ├── nitro-generator/
        ├── number-info/
        ├── run_tool.py               # Installs prompt localization before launching a tool
        ├── search-database/
        └── simple-dox/
```

Most tool directories contain both `en.py` and `fr.py`. `__pycache__`, `node_modules`, and generated runtime files do not need to be distributed or committed.

## Operational notes

- External APIs can change, rate-limit requests, or become unavailable.
- IP, email, username, and phone lookups may process personal data; minimize collection, respect privacy, and store results securely.
- Port scanning must only be performed against authorized hosts.
- SMTP, SMS, webhook, and Selenium modules may require accounts, credentials, or additional configuration; never place secrets in source code.
- No automated test suite is declared in `NOVA/bot/package.json`; test manually in an isolated environment before use.

## Author

- Author displayed by the application: `nova_.inovation`
- Profile: [zyo.lol/nova_.inovation](https://zyo.lol/nova_.inovation)
- Version displayed in the menu: `3.0`

## License

This project is released under the [MIT License](LICENSE).

You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the project, subject to the terms in `LICENSE`. The software is provided without warranty.

---

# NOVA Tools (Tiếng Việt)

NOVA Tools là bộ công cụ dòng lệnh viết bằng Python, có giao diện terminal nhiều màu và menu được chia theo từng nhóm chức năng. Dự án cũng bao gồm một Discord bot viết bằng Node.js để thử nghiệm các thao tác quản trị server trong môi trường được cấp phép.

> **Cảnh báo an toàn và pháp lý**
>
> Một số module có thể tra cứu dữ liệu công khai, quét cổng, gửi email/SMS, tạo dữ liệu mẫu hoặc thực hiện thao tác hàng loạt trên Discord. Chỉ sử dụng với tài sản, tài khoản, server và dữ liệu mà bạn sở hữu hoặc được cho phép rõ ràng. Không sử dụng cho doxxing, spam, phishing, phá hoại, lạm dụng quyền hoặc theo dõi người khác. Người dùng chịu trách nhiệm tuân thủ pháp luật và điều khoản dịch vụ áp dụng.
>
> Không chạy Discord bot trên server thật. Hãy dùng server thử nghiệm riêng, tài khoản bot riêng và quyền tối thiểu cần thiết.

## Tính năng

### Giao diện chính

- Menu terminal tương tác với hiệu ứng khởi động, ASCII art, progress bar và theme màu ngẫu nhiên.
- Có thể chọn English, Français, 简体中文 hoặc Tiếng Việt trong Home > Language.
- Tên mục và tính năng trong menu đổi theo ngôn ngữ đã chọn. Các prompt tương tác của tool được dịch khi có bản dịch tương ứng; phần output chưa có bản dịch vẫn hiển thị theo ngôn ngữ gốc.
- Hãy mở tool từ menu chính để dùng bộ dịch prompt chung trong `NOVA/tools/localizer.py`. Chạy trực tiếp file tool sẽ bỏ qua bộ dịch của launcher.
- Ngôn ngữ mặc định và màu menu được lưu cục bộ cho lần chạy sau. Màu được đồng bộ khi điều hướng; Random chỉ chọn màu mới khi mở tool.
- Home > Color cho phép chọn Random hoặc màu cố định.
- Đường dẫn module được xử lý tương đối so với `main.py`.
- Một số mục tiện ích có thể mở dịch vụ bên ngoài bằng trình duyệt.

### OSINT và công cụ tra cứu

- Name Finder: kiểm tra username trên nhiều website và có thể mở kết quả tìm được.
- Email Info: kiểm tra định dạng email, DNS/domain và một số dữ liệu reputation qua API bên ngoài.
- Number Info: phân tích số điện thoại, nhà mạng, khu vực và múi giờ bằng `phonenumbers`.
- IP Lookup: lấy thông tin IP thông qua dịch vụ bên ngoài.
- IP Localisation: lấy quốc gia, khu vực, thành phố, tọa độ, ISP và tổ chức.
- IP Operator: tra cứu nhà mạng/operator.
- IP Open Ports: kiểm tra một số cổng phổ biến.
- IP Pinger: ping địa chỉ bằng lệnh của hệ điều hành.
- IP All Lookup: tổng hợp domain, HTTP status, IP, thông tin IP và kết quả một số cổng.
- Search Database: tìm chuỗi trong dữ liệu cục bộ được lưu trong thư mục dự án.
- Dox Creator và Simple Dox: tạo biểu mẫu văn bản từ dữ liệu nhập vào. Chỉ dùng dữ liệu giả, dữ liệu của bạn hoặc dữ liệu đã được cho phép.
- Một số liên kết như OSINT Framework, Doxbin và các dịch vụ bên ngoài được mở từ menu; chúng không phải module nội bộ.

### Email, SMS và module kiểm thử tải

- Email Bomber: gửi email lặp qua SMTP.
- Email Bomber Reset: tự động hóa luồng reset email bằng trình duyệt.
- SMS Bomber: gọi tích hợp bên ngoài khi có cấu hình cần thiết.
- Một số mục DDoS/stresser chỉ mở website bên ngoài, không phải triển khai DDoS nội bộ.

Các chức năng này có thể gây spam, vi phạm điều khoản dịch vụ hoặc làm gián đoạn người khác. Không sử dụng trên hệ thống bạn không kiểm soát.

### Discord bot

Bot nằm tại `NOVA/bot/index.js`, đọc cấu hình từ `NOVA/config/discord-nuker.json` và sử dụng prefix mặc định `!`. Các lệnh hiện có trong mã nguồn:

- `mchannel`: tạo nhiều text channel.
- `mspam`: tạo channel và gửi ping lặp.
- `mrole`: tạo nhiều role.
- `dchannel`: xoá channel.
- `drole`: xoá role.
- `de`: xoá emoji.
- `demoji`: xoá sticker.
- `mban`: ban thành viên hàng loạt.
- `mkick`: kick thành viên hàng loạt.
- `stop`: dừng bot.

Bot kiểm tra các quyền Discord như `MANAGE_CHANNELS`, `MANAGE_ROLES`, `MANAGE_EMOJIS_AND_STICKERS`, `BAN_MEMBERS` và `KICK_MEMBERS`. Các thao tác vẫn chịu giới hạn role hierarchy, API và quyền thực tế của Discord.

> Bot hiện có hành vi phá hoại và spam theo thiết kế. Không mời bot vào server của người khác, không dùng token tài khoản cá nhân, không commit token lên Git và hãy giới hạn quyền bot ở mức thấp nhất.

### Generator và tiện ích

- Sinh chuỗi và code ngẫu nhiên.
- Sinh chuỗi được menu gắn nhãn cho gift card của một số dịch vụ.
- Discord Nitro generator/checker có kết nối tới Discord API và webhook theo mã nguồn.
- Sinh IP public ngẫu nhiên; một số luồng có thể gửi kết quả tới webhook.
- Sinh mật khẩu.
- Hash cracker và các tiện ích crypto trong menu chính.
- Temp mail và liên kết tới các dịch vụ email tạm thời.

Kết quả sinh ngẫu nhiên không đại diện cho mã hợp lệ, quyền truy cập hoặc giá trị thật. Không gửi dữ liệu nhạy cảm tới webhook bạn không kiểm soát.

## Yêu cầu hệ thống

- Windows 10/11 được hỗ trợ trực tiếp bởi `setup.bat` và `start.bat`.
- Khuyến nghị Python 3.10 trở lên.
- Cần Node.js và npm nếu muốn dùng Discord bot.
- Cần Internet cho các module API, DNS, SMTP, Selenium và dịch vụ bên ngoài.
- Cần Google Chrome/Chromium và driver tương thích cho `email-bomber-reset`.

## Cài đặt

### Cài đặt nhanh trên Windows

Mở Command Prompt hoặc PowerShell tại thư mục chứa README này rồi chạy:

```bat
setup.bat
```

Script sẽ cài các package Python cần thiết và chạy `npm install` trong `NOVA/bot`.

### Cài đặt thủ công

Cài dependency Python:

```powershell
python -m pip install rich colorama requests selenium webdriver-manager deep-translator twilio phonenumbers geopy aiohttp==3.7.4 pystyle==2.9 fake-useragent==1.2.1 discord.py dnspython pyfiglet
```

Cài dependency cho bot:

```powershell
cd NOVA\bot
npm install
cd ..\..
```

`discord.py` dành cho các module Python có thể sử dụng nó; Discord bot chính dùng `discord.js`.

## Chạy

### Menu chính

```bat
start.bat
```

Hoặc chạy trực tiếp:

```powershell
python .\NOVA\main.py
```

Chọn ngôn ngữ và mục trong menu, sau đó làm theo lời nhắc của module. Ánh xạ module được định nghĩa trong `NOVA/main.py`.

Để đổi ngôn ngữ giao diện, mở **Home > Language**, chọn English, Français, 简体中文 hoặc Tiếng Việt rồi quay lại menu. Lựa chọn được lưu cục bộ. Hãy mở tool từ menu chính để các prompt được hỗ trợ hiển thị theo ngôn ngữ đã chọn.

### Discord bot

1. Tạo bot trong Discord Developer Portal.
2. Bật intents cần thiết và chỉ cấp quyền tối thiểu trong server thử nghiệm.
3. Mở `NOVA/config/discord-nuker.json`.
4. Thay các giá trị mẫu bằng cấu hình cục bộ:

```json
{
  "prefix": "!",
  "userID": "your_user_id",
  "disableEveryone": true,
  "token": "YOUR_BOT_TOKEN"
}
```

5. Chạy từ thư mục dự án:

```powershell
node .\NOVA\bot\index.js
```

Không upload file cấu hình chứa token lên GitHub hoặc chia sẻ công khai. Nếu token bị lộ, hãy reset ngay trong Developer Portal.

## Cấu trúc dự án

```text
.
├── setup.bat                         # Cài dependency Python và Node.js
├── start.bat                         # Khởi chạy menu Python
└── NOVA/
    ├── main.py                       # Menu, giao diện và điều phối module
    ├── bot/
    │   ├── index.js                  # Discord bot
    │   ├── package.json              # Dependency Node.js
    │   └── package-lock.json
    ├── config/
    │   └── discord-nuker.json        # Cấu hình prefix và token bot cục bộ
    └── tools/
      ├── localizer.py               # Bản dịch dùng chung cho prompt được hỗ trợ
      ├── run_tool.py                # Cài bộ dịch trước khi chạy tool
        ├── dox/
        ├── email-bomber/
        ├── email-bomber-reset/
        ├── email-info/
        ├── generator/
        ├── ip-all-lookup/
        ├── ip-generator/
        ├── ip-localisation/
        ├── ip-lookup/
        ├── ip-open-ports/
        ├── ip-operator/
        ├── ip-pinger/
        ├── name-tracker/
        ├── nitro-generator/
        ├── number-info/
        ├── search-database/
        └── simple-dox/
```

Hầu hết thư mục tool có cả `en.py` và `fr.py`. Không cần phân phối hoặc commit `__pycache__`, `node_modules` và các file runtime được sinh ra.

## Lưu ý vận hành

- API bên ngoài có thể thay đổi, giới hạn tốc độ hoặc ngừng hoạt động.
- Tra cứu IP, email, username và số điện thoại có thể xử lý dữ liệu cá nhân; hãy giảm dữ liệu thu thập, tôn trọng quyền riêng tư và lưu kết quả an toàn.
- Chỉ quét cổng trên host được ủy quyền.
- SMTP, SMS, webhook và Selenium có thể cần tài khoản, credential hoặc cấu hình bổ sung; không đặt secret trong source code.
- `NOVA/bot/package.json` hiện không khai báo bộ test tự động; hãy kiểm tra thủ công trong môi trường cô lập.

## Tác giả

- Tác giả hiển thị trong ứng dụng: `nova_.inovation`
- Profile: [zyo.lol/nova_.inovation](https://zyo.lol/nova_.inovation)
- Phiên bản hiển thị trong menu: `3.0`

## Giấy phép

Dự án được phát hành theo [MIT License](LICENSE). Bạn có thể sử dụng, sao chép, chỉnh sửa, gộp, xuất bản, phân phối, cấp phép lại và bán bản sao của dự án theo các điều khoản trong file `LICENSE`. Phần mềm được cung cấp không kèm bảo hành.
