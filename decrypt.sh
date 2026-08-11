#!/bin/bash
# رمزگشایی محلی سورس — خروجی در پوشهٔ decrypted/
# استفاده:  SRC_KEY=رمز ./decrypt.sh      یا      ./decrypt.sh رمز
set -e
KEY="${SRC_KEY:-$1}"
if [ -z "$KEY" ]; then
  echo "❌ رمز را بده: SRC_KEY=رمز ./decrypt.sh   یا   ./decrypt.sh رمز"
  exit 1
fi
mkdir -p decrypted
openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 -in src.enc -pass "pass:$KEY" | tar -xz -C decrypted
echo "✅ سورس در ./decrypted رمزگشایی شد"
echo "   اجرای لوکال:  cd decrypted && cp ../.env.example .env  # بعد .env را پر کن"
