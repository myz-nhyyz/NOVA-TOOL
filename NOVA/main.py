#!/usr/bin/env python3
"""
 ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗
 ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
 ██╔██╗ ██║██║   ██║██║   ██║███████║
 ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
 ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
 ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
     nova-tool v1.0  ·  by nova_.inovation
"""
import os, sys, time, shutil, subprocess, webbrowser, re, random, math, threading, string, unicodedata
from colorama import init, Fore, Style
init(autoreset=True)

from rich.console  import Console
from rich.panel    import Panel
from rich.table    import Table
from rich.text     import Text
from rich.columns  import Columns
from rich.rule     import Rule
from rich.align    import Align
from rich.live     import Live
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich          import box
import pyfiglet

console = Console(highlight=False)

C_BLOOD   = "#006994"
C_DARK    = "#008CC1"
C_MID     = "#00AEEF"
C_RED     = "#29B6F6"
C_NEON    = "#81D4FA"
C_BRIGHT  = "#B3E5FC"
C_WHITE   = "#FFFFFF"
C_SILVER  = "#CCCCCC"
C_DIM     = "#666666"
C_GOLD    = "#FFD700"
C_GOLD2   = "#FFA500"

COLOR_THEMES = [
    {
        "blood": "#006994", "dark": "#008CC1", "mid": "#00AEEF",
        "neon": "#81D4FA", "bright": "#B3E5FC", "white": "#FFFFFF",
        "silver": "#CCCCCC", "dim": "#666666", "gold": "#FFD700", "gold2": "#FFA500",
    },
    {
        "blood": "#650000", "dark": "#990000", "mid": "#D00000",
        "neon": "#FF3030", "bright": "#FF7777", "white": "#FFFFFF",
        "silver": "#D8D8D8", "dim": "#777777", "gold": "#FFD700", "gold2": "#FFA500",
    },
    {
        "blood": "#160000", "dark": "#350000", "mid": "#650000",
        "neon": "#9B0000", "bright": "#D43737", "white": "#FFFFFF",
        "silver": "#C8C8C8", "dim": "#666666", "gold": "#D4AF37", "gold2": "#8B6508",
    },
    {
        "blood": "#000000", "dark": "#181818", "mid": "#383838",
        "neon": "#707070", "bright": "#BEBEBE", "white": "#FFFFFF",
        "silver": "#D8D8D8", "dim": "#8A8A8A", "gold": "#B0B0B0", "gold2": "#666666",
    },
    {
        "blood": "#FFFFFF", "dark": "#D8D8D8", "mid": "#A0A0A0",
        "neon": "#303030", "bright": "#111111", "white": "#000000",
        "silver": "#444444", "dim": "#777777", "gold": "#555555", "gold2": "#222222",
    },
    {
        "blood": "#064E3B", "dark": "#047857", "mid": "#10B981",
        "neon": "#34D399", "bright": "#A7F3D0", "white": "#FFFFFF",
        "silver": "#D1FAE5", "dim": "#6B7280", "gold": "#FDE047", "gold2": "#A16207",
    },
    {
        "blood": "#713F12", "dark": "#A16207", "mid": "#EAB308",
        "neon": "#FACC15", "bright": "#FEF08A", "white": "#FFFFFF",
        "silver": "#FEF9C3", "dim": "#78716C", "gold": "#FFF7AE", "gold2": "#CA8A04",
    },
    {
        "blood": "#831843", "dark": "#BE185D", "mid": "#EC4899",
        "neon": "#F472B6", "bright": "#FBCFE8", "white": "#FFFFFF",
        "silver": "#FCE7F3", "dim": "#9D7487", "gold": "#F9A8D4", "gold2": "#DB2777",
    },
    {
        "blood": "#3B0764", "dark": "#6B21A8", "mid": "#A855F7",
        "neon": "#C084FC", "bright": "#E9D5FF", "white": "#FFFFFF",
        "silver": "#F3E8FF", "dim": "#8B7A9E", "gold": "#D8B4FE", "gold2": "#9333EA",
    },
    {
        "blood": "#7C2D12", "dark": "#C2410C", "mid": "#F97316",
        "neon": "#FB923C", "bright": "#FED7AA", "white": "#FFFFFF",
        "silver": "#FFEDD5", "dim": "#9A7060", "gold": "#FDBA74", "gold2": "#EA580C",
    },
]

AUTHOR       = "nova_.inovation"
PROFILE      = "https://zyo.lol/nova_.inovation"
path         = os.getcwd()
PROJECT_DIR  = os.path.dirname(os.path.abspath(__file__))
LANGUAGE_FILE = os.path.join(PROJECT_DIR, "data", ".language")
COLOR_FILE = os.path.join(PROJECT_DIR, "data", ".color")
LANGUAGE = "en"
COLOR_MODE = "random"
THEME_FOR_NEXT_MENU = False


def open_community_links():
    return None

def load_language():
    global LANGUAGE
    try:
        with open(LANGUAGE_FILE, "r", encoding="utf-8") as file:
            language = file.read().strip().lower()
        if language in {"en", "fr", "zh", "vi"}:
            LANGUAGE = language
    except (FileNotFoundError, OSError):
        LANGUAGE = "en"
    return LANGUAGE

def save_language(language):
    global LANGUAGE
    if language not in {"en", "fr", "zh", "vi"}:
        return
    os.makedirs(os.path.dirname(LANGUAGE_FILE), exist_ok=True)
    with open(LANGUAGE_FILE, "w", encoding="utf-8") as file:
        file.write(language)
    LANGUAGE = language

def language_label(language):
    return {
        "en": "English",
        "fr": "Français",
        "zh": "简体中文",
        "vi": "Tiếng Việt",
    }.get(language, "English")

UI_LABELS = {
    "Profile": {"fr": "Profil", "zh": "个人资料", "vi": "Hồ sơ"},
    "Language": {"fr": "Langue", "zh": "语言", "vi": "Ngôn ngữ"},
    "Color": {"fr": "Couleur", "zh": "颜色", "vi": "Màu sắc"},
    "next": {"fr": "suivant", "zh": "下一页", "vi": "tiếp"},
    "quit": {"fr": "quitter", "zh": "退出", "vi": "thoát"},
    "back": {"fr": "retour", "zh": "返回", "vi": "quay lại"},
    "DEFAULT LANGUAGE": {"fr": "LANGUE PAR DÉFAUT", "zh": "默认语言", "vi": "NGÔN NGỮ MẶC ĐỊNH"},
    "MENU COLOR": {"fr": "COULEUR DU MENU", "zh": "菜单颜色", "vi": "MÀU MENU"},
}

def ui_label(label):
    return UI_LABELS.get(label, {}).get(LANGUAGE, label)

