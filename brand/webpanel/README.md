# 🌐 پنل وب ARIAMIR — بسته‌ی آیکون SVG + هدایت PHP

پنل وب PHP روی `ariamir.gt.tc` اجرا می‌شود. این پوشه ابزارهای لازم برای یکپارچه‌کردن **آیکون‌های برند ARIAMIR** در آن پنل را دارد.

## 📁 محتویات

| فایل | توضیح |
|---|---|
| `assets/*.svg` | **۷۹ آیکون وکتوری برند** (گرادیان). هم‌نام با کلیدهای `ICON_IDS` دو ربات. |
| `ariamir_icons.php` | **تابع کمکی PHP** برای درج آیکون‌ها به‌صورت inline SVG در پنل. |

## 🚀 راه‌اندازی

1. پوشه‌ی `assets/` و فایل `ariamir_icons.php` را داخل پنل (مثلاً `panel/`) کپی کن.
2. در هر صفحه که می‌خواهی آیکون باشد:
   ```php
   <?php require __DIR__ . '/ariamir_icons.php'; ?>

   <!-- آیکون سفارش‌ها با ۲۴ پیکسل -->
   <span class="icon"><?= ariamir_icon('orders', 24) ?></span>
   <span class="icon"><?= ariamir_icon('robot', 20) ?></span>
   ```
3. اگر خواستی نگاشت دکمه‌های ربات را هم در پنل بازسازی کنی:
   ```php
   $map = ariamir_icon_map();          // ['home'=>'home', 'orders'=>'orders', ...]
   echo ariamir_icon($map['orders'], 22);
   ```

## 🎨 نمونه

| کلید | فایل | نمونه |
|---|---|---|
| `home` | `home.svg` | 🏠 |
| `orders` | `orders.svg` | 📋 |
| `robot` | `robot.svg` | 🤖 |
| `star` | `star.svg` | ⭐ |
| `shield` | `shield.svg` | 🛡 |

## ⚠️ نکته
این آیکون‌ها برای **سمت وب/پنل/برندینگ** هستند. برای **دکمه‌های داخل چت تلگرام** که SVG را رندر نمی‌کنند، از **پک custom emoji** (فایل `ariamir_custom_emoji_pack.zip` و راهنمای `emoji_guide.html`) استفاده کن.
