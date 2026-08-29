# 🎨 ARIAMIR — برند & آیکون‌ها (Brand & Icons)

ست کامل **آیکون‌های وکتوری برند ARIAMIR** — هماهنگ با کلیدهای دکمه‌های ربات (`ICON_IDS`).
همه‌ی این فایل‌ها **داخل همین ریپو** هستند و از گیت‌هاب قابل استفاده/دانلودند.

---

## 📁 ساختار پوشه

| مسیر | توضیح |
|---|---|
| `icons/` | **۷۹ فایل SVG** وکتوری برند با گرادیان — برای وب‌سایت / پنل وب / پرزنت / بنر |
| `emoji_pack/` | **۷۹ PNG شفاف ۵۱۲×۵۱۲** — قالبِ «ایموجی اختصاصی تلگرام» برای دکمه‌های **داخل چت** |
| `webpanel/ariamir_icons.php` | تابع کمکی PHP برای درج آیکون‌های SVG در پنل وب |
| `webpanel/README.md` | راهنمای راه‌اندازی پنل وب |
| `emoji_guide.html` | راهنمای گام‌به‌گام آپلود پک ایموجی از @BotFather |
| `scripts/build_icon_ids.py` | اسکریپت خودکار برای به‌روزرسانی `ICON_IDS` در `src.enc` |

---

## ⚠️ نکته‌ی مهم (محدودیت واقعی تلگرام)

**دکمه‌های تلگرام (inline keyboard) SVG را رندر نمی‌کنند** — فقط **ایموجی** یا **custom emoji** را نشان می‌دهند.
پس:
- **برای وب / پنل / برندینگ** ← از `icons/*.svg` استفاده کن. ✅
- **برای دکمه‌های داخل چت** ← از `emoji_pack/*.png` (با آپلود از @BotFather) استفاده کن. ✅

---

## 🔌 اتصال به دکمه‌های ربات (داخل چت)

کد ربات آیکون‌ها را از دیکشنری `ICON_IDS` در `config.py` می‌خواند (فایل در `src.enc` رمز است).
هر ایموجی در پک تلگرام یک **ID عددی** دارد. برای جایگزینی:

1. در تلگرام به **@BotFather** برو → `/newemojipack` → عنوان/نام بده.
2. هر `emoji_pack/X.png` را به‌همراه یک ایموجی متناظر آپلود کن (دستور `/addemoji`).
3. کدهای ID که BotFather می‌دهد را جمع کن.
4. از این دستور (از پوشه‌ی ریشه‌ی ریپو) استفاده کن — `config.py` داخل `src.enc` را خودکار به‌روزرسانی و برای پوش آماده می‌کند:
   ```bash
   SRC_KEY="رمز_SRC_KEY" \
   python3 brand/scripts/build_icon_ids.py \
     home=5368123456 orders=5368998877 robot=5368112233 ...
   ```
5. سپس:
   ```bash
   cp src_new.enc src.enc
   git add src.enc
   git commit -m "🎨 به‌روزرسانی ICON_IDS به پک ایموجی جدید"
   git push origin main
   ```

> 💡 فقط ایموجی‌هایی که کدشان را بدهی عوض می‌شوند؛ بقیه دست‌نخورده می‌مانند (پک قدیمی).

---

## 🖼 استفاده در وب/پنل PHP

```php
<?php require 'brand/webpanel/ariamir_icons.php'; ?>
<!-- آیکون سفارش‌ها ۲۴ پیکسل -->
<span class="icon"><?= ariamir_icon('orders', 24) ?></span>
<span class="icon"><?= ariamir_icon('robot', 20) ?></span>
```
جزئیات بیشتر در `webpanel/README.md`.

---

## 🎨 پالت برند
گرادیان: `#6366f1` (indigo) → `#8b5cf6` (violet) → `#d946ef` (fuchsia) · پس‌زمینه/متن: `#0f172a` / `#e5e7eb`.

**ARIAMIR · One brand. The whole world. ✦**
