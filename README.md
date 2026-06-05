# معرفی پروژه

این پروژه یک MVP برای دستیار هوشمند پشتیبانی راستاد است که با استفاده از هوش مصنوعی، پیام کاربران را دریافت کرده، نوع درخواست آن‌ها را تشخیص می‌دهد، اطلاعات مرتبط را از پایگاه دانش داخلی استخراج می‌کند و پاسخ مناسبی تولید می‌نماید.

هدف اصلی این پروژه، نمایش توانایی طراحی و پیاده‌سازی یک سیستم AI-Driven شامل Backend، مدیریت داده، بازیابی دانش (RAG) و اتوماسیون پاسخگویی است.

---

# روش اجرای پروژه

برای اجرای پروژه با استفاده از Docker Compose:

```bash
sudo docker compose up -d --build
```

این دستور تمام سرویس‌های Backend و Assistant را به همراه وابستگی‌ها ساخته و به صورت همزمان اجرا می‌کند.

---

# تنظیمات محیطی (Environment Variables)

## Backend

```env
ASSISTANT_URL=...
DATABASE_URL=...
```

## Assistant Service

```env
LLM_MODEL=...
EMBEDDING_MODEL=...
OPENROUTER_API_KEY=...
QDRANT_COLLECTION=...
```

---

# معماری سیستم

پروژه از دو سرویس مستقل تشکیل شده است:

## Backend Service

- ارائه API
- اعتبارسنجی درخواست‌ها
- مدیریت کاربران
- ذخیره‌سازی اطلاعات
- ارتباط با سرویس Assistant

---

## Assistant Service

- تشخیص Intent
- تشخیص Segment کاربر
- بازیابی اطلاعات از Knowledge Base
- تولید پاسخ
- تشخیص نیاز به پشتیبانی انسانی
- پیاده‌سازی با LangGraph Workflow

---

# ارتباط بین سرویس‌ها

سرویس Backend برای تولید پاسخ، درخواست کاربر را به سرویس Assistant ارسال می‌کند:

- Endpoint: `/api/ask`
- Payload:
  - user_id
  - message

- Response:
  - reply
  - intent
  - user_segment
  - needs_human_support

---

# تکنولوژی‌های استفاده شده

## Backend
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL

## لایه هوش مصنوعی
- LangGraph
- OpenRouter / Ollama
- Qdrant Vector Database

## زیرساخت
- Docker
- Docker Compose

---

# مستندات API

پس از اجرای پروژه:

http://localhost:9000/docs

---

# پایگاه دانش (Knowledge Base)

knowledge_base/

  rastad_services.txt

  vip_products.txt

  exchange_signup.txt

  kol_program.txt

در زمان دریافت درخواست، اطلاعات مرتبط از Qdrant بازیابی شده و برای تولید پاسخ نهایی به مدل زبانی ارسال می‌شوند.

---

# مدیریت خطا

- خالی بودن user_id
- خالی بودن پیام
- عدم وجود کاربر
- خطاهای ارتباطی با سرویس Assistant

---

# استفاده از LLM و قابلیت جایگزینی مدل‌ها

## حالت اجرای فعلی (Local LLM)

در حالت توسعه، از Ollama برای اجرای مدل به صورت لوکال استفاده شده است تا سیستم بدون نیاز به API خارجی قابل اجرا باشد.

---

## حالت Production (Cloud LLM)

معماری سیستم به‌گونه‌ای طراحی شده که به راحتی می‌توان آن را به سرویس‌های زیر متصل کرد:

- OpenAI
- Claude (Anthropic)
- OpenRouter
- Gemini
- یا هر مدل سازگار دیگر

---

# جداسازی سرویس‌ها

پروژه به صورت کاملاً ماژولار و دو سرویس مستقل طراحی شده است.

---

# مزیت معماری

- امکان تغییر LLM بدون تغییر در منطق کسب‌وکار
- توسعه مستقل Backend و AI Layer
- آماده برای مقیاس‌پذیری افقی
- مناسب برای اتصال به CRM یا Telegram Bot

---

# مثال‌ها (Assistant Service)
<img width="1280" height="668" alt="image" src="https://github.com/user-attachments/assets/43f5a60b-bafb-4800-8c8d-f0b4dc623ca3" />
<img width="1280" height="668" alt="image" src="https://github.com/user-attachments/assets/8db90e59-2867-418e-99a7-f0f1ef8f8023" />
<img width="1280" height="668" alt="image" src="https://github.com/user-attachments/assets/91d3f474-7e9f-46cf-ae5d-64f4332d6b25" />
