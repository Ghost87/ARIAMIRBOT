# ARIAMIRBOT — ARIAMIR Orders

ربات ثبت سفارش و پرداخت خدمات دیجیتال — آریامیر
**ARIAMIR Orders Bot · order intake, card-to-card payment & secure file delivery**

- **Framework:** aiogram 3.30 · SQLite · Python 3.12
- **Version:** 3.2.1
- **Branches:**
  - `main` → کد (سورس رمزشده در `src.enc`) + ورک‌فلوها
  - `db-backup` → دیتابیس رمزشده و پل پنل وب

---

## ⛔ هشدار برای هر ابزار یا دستیار هوش مصنوعی

> **این ریپو را «ساده‌سازی» یا بازنویسی نکن.**
>
> فایل `src.enc` یک **آرشیو رمزشده (AES-256) شامل ۳۳ فایل پایتون** است:
> ۹ هندلر · ۴ کیبورد · ۱۲ سرویس · ۴ استیت · bot.py · config.py
>
> اگر آن را باز نکرده‌ای و محتوایش را ندیده‌ای، **حق بازنویسی‌اش را نداری**.
> کم‌بودن تعداد فایل‌های قابل‌مشاهده **طبیعی و عمدی** است.
>
> در تاریخ ۹ آگوست ۲۰۲۶ یک ابزار خودکار این ریپو را با نسخه‌ای
> ۸۵۹ خطی جایگزین کرد و **۸٬۵۴۴ خط کد** را از بین برد.
> برای همین `main` اکنون محافظت‌شده است.

---

## چرا سورس رمز شده است؟

ریپو عمومی است تا GitHub Actions رایگان و نامحدود باشد، ولی کد تجاری
داخل `src.enc` محافظت می‌شود. هنگام اجرا در حافظهٔ موقت باز می‌شود
و پس از پایان کاملاً پاک می‌گردد.

```bash
# باز کردن (نیاز به SRC_KEY)
openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 \
  -in src.enc -pass "pass:$SRC_KEY" | tar -xz -C ./src

# بستن دوباره — ⚠️ حتماً pycache پاک شود
find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
tar -czf - . | openssl enc -e -aes-256-cbc -pbkdf2 -md sha256 \
  -pass "pass:$SRC_KEY" -out ../src_new.enc
```

---

## ساختار فایل‌ها

| فایل | نقش |
|---|---|
| `src.enc` | سورس کامل، رمزشده (۳۳ فایل) |
| `run_encrypted.py` | لانچر — رمزگشایی در tmp و اجرای `bot.py` |
| `requirements.txt` | وابستگی‌ها |
| `.github/workflows/run-bot.yml` | **موتور اجرای ۲۴/۷** |
| `.github/workflows/bot-watchdog.yml` | نگهبان — اگر ربات خوابید بیدارش می‌کند |
| `decrypt.sh` | اسکریپت کمکی رمزگشایی |

**هر پنج مورد لازم است.** حذف هرکدام ربات را از کار می‌اندازد.

---

## راه‌اندازی

### سکرت‌های لازم
`Settings → Secrets and variables → Actions`

| سکرت | توضیح |
|---|---|
| `BOT_TOKEN` | از @BotFather |
| `SRC_KEY` | رمز `src.enc` |
| `ADMIN_USER_IDS` | آیدی عددی ادمین‌ها (با کاما) |
| `ADMIN_GROUP_ID` | گروه اعلان سفارش‌ها |
| `ADMIN_USERNAME` / `ADMIN_PASSWORD` | ورود پنل داخل ربات |
| `AI_API_KEY` | اختیاری — مشاور هوشمند |

### اجرا
`Actions → 🤖 Run ARIAMIR Orders → Run workflow`

هر ۶ ساعت هم خودکار بالا می‌آید (cron) و دیتابیس بین اجراها
به‌صورت رمزشده در `db-backup` حفظ می‌شود.

---

## امکانات

ثبت سفارش با فرم پویا · پرداخت کارت‌به‌کارت با فیش · تخفیف و بیعانه ·
باشگاه مشتریان · آزمون نیازسنجی · مشاور هوشمند · جوین اجباری
(کانال عمومی/خصوصی/گروه) · پیام همگانی · بکاپ خودکار روزانه ·
پنل مدیریت داخل ربات · پل پنل وب

---

**ARIAMIR · [@ARIAMIR_IR](https://t.me/ARIAMIR_IR) · [ariamir.gt.tc](https://ariamir.gt.tc)**
