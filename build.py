#!/usr/bin/env python3
"""從 ad-agency-brain 的 sales kit 複製合作方案文件，改成英文檔名並加上不收錄設定。

夥伴看的（總覽頁、夥伴對齊，含分潤）留在本倉庫；
客戶會看到的三份文件放到 ../ad-onboarding，兩邊網址分開。
"""
import pathlib

來源 = pathlib.Path.home() / "Desktop/vibe-coding playground/ad-agency-brain/sales kit"
這裡 = pathlib.Path(__file__).parent
客戶站 = 這裡.parent / "ad-onboarding"
客戶站網址 = "https://liiiiwei.github.io/ad-onboarding/"
前綴, 後綴 = "立崴_短影音廣告合作方案_", "_2026-10-03"
夥伴文件 = {
    "總覽頁.html": "index.html",
    "夥伴對齊.html": "partner.html",
}
客戶文件 = {
    "客戶資料表.html": "client-form.html",
    "腳本檢查表.html": "script-checklist.html",
    "常見問答.html": "faq.html",
}

def 原檔名(名稱):
    主檔, 副檔 = 名稱.rsplit(".", 1)
    return f"{前綴}{主檔}{後綴}.{副檔}"

def 產生(對照, 目的地, 是客戶站):
    for 名稱, 新名 in 對照.items():
        內容 = (來源 / 原檔名(名稱)).read_text(encoding="utf-8")
        for 名稱2, 新名2 in 客戶文件.items():
            內容 = 內容.replace(原檔名(名稱2), 新名2 if 是客戶站 else 客戶站網址 + 新名2)
        for 名稱2, 新名2 in 夥伴文件.items():
            # 客戶站不得連回夥伴文件
            assert not (是客戶站 and 原檔名(名稱2) in 內容), 名稱
            內容 = 內容.replace(原檔名(名稱2), 新名2)
        assert "<head>" in 內容, 名稱
        內容 = 內容.replace("<head>", '<head>\n    <meta name="robots" content="noindex, nofollow" />', 1)
        assert 前綴 not in 內容, 名稱
        if 是客戶站:
            for 詞 in ("分潤", "介紹費", "夥伴"):
                assert 詞 not in 內容, (名稱, 詞)
        (目的地 / 新名).write_text(內容, encoding="utf-8")
        print("已產生", 目的地.name + "/" + 新名)

產生(夥伴文件, 這裡, False)
產生(客戶文件, 客戶站, True)
