#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 ARIAMIR — Build ICON_IDS (custom emoji) generator
=====================================================
وقتی در @BotFather پک ایموجی اختصاصی ساختی، برای هر ایموجی یک «کد عددی ID»
می‌گیری (مثلاً 5368...). این اسکریپت آن کدها را می‌گیرد و:
  ۱) بلوک جدید `ICON_IDS` را می‌سازد (همهٔ کلیدهای فعلی + مقادیر جدید).
  ۲) فایل `config.py` را در `src.enc` با همان `SRC_KEY` به‌روزرسانی می‌کند
     (رمزگشایی → جایگزینی بلوک → رمز مجدد → پوش‌کردن به گیت‌هاب).

استفاده (از پوشهٔ ریشهٔ ریپو):
    SRC_KEY="رمز" python3 brand/scripts/build_icon_ids.py home=5368123456 orders=5368998877 ...

کلیدهایی که مقدار ندهید، با مقدار فعلی (پک قدیمی) می‌مانند؛ یعنی فقط
ایموجی‌هایی که خواسته‌اید را عوض می‌کند و بقیه را دست نمی‌زند.
"""
import os, re, subprocess, sys, tempfile, shutil

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ENC = os.path.join(REPO, "src.enc")


def parse_pairs():
    out = {}
    for a in sys.argv[1:]:
        if "=" in a and not a.endswith("="):
            k, v = a.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def main():
    key = os.environ.get("SRC_KEY", "").strip()
    if not key:
        print("❌ SRC_KEY ست نشده!  مثل:  SRC_KEY=رمز python3 brand/scripts/build_icon_ids.py ...")
        return 1
    pairs = parse_pairs()
    if not pairs:
        print("ℹ️ هیچ کدی داده نشدی. مثال: home=5368123456 orders=5368998877")
        return 1

    # ۱) رمزگشایی
    tmp = tempfile.mkdtemp(prefix="ariamir_icon_")
    try:
        tgz = os.path.join(tmp, "src.tgz")
        r = subprocess.run(["openssl","enc","-d","-aes-256-cbc","-pbkdf2","-md","sha256",
                            "-in",ENC,"-out",tgz,"-pass",f"pass:{key}"], capture_output=True)
        if r.returncode != 0:
            print("❌ رمزگشایی ناموفق — SRC_KEY درست است؟")
            return 1
        src = os.path.join(tmp, "src")
        os.makedirs(src, exist_ok=True)
        subprocess.run(["tar","-xzf",tgz,"-C",src], check=True)
        cfg = os.path.join(src, "config.py")
        data = open(cfg, encoding="utf-8").read()

        # به‌روزرسانی بلوک ICON_IDS
        m = re.search(r"(ICON_IDS: dict\[str, str\] = \{)(.*?)(\n\})", data, re.S)
        if not m:
            print("❌ بلوک ICON_IDS در config.py پیدا نشد")
            return 1
        block = m.group(2)
        new_block = block
        for k, v in pairs.items():
            # جایگزینی مقدار کلید در بلوک
            new_block = re.sub(rf'(?m)^(\s*"{k}":\s*")[^"]*(",)', rf'\g<1>{v}\g<2>', new_block)
        data = data[:m.start()] + m.group(1) + new_block + m.group(3) + data[m.end():]
        open(cfg, "w", encoding="utf-8").write(data)

        # پاک‌کردن pycache + رمز مجدد
        for _src in os.listdir(src):
            p = os.path.join(src, _src)
            if _src == "__pycache__":
                shutil.rmtree(p, ignore_errors=True)
        subprocess.run(["find", src, "-name", "__pycache__", "-type", "d", "-exec", "rm", "-rf", "{}", "+"], capture_output=True)
        out_enc = os.path.join(REPO, "src_new.enc")
        p1 = subprocess.run(["tar","-czf","-","-C",src,"."], capture_output=True)
        p2 = subprocess.run(["openssl","enc","-aes-256-cbc","-pbkdf2","-md","sha256",
                             "-pass",f"pass:{key}"], input=p1.stdout, capture_output=True)
        open(out_enc,"wb").write(p2.stdout)
        print(f"✅ src_new.enc ساخته شد — {len(pairs)} آیکون به‌روزرسانی شد.")
        print("   حالا:  cp src_new.enc src.enc  و  git add src.enc src_new.enc  (یا src_new را حذف کن)")
        print("   سپس:  git commit -m ...  و  git push origin main")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
