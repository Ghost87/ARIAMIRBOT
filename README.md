# ARIAMIR Orders | آریامیر · ثبت سفارش 🛍 🔐

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3ECF8E?logo=python&logoColor=white)](https://python.org)
[![aiogram 3](https://img.shields.io/badge/aiogram-3.x-2AABEE?logo=telegram&logoColor=white)](https://docs.aiogram.dev)
[![Source: Encrypted](https://img.shields.io/badge/Source-AES--256%20Encrypted-blueviolet?logo=lock)](src.enc)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🇮🇷 ربات ثبت سفارش و پرداخت خدمات دیجیتال — **سورس این ریپو به‌صورت عمدی رمزنگاری شده (AES‑256)** تا
> هویت و منطق پروژه عمومی نباشد؛ اجرا فقط با کلید رمزگشایی ممکن است.
> 🇬🇧 Telegram order & payment bot — **source is intentionally AES‑256 encrypted**; it only runs with the decryption key.

## 🔐 چرا سورس رمزشده؟

این ریپو **public** است تا اجرای GitHub Actions رایگان و نامحدود باشد ✨ — و چون public است،
کل سورس در فایل `src.enc` با **AES‑256‑CBC + PBKDF2** رمز شده. برای اجرا به سکرت
`DECRYPT_KEY` نیاز است؛ بدون آن، هیچ‌کس به سورس و اطلاعات پروژه دسترسی ندارد.

## 🚀 اجرای رایگان (مثل بقیه ربات‌ها)

۱. سکرت‌ها را بساز: **Settings → Secrets and variables → Actions → New repository secret**

| Name | Secret |
|---|---|
| `DECRYPT_KEY` | 🔑 رمز فایل‌ها (کلید رمزگشایی src.enc که به‌ت داده شده) |
| `BOT_TOKEN` | توکن ربات از @BotFather |
| `ADMIN_USERNAME` | یوزرنیم ورود به پنل `/admin` |
| `ADMIN_PASSWORD` | پسورد ورود به پنل |
| `ADMIN_USER_IDS` | آیدی عددی ادمین(ها) با کاما |
| `ADMIN_GROUP_ID` | آیدی گروه ادمین برای سفارش‌ها و فیش‌ها (`-100…`) |
| `GH_PAT` | _(اختیاری)_ توکن شخصی برای نمایش وضعیت Actions |

۲. **Actions → 🤖 Run ARIAMIR Orders → Run workflow** — تعداد دقیقه را بزن (۱ تا ۳۵۶) → ربات آنلاین می‌شود.
دیتابیس به‌صورت **رمزشده** در برنچ `db-backup` بین اجراها حفظ می‌شود؛ با Run جدید ادامه پیدا می‌کند.
(ورودی `wipe_db` برای شروع از صفر.)

## 🐕 نگهبان ۲۴ ساعته (۲۴/۷ — رایگان)

- **run-bot.yml** هر **۶ ساعت خودکار** (cron) بالا می‌آید و **۳۴۵ دقیقه** روشن می‌ماند؛ ران بعدی در صف
  می‌ایستد و درست وقتی قبلی تمام شد شروع می‌شود ⇒ پوشش شبانه‌روزی بدون تداخل پولینگ.
- **bot-watchdog.yml** هر **۳۰ دقیقه** چک می‌کند؛ اگر به هر دلیلی ربات پایین بود، خودکار دیسپچ تازه می‌زند.
- **خاموش کامل:** ورک‌فلوی 🐕 را Disable کن + ران جاری را Cancel — برای روشن‌شدن دوباره، برعکس.

## 💻 رمزگشایی و اجرای لوکال / VPS

```bash
git clone https://github.com/Ghost87/ARIAMIRBOT.git && cd ARIAMIRBOT
DECRYPT_KEY='رمز فایل‌ها' ./decrypt.sh           # خروجی: ./decrypted
cd decrypted
python3 -m venv venv && source venv/bin/activate
pip install -r ../requirements.txt
cp ../.env.example .env   # سپس .env را پر کنید
python -u bot.py
```
یا مستقیم با بوت‌لودر: `DECRYPT_KEY=... python -u run_encrypted.py` (بدون باقی‌گذاشتن سورس روی دیسک).

## ⚙️ ساختار | Structure

```
├── src.enc                     # 🔐 سورس کامل پروژه — AES-256 (handlers/services/keyboards/config/docs/deploy)
├── run_encrypted.py            # بوت‌لودر: رمزگشایی در حافظه موقت + اجرای bot.py + پاک‌سازی
├── decrypt.sh                  # رمزگشایی محلی → ./decrypted
├── requirements.txt            # وابستگی‌ها (بدون راز)
├── .env.example                # قالب تنظیمات (بدون راز)
├── .github/workflows/run-bot.yml  # اجرای رایگان: minutes تا ۶ ساعت + بکاپ رمزشده دیتابیس
└── LICENSE                     # MIT — ARIAMIR
```

## ✨ امکانات (خلاصه)

ثبت سفارش برای ۹ سرویس با فرم داینامیک • پنل ادمین کامل (آمار/سفارش/سرویس/کاربر/برودکست/کانال جوین/متن‌ها)
• 💳 پرداخت کارت‌به‌کارت + فیش در گروه ادمین + تأیید/رد • 📦 تحویل فایل پروژه با قانون
«رمز فایل فقط بعد از تأیید پرداخت» • 📋 وضعیت سفارش‌ها و پرداخت هر کاربر در پنل • 🔔 نوتیف خودکار مشتری.

---

<div align="center">

**ARIAMIR** — One brand. The whole world. ✦
[@ARIAMIR_IR](https://t.me/ARIAMIR_IR) • [t.me/Ariamir_academy](https://t.me/Ariamir_academy) • [ariamir.ir](https://ariamir.ir)
«با اطمینان بساز؛ اعتماد در هر لایه.»
</div>
