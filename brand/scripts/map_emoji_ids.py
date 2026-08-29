#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 ARIAMIR — Map custom_emoji_id (getStickerSet helper)
========================================================
بعد از اینکه پک ایموجی اختصاصی را در @Stickers ساختی، این اسکریپت با
«نام پک» و «توکن ربات» کدهای ID هر ایموجی را از تلگرام می‌گیرد و به‌صورت
«icon_key=integer_id» خروجی می‌دهد — آماده برای ساختن `ICON_IDS`.

پیش‌نیاز:
  1) پک را در @Stickers با دستور /newemoji ساختی و /publish کردی.
  2) فایل‌های PNG را دقیقاً به‌ترتیبِ «brand/upload_order.txt» آپلود کردی
     (این باعث می‌شود ترتیب داخل پک با ترتیب آیکون‌ها یکی باشد).
  3) توکن ربات و نام پک را داری.

استفاده:
  TELEGRAM_BOT_TOKEN="123:ABC" EMOJI_SET_NAME="ariamir_ui_v4" \
    python3 brand/scripts/map_emoji_ids.py

خروجی:  home=5368123456  orders=5368998877  ...  (برای build_icon_ids.py)
"""
import os, json, sys, urllib.request

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
SET = os.environ.get("EMOJI_SET_NAME", "").strip()
ORDER_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "upload_order.txt")


def api(method, **params):
    url = f"https://api.telegram.org/bot{TOKEN}/{method}"
    q = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
    with urllib.request.urlopen(url + ("?" + q if q else "")) as r:
        data = json.loads(r.read().decode())
    if not data.get("ok"):
        raise RuntimeError(data.get("description", "خطای API تلگرام"))
    return data["result"]


def load_order():
    with open(ORDER_FILE, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]


def main():
    if not TOKEN or not SET:
        print("❌ TELEGRAM_BOT_TOKEN یا EMOJI_SET_NAME تنظیم نشده!")
        print("   مثل:  TELEGRAM_BOT_TOKEN=123:ABC EMOJI_SET_NAME=ariamir_ui_v4 python3 ...")
        return 1
    try:
        res = api("getStickerSet", name=SET)
    except Exception as e:
        print(f"❌ getStickerSet ناموفق: {e}")
        print("   چک کن: نام پک درست باشد؟ توکن درست باشد؟")
        return 1
    stickers = res.get("stickers", [])
    names = load_order()
    print(f"📦 پک «{res.get('title', SET)}» — {len(stickers)} ایموجی")
    print("━" * 46)
    pairs = []
    for i, st in enumerate(stickers):
        eid = st.get("custom_emoji_id")
        emoji = st.get("emoji")
        name = names[i] if i < len(names) else f"key{i}"
        pairs.append(f"{name}={eid}")
        print(f"{i+1:2}. {name:12}  {emoji or '':2}  →  {eid}")
    print("━" * 46)
    if len(stickers) != len(names):
        print(f"⚠️ تعداد ایموجی ({len(stickers)}) با ترتیب آیکون‌ها ({len(names)}) یکی نیست.")
        print("   حتماً به همان ترتیب upload_order.txt آپلود کن، یا خروجی را دستی مرتب کن.")
    print("\nیک‌خطی برای build_icon_ids.py:")
    print("  " + " ".join(pairs))
    return 0 if len(stickers) == len(names) else 2


if __name__ == "__main__":
    sys.exit(main())