def color_label(mode):
    labels = {
        "random": {"fr": "Aléatoire", "zh": "随机", "vi": "Ngẫu nhiên"},
        "Ocean": {"fr": "Océan", "zh": "海洋", "vi": "Đại dương"},
        "Red": {"fr": "Rouge", "zh": "红色", "vi": "Đỏ"},
        "Dark Red": {"fr": "Rouge foncé", "zh": "深红", "vi": "Đỏ đậm"},
        "Monochrome": {"fr": "Monochrome", "zh": "单色", "vi": "Đơn sắc"},
        "Inverted": {"fr": "Inversé", "zh": "反色", "vi": "Đảo màu"},
        "Green": {"fr": "Vert", "zh": "绿色", "vi": "Xanh lá"},
        "Gold": {"fr": "Or", "zh": "金色", "vi": "Vàng"},
        "Pink": {"fr": "Rose", "zh": "粉色", "vi": "Hồng"},
        "Purple": {"fr": "Violet", "zh": "紫色", "vi": "Tím"},
        "Orange": {"fr": "Orange", "zh": "橙色", "vi": "Cam"},
    }
    if mode == "random":
        return labels["random"].get(LANGUAGE, "Random")
    name = ["Ocean", "Red", "Dark Red", "Monochrome", "Inverted", "Green", "Gold", "Pink", "Purple", "Orange"][int(mode)]
    return labels[name].get(LANGUAGE, name)

def load_color():
    global COLOR_MODE
    try:
        with open(COLOR_FILE, "r", encoding="utf-8") as file:
            value = file.read().strip().lower()
        if value == "random" or value.isdigit() and 0 <= int(value) < len(COLOR_THEMES):
            COLOR_MODE = value
    except (FileNotFoundError, OSError):
        COLOR_MODE = "random"
    return COLOR_MODE

def save_color(mode):
    global COLOR_MODE
    if mode != "random" and not (mode.isdigit() and 0 <= int(mode) < len(COLOR_THEMES)):
        return
    os.makedirs(os.path.dirname(COLOR_FILE), exist_ok=True)
    with open(COLOR_FILE, "w", encoding="utf-8") as file:
        file.write(mode)
    COLOR_MODE = mode


FEATURE_LABELS = {
        "Doxbin": {"fr": "Doxbin", "zh": "Doxbin", "vi": "Doxbin"},
        "OSINT Framework": {"fr": "Framework OSINT", "zh": "OSINT 框架", "vi": "Khung OSINT"},
        "Name Finder": {"fr": "Recherche de nom", "zh": "姓名查找", "vi": "Tìm tên"},
        "Email Info": {"fr": "Infos email", "zh": "邮箱信息", "vi": "Thông tin email"},
        "Number Info": {"fr": "Infos numéro", "zh": "号码信息", "vi": "Thông tin số"},
        "Dox Creator": {"fr": "Créateur de dox", "zh": "Dox 创建器", "vi": "Tạo dox"},
        "Simple Dox": {"fr": "Dox simple", "zh": "简易 Dox", "vi": "Dox đơn giản"},
        "Search DB": {"fr": "Recherche base", "zh": "搜索数据库", "vi": "Tìm cơ sở dữ liệu"},
        "IP Lookup": {"fr": "Recherche IP", "zh": "IP 查询", "vi": "Tra cứu IP"},
        "Username Hunter": {"fr": "Recherche pseudo", "zh": "用户名猎手", "vi": "Tìm tên người dùng"},
        "Domain Intel": {"fr": "Renseignements domaine", "zh": "域名情报", "vi": "Thông tin tên miền"},
        "Social Scraper": {"fr": "Scraper social", "zh": "社交抓取器", "vi": "Quét mạng xã hội"},
        "VPN Detector": {"fr": "Détecteur VPN", "zh": "VPN 检测器", "vi": "Phát hiện VPN"},
        "Email Bomber (Gmail)": {"fr": "Bombardier email (Gmail)", "zh": "邮箱轰炸器 (Gmail)", "vi": "Gửi bom email (Gmail)"},
        "Email Bomber (Reset)": {"fr": "Bombardier email (Reset)", "zh": "邮箱轰炸器 (重置)", "vi": "Gửi bom email (Reset)"},
        "DDoS IP": {"fr": "DDoS IP", "zh": "DDoS IP", "vi": "DDoS IP"},
        "DDoS Website": {"fr": "DDoS site web", "zh": "DDoS 网站", "vi": "DDoS website"},
        "SMS Bomber": {"fr": "Bombardier SMS", "zh": "短信轰炸器", "vi": "Gửi bom SMS"},
        "Nuke": {"fr": "Nuke", "zh": "Nuke", "vi": "Nuke"},
        "Auto Raid": {"fr": "Raid automatique", "zh": "自动 Raid", "vi": "Raid tự động"},
        "Ban All": {"fr": "Bannir tous", "zh": "全部封禁", "vi": "Cấm tất cả"},
        "Kick All": {"fr": "Expulser tous", "zh": "全部踢出", "vi": "Đá tất cả"},
        "Mute All": {"fr": "Rendre muet tous", "zh": "全部禁言", "vi": "Tắt tiếng tất cả"},
        "Unban All": {"fr": "Débannir tous", "zh": "全部解封", "vi": "Bỏ cấm tất cả"},
        "Delete Channels": {"fr": "Supprimer les salons", "zh": "删除频道", "vi": "Xóa kênh"},
        "Delete Emojis": {"fr": "Supprimer les emojis", "zh": "删除表情", "vi": "Xóa emoji"},
        "Delete Stickers": {"fr": "Supprimer les stickers", "zh": "删除贴纸", "vi": "Xóa sticker"},
        "Create Channels": {"fr": "Créer des salons", "zh": "创建频道", "vi": "Tạo kênh"},
        "Create Roles": {"fr": "Créer des rôles", "zh": "创建角色", "vi": "Tạo vai trò"},
        "Create Categories": {"fr": "Créer des catégories", "zh": "创建分类", "vi": "Tạo danh mục"},
        "Rename Channels": {"fr": "Renommer les salons", "zh": "重命名频道", "vi": "Đổi tên kênh"},
        "Rename Roles": {"fr": "Renommer les rôles", "zh": "重命名角色", "vi": "Đổi tên vai trò"},
        "Edit Server": {"fr": "Modifier le serveur", "zh": "编辑服务器", "vi": "Chỉnh sửa máy chủ"},
        "Ghost Ping": {"fr": "Ping fantôme", "zh": "幽灵 Ping", "vi": "Ping ma"},
        "DM Spam": {"fr": "Spam DM", "zh": "私信垃圾信息", "vi": "Spam tin nhắn riêng"},
        "Webhook Spam": {"fr": "Spam webhook", "zh": "Webhook 垃圾信息", "vi": "Spam webhook"},
        "Lockdown": {"fr": "Verrouillage", "zh": "锁定", "vi": "Khóa máy chủ"},
        "Clone Server": {"fr": "Cloner le serveur", "zh": "克隆服务器", "vi": "Sao chép máy chủ"},
        "Message All": {"fr": "Message à tous", "zh": "向所有人发消息", "vi": "Nhắn tin tất cả"},
        "Mass Spam": {"fr": "Spam massif", "zh": "群发垃圾信息", "vi": "Spam hàng loạt"},
        "Mass Ban": {"fr": "Bannissement massif", "zh": "批量封禁", "vi": "Cấm hàng loạt"},
        "Mass Kick": {"fr": "Expulsion massive", "zh": "批量踢出", "vi": "Đá hàng loạt"},
        "Token Checker": {"fr": "Vérificateur de token", "zh": "Token 检查器", "vi": "Kiểm tra token"},
        "Server Cloner": {"fr": "Cloneur de serveur", "zh": "服务器克隆器", "vi": "Sao chép máy chủ"},
        "Web Lookup": {"fr": "Recherche web", "zh": "网络查询", "vi": "Tra cứu web"},
        "IP Localisation": {"fr": "Géolocalisation IP", "zh": "IP 定位", "vi": "Định vị IP"},
        "IP Operator": {"fr": "Opérateur IP", "zh": "IP 运营商", "vi": "Nhà mạng IP"},
        "IP Open Ports": {"fr": "Ports IP ouverts", "zh": "IP 开放端口", "vi": "Cổng IP mở"},
        "IP Pinger": {"fr": "Ping IP", "zh": "IP Ping", "vi": "Ping IP"},
        "IP DDoS": {"fr": "DDoS IP", "zh": "IP DDoS", "vi": "DDoS IP"},
        "IP Generator": {"fr": "Générateur IP", "zh": "IP 生成器", "vi": "Tạo IP"},
        "Discord Nitro": {"fr": "Discord Nitro", "zh": "Discord Nitro", "vi": "Discord Nitro"},
        "Amazon Giftcard": {"fr": "Carte cadeau Amazon", "zh": "亚马逊礼品卡", "vi": "Thẻ quà tặng Amazon"},
        "Netflix Giftcard": {"fr": "Carte cadeau Netflix", "zh": "Netflix 礼品卡", "vi": "Thẻ quà tặng Netflix"},
        "Roblox Giftcard": {"fr": "Carte cadeau Roblox", "zh": "Roblox 礼品卡", "vi": "Thẻ quà tặng Roblox"},
        "Apple Giftcard": {"fr": "Carte cadeau Apple", "zh": "Apple 礼品卡", "vi": "Thẻ quà tặng Apple"},
        "Steam Giftcard": {"fr": "Carte cadeau Steam", "zh": "Steam 礼品卡", "vi": "Thẻ quà tặng Steam"},
        "Google Play": {"fr": "Google Play", "zh": "Google Play", "vi": "Google Play"},
        "Spotify Giftcard": {"fr": "Carte cadeau Spotify", "zh": "Spotify 礼品卡", "vi": "Thẻ quà tặng Spotify"},
        "Hash Cracker": {"fr": "Crack de hash", "zh": "哈希破解器", "vi": "Bẻ khóa hash"},
        "Password Generator": {"fr": "Générateur de mots de passe", "zh": "密码生成器", "vi": "Tạo mật khẩu"},
        "Temp Mail": {"fr": "Email temporaire", "zh": "临时邮箱", "vi": "Email tạm thời"},
}

