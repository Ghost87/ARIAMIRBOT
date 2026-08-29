<?php
/**
 * ARIAMIR — Icons helper (PHP)
 * -----------------------------------------------
 * درج آیکون‌های SVG برند ARIAMIR به‌صورت inline در پنل وب.
 *
 * مسیر آیکون‌ها:
 *   - به‌صورت پیش‌فرض از «../icons/» (نسبت به این فایل) خوانده می‌شود.
 *   - اگر پنل را جدا نصب کردید و آیکون‌ها را در «assets/» گذاشتید،
 *     متغیر $ARIAMIR_ICON_DIR را تنظیم کنید.
 *
 * کاربرد:
 *   <?php require 'brand/webpanel/ariamir_icons.php'; ?>
 *   echo ariamir_icon('orders', 24);
 */

if (!function_exists('ariamir_icon')) {
    /**
     * یک آیکون SVG برمی‌گرداند (inline) یا خالی در نبود فایل.
     */
    function ariamir_icon(string $name, int $size = 24): string {
        // پوشه‌های جستجو به‌ترتیب اولویت
        $dirs = [
            __DIR__ . '/assets',      // حالت نصب مستقل پنل
            dirname(__DIR__) . '/icons',  // حالت داخل brand/ ریپو
            dirname(__DIR__, 2) . '/icons',
        ];
        $file = '';
        foreach ($dirs as $d) {
            $cand = $d . '/' . basename($name) . '.svg';
            if (is_file($cand)) { $file = $cand; break; }
        }
        if (!$file) {
            return '';
        }
        $svg = file_get_contents($file);
        $svg = preg_replace('/\s*(aria-hidden|width|height)="[^"]*"/', '', $svg, 1);
        $svg = preg_replace('/<svg /', '<svg width="' . (int)$size . '" height="' . (int)$size . '" ', $svg, 1);
        return $svg;
    }
}

if (!function_exists('ariamir_icon_map')) {
    /**
     * نگاشت کلیدهای دکمه‌های ربات → نام فایل آیکون (برای بازسازی در پنل).
     */
    function ariamir_icon_map(): array {
        return [
            'home'=>'home','orders'=>'orders','robot'=>'robot','star'=>'star',
            'money'=>'money','shield'=>'shield','rocket'=>'rocket','zap'=>'zap',
            'handshake'=>'handshake','brain'=>'brain','crown'=>'crown','bag'=>'bag',
            'card'=>'card','check'=>'check','back'=>'back','cancel'=>'cancel',
            'users'=>'users','user'=>'user','ticket'=>'ticket','chart'=>'chart',
            'pencil'=>'pencil','mega'=>'mega','speaker'=>'speaker','floppy'=>'floppy',
            'door'=>'door','search'=>'search','plus'=>'plus','trash'=>'trash',
        ];
    }
}
