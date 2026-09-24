# Crypt & Decrypt with AES 🔐

أداة بسيطة تعمل من الـ Terminal (CLI) لتشفير وفك تشفير النصوص باستخدام مكتبة `cryptography` في Python، عبر خوارزمية **Fernet** (وهي بروتوكول تشفير متماثل symmetric encryption مبني على AES في وضع CBC مع HMAC للتحقق من سلامة البيانات integrity).

## ✨ المميزات

- تشفير encrypt أي نص يدخله المستخدم.
- فك تشفير decrypt نص مشفّر باستخدام الـ key الصحيح.
- توليد key عشوائي آمن تلقائيًا عند كل عملية تشفير.
- خيار لعرض الـ key بعد التشفير أو إخفائه.
- التعامل الصحيح مع الأخطاء الشائعة (bytes/str encoding, invalid token).

## 🛠️ المتطلبات

- Python 3.7 أو أحدث
- مكتبة `cryptography`

### تثبيت المكتبة

```
pip install cryptography
```

## 🚀 طريقة الاستخدام

1. شغّل السكربت:

```
python AES.py
```

2. اختر العملية:
   - اكتب `e` للتشفير (encrypt)
   - اكتب `d` لفك التشفير (decrypt)

### مثال تشفير (Encrypt)

```
do to want to decrypt 'd' or encrypt 'e' e
enter the text to encrypt it: Hello World
this is the cipher text:>> gAAAAABq...
do you want the key: y or n: y
xAbvMPt1nFg10f-DztKEMPPITppIP6GdNEDwFYtLel...
```

⚠️ **مهم:** احتفظ بالـ key في مكان آمن — بدونه لن تستطيع فك تشفير النص أبدًا.

### مثال فك التشفير (Decrypt)

```
do to want to decrypt 'd' or encrypt 'e' d
enter the cipher text:>> gAAAAABq...
enter the key: xAbvMPt1nFg10f-DztKEMPPITppIP6GdNEDwFYtLel...
the text is :>> Hello World
```

## 🐞 مشاكل شائعة تم حلها أثناء التطوير

| المشكلة | السبب | الحل |
| --- | --- | --- |
| `InvalidSignature` / `InvalidToken` | استخدام key مختلف عن اللي اتشفر بيه النص الأصلي | إعادة إنشاء `cipher_suite = Fernet(key.encode())` بالـ key الجديد المُدخل من المستخدم |
| `TypeError: token must be bytes or str` | نسيان `()` بعد `.encode` | التأكد من استدعاء الدالة بشكل صحيح: `.encode()` |
| `TypeError` عند طباعة cipher_text | محاولة دمج `bytes` مع `str` مباشرة | استخدام `.decode()` قبل الطباعة |

## 🔒 ملاحظة أمنية

هذا المشروع لأغراض تعليمية بشكل أساسي. الـ key يظهر ويُدخل كنص عادي في الـ Terminal، وهو غير مناسب للاستخدام الإنتاجي production بدون تأمين إضافي (مثل تخزين الـ key في متغير بيئة environment variable أو Vault).

## 📜 الترخيص

MIT License