def feature_label(label):
    return FEATURE_LABELS.get(label, {}).get(LANGUAGE, label)
def apply_saved_color():
    if COLOR_MODE == "random":
        set_random_theme()
    else:
        set_theme(int(COLOR_MODE))

def sp(f, n): return os.path.join(PROJECT_DIR, "tools", f, n)
def cls():    os.system("cls" if os.name == "nt" else "clear")
def tw():     return shutil.get_terminal_size((100, 30)).columns
def th():     return shutil.get_terminal_size((100, 30)).lines
def norm(o):
    o = o.strip()
    return f"0{o}" if o.isdigit() and len(o) == 1 else o

def display_width(text):
    width = 0
    for char in text:
        if unicodedata.combining(char):
            continue
        width += 2 if unicodedata.east_asian_width(char) in "WFA" else 1
    return width

_RAIN = list("01▓▒░│┤╣║╗╝┐└┴┬├─┼╚╔╩╦╠═╬┘┌AB3F9E#%&?$")

NOVA_ASCII = [
    " ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗",
    " ████╗  ██║██╔═══██╗██║   ██║██╔══██╗",
    " ██╔██╗ ██║██║   ██║██║   ██║███████║",
    " ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║",
    " ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║",
    " ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝",
]

LOADING_LINES = [
    r"  _   _  ______      __       _______ ____   ____  _",
    r" | \ | |/ __ \ \    / /\     |__   __/ __ \ / __ \| |",
    r" |  \| | |  | \ \  / /  \       | | | |  | | |  | | |",
    r" | . ` | |  | |\ \/ / /\ \      | | | |  | | |  | | |",
    r" | |\  | |__| | \  / ____ \     | | | |__| | |__| | |____",
    r" |_| \_|\____/   \/_/    \_\    |_|  \____/ \____/|______|",
]

MENU_ASCII = [
    r"  _   _  ______      __       _______ ____   ____  _",
    r" | \ | |/ __ \ \    / /\     |__   __/ __ \ / __ \| |",
    r" |  \| | |  | \ \  / /  \       | | | |  | | |  | | |",
    r" | . ` | |  | |\ \/ / /\ \      | | | |  | | |  | | |",
    r" | |\  | |__| | \  / ____ \     | | | |__| | |__| | |____",
]

def _rain_frame(w, h, t):
    f = Text()
    for row in range(h):
        for col in range(w):
            spd = 1.0 + (col % 7) * 0.3
            ph  = int((t * spd * 12 + col * 3.7)) % len(_RAIN)
            ch  = _RAIN[(col * 17 + row * 3 + ph) % len(_RAIN)]
            b   = int(0x55 + abs(math.sin(col * 0.4 + t * 0.8)) * (0xAA - 0x55))
            if random.random() < 0.03: b = 0xFF
            f.append(ch, style=C_MID)
        if row < h - 1:
            f.append("\n")
    return f

