#!/usr/bin/env python3
"""從 ad-agency-brain 的 sales kit 複製合作方案文件，改成英文檔名並加上不收錄設定。"""
import pathlib, shutil

來源 = pathlib.Path.home() / "Desktop/vibe-coding playground/ad-agency-brain/sales kit"
這裡 = pathlib.Path(__file__).parent
前綴, 後綴 = "立崴_短影音廣告合作方案_", "_2026-10-03"
對照 = {
    "總覽頁.html": "index.html",
    "夥伴對齊.html": "partner.html",
    "客戶資料表.html": "client-form.html",
    "腳本檢查表.html": "script-checklist.html",
    "常見問答.html": "faq.html",
}

def 原檔名(名稱):
    主檔, 副檔 = 名稱.rsplit(".", 1)
    return f"{前綴}{主檔}{後綴}.{副檔}"

for 名稱, 新名 in 對照.items():
    原 = 來源 / 原檔名(名稱)
    if not 新名.endswith(".html"):
        shutil.copyfile(原, 這裡 / 新名)
        continue
    內容 = 原.read_text(encoding="utf-8")
    for 名稱2, 新名2 in 對照.items():
        內容 = 內容.replace(原檔名(名稱2), 新名2)
    assert "<head>" in 內容, 名稱
    內容 = 內容.replace("<head>", '<head>\n    <meta name="robots" content="noindex, nofollow" />', 1)
    assert 前綴 not in 內容, 名稱
    (這裡 / 新名).write_text(內容, encoding="utf-8")
    print("已產生", 新名)
