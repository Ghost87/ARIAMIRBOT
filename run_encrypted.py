# -*- coding: utf-8 -*-
# ─── توسعه: ARIAMIR ─ تلگرام: @ARIAMIR_IR ─ https://t.me/Ariamir_academy ───
"""بوت‌لودر اجرای رمزنگاری‌شده.

سورس واقعی پروژه داخل src.enc (AES-256) است. این فایل آن را با متغیر
محیطی DECRYPT_KEY رمزگشایی می‌کند، سپس bot.py را اجرا می‌کند.
دیتابیس خارج از پوشهٔ موقت نگه‌داری می‌شود تا قابل بکاپ باشد؛
پوشهٔ موقت سورس در پایان کار کاملاً پاک می‌شود.
"""
import os
import pathlib
import shutil
import signal
import subprocess
import sys
import tempfile

BASE = pathlib.Path(__file__).resolve().parent
ENC = BASE / "src.enc"


def main() -> int:
    key = os.environ.get("DECRYPT_KEY", "").strip()
    if not key:
        print("❌ DECRYPT_KEY تنظیم نشده! در GitHub: Settings → Secrets and variables → Actions")
        return 1
    if not ENC.exists():
        print("❌ src.enc پیدا نشد! کنار run_encrypted.py باید باشد.")
        return 1

    tmp_path = pathlib.Path(tempfile.mkdtemp(prefix="ariamir_orders_"))
    tgz = tmp_path / "src.tgz"
    try:
        data_dir = BASE / "data"
        data_dir.mkdir(exist_ok=True)  # دیتابیس بیرون از حذافه — برای بکاپ ورک‌فلو
        r = subprocess.run(
            ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-md", "sha256",
             "-in", str(ENC), "-out", str(tgz), "-pass", "env:DECRYPT_KEY"],
        )
        if r.returncode != 0:
            print("❌ رمزگشایی ناموفق — DECRYPT_KEY اشتباه است؟")
            return 1
        src = tmp_path / "src"
        src.mkdir()
        subprocess.run(["tar", "-xzf", str(tgz), "-C", str(src)], check=True)
        tgz.unlink(missing_ok=True)
        os.symlink(str(data_dir), str(src / "data"))

        proc = subprocess.Popen([sys.executable, "-u", "bot.py"],
                                cwd=src, env=os.environ.copy())

        def _forward(sig, frame):
            try:
                proc.terminate()
            except Exception:
                pass

        signal.signal(signal.SIGTERM, _forward)
        signal.signal(signal.SIGINT, _forward)
        return proc.wait()
    finally:
        shutil.rmtree(tmp_path, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