def play_intro():
    w = tw(); h = max(th() - 2, 20); t0 = time.monotonic()
    with Live(console=console, screen=True, refresh_per_second=24, transient=True) as live:
        while time.monotonic() - t0 < 1.0:
            live.update(_rain_frame(w, h, time.monotonic() - t0))
            time.sleep(1 / 24)
    fl = LOADING_LINES
    fh = len(fl); ly = max(0, h // 2 - fh // 2)
    lc = [f"#00{max(0x80, min(0xE0, int(0x80 + i/max(fh-1,1)*(0xE0-0x80)))):02X}FF"
          for i in range(fh)]
    with Live(console=console, screen=True, refresh_per_second=24, transient=True) as live:
        t2 = time.monotonic()
        while time.monotonic() - t2 < 1.8:
            t  = time.monotonic() - t0
            fd = min((time.monotonic() - t2) / 1.8, 1.0)
            frame = Text()
            for row in range(h):
                rel = row - ly
                if 0 <= rel < fh and random.random() < fd:
                        frame.append(f"  {fl[rel]}\n", style=f"{C_NEON} bold")
                else:
                    for col in range(w):
                        spd = 1.0 + (col % 7) * 0.3
                        ph  = int((t * spd * 12 + col * 3.7)) % len(_RAIN)
                        ch  = _RAIN[(col * 17 + row * 3 + ph) % len(_RAIN)]
                        b   = int(0x45 + (1 - fd) * (0x55 - 0x45))
                        frame.append(ch, style=C_MID)
                    frame.append("\n")
            live.update(frame)
            time.sleep(1 / 24)

def gradient_line(text, w=None):
    t = Text(); n = len(text)
    for i, ch in enumerate(text):
        frac = i / max(n - 1, 1)
        b = int(0xA0 + frac * (0xFF - 0xA0))
        t.append(ch, style=f"{C_NEON} bold")
    return t

_NOISE = list("#%&!?$@+-=~^/*|\\><▓▒░")

def glitch_reveal_rich(text):
    n = len(text); revealed = [False] * n
    with Live(console=console, refresh_per_second=30, transient=True) as live:
        for _ in range(6):
            t = Text()
            for ch in text:
                if random.random() < 0.6:
                    t.append(random.choice(_NOISE), style=C_BLOOD)
                else:
                    t.append(ch, style=f"{C_NEON} bold")
            live.update(Align.center(t)); time.sleep(0.04)
        s = 0
        while not all(revealed):
            if s < n:       revealed[s]     = True
            if n - 1 - s >= 0: revealed[n-1-s] = True
            t = Text()
            for i, ch in enumerate(text):
                if revealed[i]:
                    t.append(ch, style=f"{C_NEON} bold")
                else:
                    t.append(random.choice(_NOISE), style=C_BLOOD)
            live.update(Align.center(t)); time.sleep(0.028); s += 1
    console.print(Align.center(gradient_line(text)))

def rich_boot_bars():
    tasks_cfg = [
        ("KERNEL LOAD",     0.18), ("MEMORY ALLOC",    0.22),
        ("NET INTERFACE",   0.19), ("CRYPTO ENGINE",   0.15),
        ("OSINT MODULE",    0.20), ("NUKER MODULE",    0.17),
        ("RENDER PIPELINE", 0.16), ("DARK WEB LAYER",  0.21),
    ]
    with Progress(
        SpinnerColumn(style=f"{C_NEON} bold"),
        TextColumn(f"[{C_SILVER}]{{task.description:<20}}"),
        BarColumn(bar_width=32, style=C_BLOOD, complete_style=C_NEON, finished_style=C_BRIGHT),
        TextColumn(f"[{C_NEON} bold]{{task.percentage:>5.1f}}%"),
        console=console, transient=False,
    ) as progress:
        job_ids = [progress.add_task(label, total=100) for label, _ in tasks_cfg]
        while not all(progress.tasks[jid].finished for jid in job_ids):
            for idx, jid in enumerate(job_ids):
                if not progress.tasks[jid].finished:
                    progress.advance(jid, random.uniform(3, 14))
                    time.sleep(tasks_cfg[idx][1] * random.uniform(0.5, 1.5) / 10)

LOGO_LINES = MENU_ASCII
LOGO_COLORS = [C_NEON, C_RED, C_MID, C_DARK, C_BLOOD]

def set_random_theme():
    global C_BLOOD, C_DARK, C_MID, C_NEON, C_BRIGHT
    global C_WHITE, C_SILVER, C_DIM, C_RED, C_GOLD, C_GOLD2, LOGO_COLORS

    theme = random.choice(COLOR_THEMES)
    C_BLOOD = theme["blood"]
    C_DARK = theme["dark"]
    C_MID = theme["mid"]
    C_RED = theme["mid"]
    C_NEON = theme["neon"]
    C_BRIGHT = theme["bright"]
    C_WHITE = theme["white"]
    C_SILVER = theme["silver"]
    C_DIM = theme["dim"]
    C_GOLD = theme["gold"]
    C_GOLD2 = theme["gold2"]
    LOGO_COLORS = [C_NEON, C_RED, C_MID, C_DARK, C_BLOOD]

def set_theme(index):
    global C_BLOOD, C_DARK, C_MID, C_NEON, C_BRIGHT
    global C_WHITE, C_SILVER, C_DIM, C_RED, C_GOLD, C_GOLD2, LOGO_COLORS

    theme = COLOR_THEMES[index]
    C_BLOOD = theme["blood"]
    C_DARK = theme["dark"]
    C_MID = theme["mid"]
    C_RED = theme["mid"]
    C_NEON = theme["neon"]
    C_BRIGHT = theme["bright"]
    C_WHITE = theme["white"]
    C_SILVER = theme["silver"]
    C_DIM = theme["dim"]
    C_GOLD = theme["gold"]
    C_GOLD2 = theme["gold2"]
    LOGO_COLORS = [C_NEON, C_RED, C_MID, C_DARK, C_BLOOD]

def draw_logo_rich():
    if len(LOGO_LINES[0]) <= tw() - 2:
        for line, col in zip(LOGO_LINES, LOGO_COLORS):
            console.print(f" {line}", style=f"{col} bold")
    else:
        console.print(" NOVA-TOOL", style=f"{C_NEON} bold")

def first_run():
    flag = os.path.join(PROJECT_DIR, "data", ".launched")
    if not os.path.exists(flag):
        open_community_links()
        with open(flag, "w") as f:
            f.write("1")

def boot():
    global THEME_FOR_NEXT_MENU
    load_language()
    load_color()
    apply_saved_color()
    THEME_FOR_NEXT_MENU = True
    first_run()
    play_intro()
    cls(); console.print()
    for i, (line, col) in enumerate(zip(LOGO_LINES, LOGO_COLORS)):
        time.sleep(0.06)
        console.print(f" {line}", style=f"{col} bold")
    console.print()
    glitch_reveal_rich("NOVA-TOOL  //  SYSTEM INITIALIZATION")
    console.print()
    rich_boot_bars()
    console.print()
    console.print(Panel(
        Align.center(Text.from_markup(
            f"[{C_NEON} bold][ ALL SYSTEMS ONLINE ]\n"
            f"[{C_MID}]NOVA-TOOL v1.0  ·  by {AUTHOR}"
        )),
        border_style=C_BLOOD, box=box.DOUBLE_EDGE, padding=(0, 2),
    ))
    time.sleep(0.5)

def draw_header():
    cls(); console.print()
    draw_logo_rich(); console.print()
    left  = Text.from_markup(f"[{C_MID}] v1.0  [{C_DARK}]|[/]  by [{C_WHITE} bold]{AUTHOR}")
    right = Text.from_markup("")
    w = tw(); gap = w - len(f" v1.0  |  by {AUTHOR}") - 2
    console.print(left, end=""); console.print(" " * max(1, gap), end=""); console.print(right)
    seg = (w - 2) // 3
    console.print(f"[{C_BLOOD}]" + "─"*seg + f"[{C_MID}]" + "─"*seg + f"[{C_NEON}]" + "─"*(w-2-seg*2))
    console.print()

def make_cell(key, label):
    if not key.strip(): return Text(label, style=C_DIM)
    t = Text()
    t.append("[", style="#FFFFFF"); t.append(key, style="#FFFFFF bold")
    t.append("] ", style="#FFFFFF"); t.append(label, style="#FFFFFF bold")
    return t

def draw_tree(title, items):
    console.print(Text.from_markup(f"[{C_BLOOD}] ┌── [{C_NEON} bold]{title}"))
    for i, e in enumerate(items):
        last = (i == len(items) - 1)
        b = "└──" if last else "├──"
        if e[0] == "cat":
            console.print(f"[{C_BLOOD}] │")
            console.print(Text.from_markup(f"[{C_BLOOD}] {b} [{C_NEON} bold]{e[1]}"))
        elif e[0] == "cols":
            pairs = e[1]; col_w = max(20, (tw() - 12) // 2)
            for j in range(0, len(pairs), 2):
                L = pairs[j]; R = pairs[j+1] if j+1 < len(pairs) else None
                sub = "└──" if (j+2 >= len(pairs)) else "├──"
                pad = col_w - display_width(f"[{L[0]}] {L[1]}")
                line = Text.from_markup(f"[{C_BLOOD}] │   [{C_DARK}]{sub} ")
                line.append_text(make_cell(L[0], L[1]))
                line.append(" " * max(1, pad))
                if R:
                    line.append_text(Text.from_markup(f"[{C_BLOOD}]│  "))
                    line.append_text(make_cell(R[0], R[1]))
                console.print(line)
        elif e[0] in ("nav", "navlast"):
            b2 = "└──" if e[0] == "navlast" else "├──"
            console.print(f"[{C_BLOOD}] │")
            console.print(Text.from_markup(
                f"[{C_BLOOD}] {b2}  [#FFFFFF][[#FFFFFF bold]{e[1]}[#FFFFFF]]  [#FFFFFF bold]{e[2]}"
            ))
    console.print()

def prompt(loc):
    console.print(Text.from_markup(
        f"[{C_BLOOD}] ┌─[[{C_NEON} bold]nova[{C_DARK}]@[{C_RED}]tool[{C_BLOOD}]]"
        f"──[[{C_WHITE} bold]{loc}[{C_BLOOD}]]"
    ), end="\n")
    raw = input(f"{_ansi(C_MID)} └──{_ansi(C_NEON)}\033[1m >> \033[0m").strip()
    return norm(raw)

def C_to_ansi(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f"38;2;{r};{g};{b}m"

def show(loc, title, items):
    global THEME_FOR_NEXT_MENU
    if THEME_FOR_NEXT_MENU:
        THEME_FOR_NEXT_MENU = False
    draw_header(); draw_tree(title, items); return prompt(loc)

def run(fr, en, zh=None):
    apply_saved_color()
    sources = {"fr": fr, "en": en, "zh": zh or en, "vi": en}
    src = sources.get(LANGUAGE, en)
    try:
        environment = os.environ.copy()
        environment["NOVA_LANGUAGE"] = LANGUAGE
        runner = os.path.join(PROJECT_DIR, "tools", "run_tool.py")
        subprocess.run(["python", runner, src], env=environment)
    except: console.print(f"[{C_NEON} bold]  [!] script not found")
    input(f"{_ansi(C_MID)}  press enter to continue...\033[0m")

def _ansi(h):
    hx = h.lstrip("#"); r,g,b = int(hx[0:2],16),int(hx[2:4],16),int(hx[4:6],16)
    return f"\033[38;2;{r};{g};{b}m"

def _panel(title, desc):
    console.print(); console.print(Panel(
        Align.center(Text.from_markup(f"[{C_GOLD} bold]* {title} *\n[{C_SILVER}]{desc}")),
        border_style=C_BLOOD, box=box.DOUBLE_EDGE, padding=(0,3), width=min(60, tw()-2)
    )); console.print()

def _open_links(pairs):
    for name, url in pairs:
        t = Text()
        t.append(" │   ├── ", style=C_BLOOD)
        t.append(f"{name:<20}", style=C_WHITE)
        t.append(" ──>  ", style=C_DIM)
        t.append(url, style=C_GOLD2)
        console.print(t)
        webbrowser.open(url); time.sleep(0.08)
    console.print(); input(f"{_ansi(C_MID)}  press enter...\033[0m")

def tool_username_hunter():
    _panel("USERNAME HUNTER", "Cherche un pseudo sur 12 plateformes")
    u = input(f"{_ansi(C_MID)}  username >> \033[0m").strip()
    if not u: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Results for : {u}"))
    _open_links([
        ("Twitter/X", f"https://x.com/{u}"),
        ("Instagram", f"https://instagram.com/{u}"),
        ("TikTok",    f"https://tiktok.com/@{u}"),
        ("Reddit",    f"https://reddit.com/u/{u}"),
        ("Twitch",    f"https://twitch.tv/{u}"),
        ("YouTube",   f"https://youtube.com/@{u}"),
        ("Steam",     f"https://steamcommunity.com/id/{u}"),
        ("Snapchat",  f"https://snapchat.com/add/{u}"),
        ("Pinterest", f"https://pinterest.com/{u}"),
        ("Medium",    f"https://medium.com/@{u}"),
    ])

def tool_domain_intel():
    _panel("DOMAIN INTEL", "WHOIS · DNS · SSL · Shodan · VirusTotal")
    d = input(f"{_ansi(C_MID)}  domain (ex: google.com) >> \033[0m").strip()
    if not d: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Intel for : {d}"))
    _open_links([
        ("WHOIS",       f"https://who.is/whois/{d}"),
        ("DNS Lookup",  f"https://dnschecker.org/#A/{d}"),
        ("Subdomains",  f"https://subdomainfinder.c99.nl/?domain={d}"),
        ("SSL Cert",    f"https://crt.sh/?q={d}"),
        ("VirusTotal",  f"https://virustotal.com/gui/domain/{d}"),
        ("Shodan",      f"https://shodan.io/search?query=hostname%3A{d}"),
        ("URLScan",     f"https://urlscan.io/search/#domain%3A{d}"),
    ])

def tool_social_scraper():
    _panel("SOCIAL SCRAPER", "Outils de scraping de profils publics")
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Social Scraper Tools"))
    _open_links([
        ("Instagram",    "https://imginn.com/"),
        ("TikTok",       "https://exolyt.com/"),
        ("Facebook ID",  "https://lookup-id.com/"),
        ("LinkedIn",     "https://osint.support/"),
        ("Social Search","https://socialsearcher.com/"),
    ])

def tool_vpn_detector():
    _panel("VPN DETECTOR", "Détecte VPN · Proxy · Tor sur une IP")
    ip = input(f"{_ansi(C_MID)}  IP address >> \033[0m").strip()
    if not ip: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── VPN Check : {ip}"))
    _open_links([
        ("IPQualityScore", f"https://ipqualityscore.com/free-ip-lookup-proxy-vpn-test/lookup/{ip}"),
        ("IPHub",          f"https://iphub.info/ip/{ip}"),
        ("AbuseIPDB",      f"https://abuseipdb.com/check/{ip}"),
        ("Shodan",         f"https://shodan.io/host/{ip}"),
        ("GreyNoise",      f"https://viz.greynoise.io/ip/{ip}"),
    ])

def tool_sms_bomber():
    _panel("SMS BOMBER", "Plateformes de flood SMS (web)")
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── SMS Services"))
    _open_links([
        ("SMS24",        "https://sms24.me/"),
        ("SMSPool",      "https://smspool.net/"),
        ("TextBelt",     "https://textbelt.com/"),
        ("Receive-SMS",  "https://receive-sms.com/"),
        ("SMS Receive",  "https://smsreceivefree.com/"),
    ])

def tool_token_checker():
    import urllib.request, json
    _panel("TOKEN CHECKER", "Vérifie la validité d'un token Discord")
    token = input(f"{_ansi(C_MID)}  Discord token >> \033[0m").strip()
    if not token: return
    try:
        req = urllib.request.Request(
            "https://discord.com/api/v9/users/@me",
            headers={"Authorization": token}
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
        console.print(Panel(
            Text.from_markup(
                f"[{C_GOLD} bold]* TOKEN VALID *\n\n"
                f"[{C_SILVER}]User   : [{C_WHITE} bold]{d.get('username','?')}#{d.get('discriminator','0')}\n"
                f"[{C_SILVER}]ID     : [{C_WHITE}]{d.get('id','?')}\n"
                f"[{C_SILVER}]Email  : [{C_WHITE}]{d.get('email','hidden')}\n"
                f"[{C_SILVER}]Nitro  : [{C_WHITE}]{'Yes' if d.get('premium_type') else 'No'}\n"
                f"[{C_SILVER}]Phone  : [{C_WHITE}]{'Yes' if d.get('phone') else 'No'}"
            ),
            border_style=C_GOLD, box=box.DOUBLE_EDGE, padding=(0, 3)
        ))
    except Exception:
        console.print(f"\n[{C_NEON} bold]  [!] INVALID TOKEN or network error")
    console.print(); input(f"{_ansi(C_MID)}  press enter...\033[0m")

def tool_server_cloner():
    _panel("SERVER CLONER", "Clone complet d'un serveur Discord")
    console.print(f"[{C_NEON} bold]  [!] Server cloner is unavailable in this build.")
    console.print(); input(f"{_ansi(C_MID)}  press enter...\033[0m")

def tool_hash_cracker():
    _panel("HASH CRACKER", "Crack MD5 · SHA1 · SHA256 via lookup online")
    h = input(f"{_ansi(C_MID)}  hash >> \033[0m").strip()
    if not h: return
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Hash : {h[:40]}{'...' if len(h)>40 else ''}"))
    _open_links([
        ("CrackStation", "https://crackstation.net/"),
        ("HashKiller",   "https://hashkiller.io/listmanager"),
        ("MD5Decrypt",   "https://md5decrypt.net/"),
        ("Hashes.com",   "https://hashes.com/en/decrypt/hash"),
        ("Nitrxgen",     f"https://www.nitrxgen.net/md5db/{h}"),
    ])

def tool_password_gen():
    _panel("PASSWORD GENERATOR", "Génère des mots de passe ultra-sécurisés")
    try: length = int(input(f"{_ansi(C_MID)}  length (default 20) >> \033[0m").strip() or "20")
    except ValueError: length = 20
    charset = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    console.print(); console.print(Text.from_markup(f"[{C_NEON} bold] ┌── 8 passwords  ·  length {length}"))
    for i in range(8):
        pwd = ''.join(random.choices(charset, k=length))
        t = Text()
        t.append(f" │   [{i+1:02d}] ", style=C_BLOOD)
        t.append(pwd, style=f"{C_WHITE} bold")
        console.print(t)
    console.print(); input(f"{_ansi(C_MID)}  press enter...\033[0m")

def tool_temp_mail():
    _panel("TEMP MAIL", "Adresse mail jetable instantanée")
    console.print(Text.from_markup(f"[{C_NEON} bold] ┌── Temp Mail Services"))
    _open_links([
        ("10MinuteMail",  "https://10minutemail.com/"),
        ("Guerrilla Mail","https://guerrillamail.com/"),
        ("TempMail",      "https://temp-mail.org/"),
        ("Mailnull",      "https://www.mailnull.com/"),
        ("Dispostable",   "https://dispostable.com/"),
        ("FakeMail",      "https://www.fakemail.net/"),
    ])

def home():
    while True:
        o = show("~/home", "HOME  ·  1/11", [
            ("cat",    "NOVA-TOOL"),
            ("nav",    "01", ui_label("Profile")),
            ("nav",    "02", f"{ui_label('Language')} ({language_label(LANGUAGE)})"),
            ("nav",    "03", f"{ui_label('Color')} ({color_label(COLOR_MODE)})"),
            ("nav",    "N", f"{ui_label('next')}  ──>  osint"),
            ("navlast","Q", ui_label("quit")),
        ])
        if o == "01": webbrowser.open(PROFILE)
        elif o == "02": page_language()
        elif o == "03": page_color()
        elif o.upper() == "N": page_osint(); return
        elif o.upper() == "Q": cls(); sys.exit(0)

def page_language():
    while True:
        o = show("~/language", ui_label("Language"), [
            ("cat", ui_label("DEFAULT LANGUAGE")),
            ("cols", [
                ("01", "English"),
                ("02", "Français"),
                ("03", "简体中文"),
                ("04", "Tiếng Việt"),
            ]),
            ("navlast", "B", ui_label("back")),
        ])
        choices = {"01": "en", "02": "fr", "03": "zh", "04": "vi"}
        if o.upper() == "B":
            return
        if o in choices:
            save_language(choices[o])
            console.print(f"[{C_NEON} bold]  Language saved: {language_label(LANGUAGE)}")
            input(f"{_ansi(C_MID)}  press enter to continue...\033[0m")
            return

def page_color():
    choices = {
        "01": "random",
        "02": "0",
        "03": "1",
        "04": "2",
        "05": "3",
        "06": "4",
        "07": "5",
        "08": "6",
        "09": "7",
        "10": "8",
        "11": "9",
    }
    labels = [
        ("01", color_label("random")), ("02", color_label("0")), ("03", color_label("1")),
        ("04", color_label("2")), ("05", color_label("3")), ("06", color_label("4")),
        ("07", color_label("5")), ("08", color_label("6")), ("09", color_label("7")),
        ("10", color_label("8")), ("11", color_label("9")),
    ]
    while True:
        o = show("~/color", ui_label("Color"), [
            ("cat", ui_label("MENU COLOR")),
            ("cols", labels),
            ("navlast", "B", ui_label("back")),
        ])
        if o.upper() == "B":
            return
        if o in choices:
            save_color(choices[o])
            apply_saved_color()
            console.print(f"[{C_NEON} bold]  Color saved: {color_label(COLOR_MODE)}")
            input(f"{_ansi(C_MID)}  press enter to continue...\033[0m")
            return
        if o in choices:
            save_language(choices[o])
            console.print(f"[{C_NEON} bold]  Language saved: {language_label(LANGUAGE)}")
            input(f"{_ansi(C_MID)}  press enter to continue...\033[0m")
            return

def page_osint():
    SC = {
        "03": (sp("name-tracker","fr.py"),      sp("name-tracker","en.py")),
        "05": (sp("email-info","fr.py"),        sp("email-info","en.py")),
        "06": (sp("number-info","fr.py"),       sp("number-info","en.py")),
        "07": (sp("dox","fr.py"),               sp("dox","en.py")),
        "08": (sp("simple-dox","fr.py"),        sp("simple-dox","en.py")),
        "09": (sp("search-database","fr.py"),   sp("search-database","en.py")),
        "10": (sp("ip-lookup","fr.py"),         sp("ip-lookup","en.py")),
    }
    while True:
        o = show("~/osint", "OSINT  ·  2/11", [
            ("cat",  "OSINT"),
            ("cols", [
                ("01",feature_label("Doxbin")),          ("02",feature_label("OSINT Framework")),
                ("03",feature_label("Name Finder")),     ("05",feature_label("Email Info")),
                ("06",feature_label("Number Info")),     ("07",feature_label("Dox Creator")),
                ("08",feature_label("Simple Dox")),      ("09",feature_label("Search DB")),
                ("10",feature_label("IP Lookup")),       ("11",feature_label("Username Hunter")),
                ("12",feature_label("Domain Intel")),    ("13",feature_label("Social Scraper")),
                ("14",feature_label("VPN Detector")),    ("  ",""),
            ]),
            ("nav",    "B", ui_label("back")),
            ("navlast","N", f"{ui_label('next')}  ──>  attack"),
        ])
        if   o.upper() == "N": page_attack(); return
        elif o.upper() == "B": home();        return
        elif o == "01": webbrowser.open("https://doxbin.com/")
        elif o == "02": webbrowser.open("https://osintframework.com/")
        elif o == "11": tool_username_hunter()
        elif o == "12": tool_domain_intel()
        elif o == "13": tool_social_scraper()
        elif o == "14": tool_vpn_detector()
        elif o in SC:   run(*SC[o])

def page_attack():
    while True:
        o = show("~/attack", "ATTACK  ·  3/11", [
            ("cat",  "ATTACK"),
            ("cols", [
                ("01",feature_label("Email Bomber (Gmail)")), ("02",feature_label("Email Bomber (Reset)")),
                ("03",feature_label("DDoS IP")),              ("04",feature_label("DDoS Website")),
                ("05",feature_label("SMS Bomber")),           ("  ",""),
            ]),
            ("nav",    "B", ui_label("back")),
            ("navlast","N", f"{ui_label('next')}  ──>  nuker 1/2"),
        ])
        if   o.upper() == "N": page_nuker_a(); return
        elif o.upper() == "B": page_osint();   return
        elif o == "05": tool_sms_bomber()
        elif o == "01": run(sp("email-bomber","fr.py"),       sp("email-bomber","en.py"))
        elif o == "02": run(sp("email-bomber-reset","fr.py"), sp("email-bomber-reset","en.py"))
        elif o in ("03","04"): webbrowser.open("https://stresserai.ru/hub")

def page_nuker_a():
    NK = {f"{i:02d}" for i in range(1,13)}
    while True:
        o = show("~/nuker", "NUKER  ·  4/11  [1/2]", [
            ("cat",  "DISCORD NUKER"),
            ("cols", [
                ("01",feature_label("Nuke")),            ("02",feature_label("Auto Raid")),
                ("03",feature_label("Ban All")),         ("04",feature_label("Kick All")),
                ("05",feature_label("Mute All")),        ("06",feature_label("Unban All")),
                ("07",feature_label("Delete Channels")), ("08",feature_label("Delete Emojis")),
                ("09",feature_label("Delete Stickers")), ("10",feature_label("Create Channels")),
                ("11",feature_label("Create Roles")),    ("12",feature_label("Create Categories")),
            ]),
            ("nav",    "B", ui_label("back")),
            ("navlast","N", f"{ui_label('next')}  ──>  nuker 2/2"),
        ])
        if   o.upper() == "N": page_nuker_b(); return
        elif o.upper() == "B": page_attack();  return
        elif o in NK: open_community_links()

def page_nuker_b():
    NK = {f"{i:02d}" for i in range(1,13)}
    while True:
        o = show("~/nuker", "NUKER  ·  5/11  [2/2]", [
            ("cat",  "DISCORD NUKER"),
            ("cols", [
                ("01",feature_label("Rename Channels")), ("02",feature_label("Rename Roles")),
                ("03",feature_label("Edit Server")),     ("04",feature_label("Ghost Ping")),
                ("05",feature_label("DM Spam")),         ("06",feature_label("Webhook Spam")),
                ("07",feature_label("Lockdown")),        ("08",feature_label("Clone Server")),
                ("09",feature_label("Message All")),     ("10",feature_label("Mass Spam")),
                ("11",feature_label("Mass Ban")),        ("12",feature_label("Mass Kick")),
            ]),
            ("cols",    [("X","Config Token"), ("00","Start Nuker")]),
            ("cat",     "DISCORD TOOLS"),
            ("cols",    [("T1",feature_label("Token Checker")), ("T2",feature_label("Server Cloner"))]),
            ("nav",    "B", f"{ui_label('back')}  ──>  nuker 1/2"),
            ("navlast","N", f"{ui_label('next')}  ──>  ip tools"),
        ])
        if   o.upper() == "N": page_ip();      return
        elif o.upper() == "B": page_nuker_a(); return
        elif o in NK: open_community_links()
        elif o == "00": subprocess.run(["node", os.path.join(PROJECT_DIR, "bot", "index.js")], shell=True)
        elif o.upper() == "X":
            console.print(f"[{C_MID}]  config  ──>  {os.path.join(PROJECT_DIR, 'config', 'discord-nuker.json')}")
            input("  enter...")
        elif o.upper() == "T1": tool_token_checker()
        elif o.upper() == "T2": tool_server_cloner()

def page_ip():
    SC = {
        "01": (sp("ip-all-lookup","fr.py"),   sp("ip-all-lookup","en.py")),
        "02": (sp("ip-localisation","fr.py"), sp("ip-localisation","en.py")),
        "03": (sp("ip-operator","fr.py"),     sp("ip-operator","en.py")),
        "04": (sp("ip-open-ports","fr.py"),   sp("ip-open-ports","en.py")),
        "05": (sp("ip-pinger","fr.py"),       sp("ip-pinger","en.py")),
        "07": (sp("ip-generator","fr.py"),    sp("ip-generator","en.py")),
    }
    while True:
        o = show("~/ip-tools", "IP TOOLS  ·  6/11", [
            ("cat",  "IP TOOLS"),
            ("cols", [
                ("01",feature_label("Web Lookup")),    ("02",feature_label("IP Localisation")),
                ("03",feature_label("IP Operator")),   ("04",feature_label("IP Open Ports")),
                ("05",feature_label("IP Pinger")),     ("06",feature_label("IP DDoS")),
                ("07",feature_label("IP Generator")),  ("  ",""),
            ]),
            ("nav",    "B", ui_label("back")),
            ("navlast","N", f"{ui_label('next')}  ──>  generator"),
        ])
        if   o.upper() == "N": page_gen();     return
        elif o.upper() == "B": page_nuker_b(); return
        elif o == "06": webbrowser.open("https://stresserai.ru/hub")
        elif o in SC:   run(*SC[o])

def page_gen():
    nitro = (sp("nitro-generator","fr.py"), sp("nitro-generator","en.py"))
    gen   = (sp("generator","fr.py"),       sp("generator","en.py"))
    gmap  = {f"{i:02d}": (nitro if i==1 else gen) for i in range(1,9)}
    while True:
        o = show("~/generator", "GENERATOR  ·  7/11", [
            ("cat",  "GENERATOR"),
            ("cols", [
                ("01",feature_label("Discord Nitro")),    ("02",feature_label("Amazon Giftcard")),
                ("03",feature_label("Netflix Giftcard")), ("04",feature_label("Roblox Giftcard")),
                ("05",feature_label("Apple Giftcard")),   ("06",feature_label("Steam Giftcard")),
                ("07",feature_label("Google Play")),      ("08",feature_label("Spotify Giftcard")),
            ]),
            ("nav",    "B", ui_label("back")),
            ("navlast","N", f"{ui_label('next')}  ──>  crypto & utils"),
        ])
        if   o.upper() == "N": page_crypto(); return
        elif o.upper() == "B": page_ip();     return
        elif o in gmap: run(*gmap[o])

def page_crypto():
    while True:
        o = show("~/crypto-utils", "CRYPTO & UTILS  ·  8/11", [
            ("cat",  "CRYPTO & UTILS"),
            ("cols", [
                ("01",feature_label("Hash Cracker")),       ("02",feature_label("Password Generator")),
                ("03",feature_label("Temp Mail")),          ("  ",""),
            ]),
            ("nav",    "B", f"{ui_label('back')}  ──>  generator"),
            ("navlast","N", f"{ui_label('next')}  ──>  dark web 1/2"),
        ])
        if   o.upper() == "N": page_dw_a();  return
        elif o.upper() == "B": page_gen();   return
        elif o == "01": tool_hash_cracker()
        elif o == "02": tool_password_gen()
        elif o == "03": tool_temp_mail()

ALL_LINKS = [
    ("01","Mail2Tor",        "http://mail2tor2zyjdctd.onion/"),
    ("02","Hidden Wiki",     "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/"),
    ("03","ProPublica",      "https://www.propub3r6espa33w.onion/"),
    ("04","DuckDuckGo",      "http://3g2upl4pq6kufc4m.onion/"),
    ("05","SecureDrop",      "https://secrdrop5wyphb5x.onion/"),
    ("06","Sci-Hub",         "http://scihub22266oqcxt.onion/"),
    ("07","CIA Onion",       "http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion/"),
    ("08","Hidden Answers",  "http://answerszuvs3gg2l64e6hmnryudl5zgrmwm3vh65hzszdghblddvfiqd.onion/"),
    ("09","IPLogger",        "https://iplogger.org/"),
    ("10","Grabify",         "https://grabify.link/"),
    ("11","Whatstheirip",    "https://whatstheirip.tech/"),
    ("12","Doxbin",          "https://doxbin.net/"),
    ("13","OSINT Industries","https://osint.industries/"),
    ("14","Epieos",          "https://epieos.com/"),
    ("15","Nuwber",          "https://nuwber.fr/"),
    ("16","OSINT Framework", "https://osintframework.com/"),
    ("17","Whatsmyname",     "https://whatsmyname.app/"),
    ("18","IPInfo",          "https://ipinfo.io/"),
    ("19","Stresser.zone",   "https://stresserai.ru/hub"),
    ("20","Stresse.ru",      "https://stresse.ru/"),
    ("21","StarkStresser",   "https://starkstresser.net/"),
    ("22","DDoS.services",   "https://ddos.services/"),
    ("23","Torch",           "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/"),
    ("24","Dark Mixer",      "http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/"),
    ("25","Onionwallet",     "http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/"),
    ("26","Spylink",         "https://www.spylink.net/"),
    ("27","Danex",           "http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/"),
]
_UM = {k:u for k,_,u in ALL_LINKS}
_NM = {k:n for k,n,_ in ALL_LINKS}

def _reveal(o):
    if o in _UM:
        console.print(); console.print(Panel(
            Text.from_markup(f"[{C_NEON} bold]{_NM[o]}\n[{C_DARK}]{_UM[o]}"),
            border_style=C_BLOOD, box=box.HEAVY, padding=(0,2),
            width=min(len(_UM[o])+8, tw()-2),
        )); input(f"{_ansi(C_MID)}  enter to continue...\033[0m")

def page_dw_a():
    chunk = ALL_LINKS[:14]
    while True:
        o = show("~/darkweb", "DARK WEB  ·  9/11  [1/2]", [
            ("cat",  "DARK WEB LINKS"),
            ("cols", [(k,n) for k,n,_ in chunk]),
            ("nav",    "B", "back"),
            ("navlast","N", "next  ──>  dark web 2/2"),
        ])
        if   o.upper() == "N": page_dw_b();   return
        elif o.upper() == "B": page_crypto();  return
        else: _reveal(o)

def page_dw_b():
    chunk = ALL_LINKS[14:]
    while True:
        o = show("~/darkweb", "DARK WEB  ·  10/11  [2/2]", [
            ("cat",  "DARK WEB LINKS"),
            ("cols", [(k,n) for k,n,_ in chunk]),
            ("nav",    "B", f"{ui_label('back')}  ──>  dark web 1/2"),
            ("navlast","N", f"{ui_label('next')}  ──>  about"),
        ])
        if   o.upper() == "N": page_about(); return
        elif o.upper() == "B": page_dw_a();  return
        else: _reveal(o)

def page_about():
    while True:
        o = show("~/about", "ABOUT  ·  11/11", [
            ("cat",  "INFO"),
            ("cols", [
                ("  ",f"author   ──>  {AUTHOR}"),  ("  ","version  ──>  3.0"),
            ]),
            ("cat",    "all features available in this build"),
            ("navlast","B",  ui_label("back")),
        ])
        if o.upper() == "B": page_dw_b(); return

if __name__ == "__main__":
    try:
        if os.name == "nt":
            import ctypes
            os.system("title nova-tool v1.0")
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        else:
            sys.stdout.write("\x1b]2;nova-tool v1.0\x07")
        boot()
        home()
    except KeyboardInterrupt:
        console.print(f"\n[{C_NEON} bold]  interrupted.")
        sys.exit(0)
