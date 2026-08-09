# ARIAMIRBOT — ARIAMIR OS v4.0

ربات ثبت سفارش و پرداخت خدمات دیجیتال — آریامیر
**ARIAMIR Orders Bot · order intake, payment & secure file delivery**

- **Framework:** aiogram 3.30, SQLite, Python 3.11+
- **Version:** 4.0.0 — ساده، تمیز، بدون دکمه تکراری
- **Branch:**
  - `main` → سورس رمز شده `src.enc` (همین برنچ)
  - `db-backup` → دیتا و پل پنل `panel/snapshot.json.enc`

## چرا فقط `src.enc` می‌بینی؟

سورس به عمد رمز شده‌ست — ریپو پابلیکه ولی کد داخل `src.enc` هست.

این طراحی از روز اول همین بوده (طبق `ARIAMIR-PROMPT.md`):

> Repo `Ghost87/ARIAMIRBOT` (public). Branch `main` = code, contains ONLY `src.enc`

### دیکریپت لوکال

```bash
DK="Amir_seyedi_1387"  # کلید از ARIAMIR-SECRETS.md
openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 -in src.enc -pass "pass:$DK" | tar -xz -C /tmp/dec
ls /tmp/dec
# bot.py config.py texts.py handlers/ keyboards/ services/ states/ assets/
```

## v4.0 چی داره؟

- ۶ قدم سفارش به جای ۹، متن طبیعی و دوستانه
- ۳ ورودی اصلی: 🚀 ثبت پروژه / 📦 سفارش‌هام / 💬 حرف بزنیم
- آیکون custom emoji از پک Topics (بدون نیاز پرمیوم)
- کاتالوگ گرید ۲ ستونه، بدون تکرار
- متصل به سایت ariamir.gt.tc via WP Plugin + Mini App

## نصب سریع (VPS)

```bash
unzip ariamir-orders-v4-vps.zip
cp .env.example .env
nano .env  # BOT_TOKEN
./install.sh
# یا
docker-compose up -d --build
```

باندل‌ها توی گروه سورس: #234-236 + گروه Arsourcer

## پنل

پنل جدید ۷ بخشه (قبل ۱۲):
📊 داشبورد / 📦 سفارش‌ها / 🧩 کاتالوگ / 👥 مخاطبان / 📝 محتوا / 💳 مالی / ⚙️ سیستم

> One Place Rule — هر تنظیم فقط یه جا

پیش‌نمایش: `ariamir-v4/panel/index.html`

## اتصال سایت و ربات

- WP Plugin: `bridge/wordpress-plugin.php` → `[ariamir_cta]`
- API: `panel/api.php` با HMAC
- Mini App: `bridge/miniapp.html`

---

ساخته شده با 💚 توسط @ARIAMIR_IR — با اطمینان بساز؛ اعتماد در هر لایه.
