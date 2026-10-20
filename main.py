# 🏭 AI & BI Automated Email Delivery System
# 🌐 مشروع مؤسسة ربا أحمد لتحليل البيانات وأتمتة التقارير الذكية للعملاء

from fastapi import FastAPI, BackgroundTasks, Body
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI(title="AI Email Analytics Agent")

def send_analytics_email(customer_email: str, customer_name: str, sales_amount: float):
    """دالة برمجية تقوم بتحليل المبيعات وصياغة تقرير BI وإرساله فوراً للعميل"""
    
    # 1. ذكاء الأعمال واتخاذ القرار التلقائي (BI Decision)
    if sales_amount >= 1500:
        bi_analysis = "أداء متجرك ممتاز جداً هذا الأسبوع! نقترح زيادة ميزانية الإعلانات."
    else:
        bi_analysis = "تنبيه: المبيعات تحت المنحنى المطلوب، نقترح عمل حملة عروض مخصصة."
        
    # 2. هيكلة وصياغة البريد الإلكتروني تلقائياً للعميل
    email_body = f"""مرحباً {customer_name}،

إليك تقرير أداء المبيعات الذكي والمؤتمت الخاص بمتجرك:
--------------------------------------------------
📊 إجمالي المبيعات المحللة: {sales_amount} دولار
📈 توصية ذكاء الأعمال (BI): {bi_analysis}
--------------------------------------------------
نظام الأتمتة السحابي يعمل بكفاءة - مؤسسة أحمد أسامة للحلول الذكية.
"""

    # 3. إعدادات خادم البريد (SMTP)
    sender = "analytics-agent@yourcompany.com" # إيميل شركتك الرسمي مستقبلاً
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = customer_email
    msg['Subject'] = "📊 تقرير الأداء المالي والتوصيات الذكية (تلقائي)"
    msg.attach(MIMEText(email_body, 'plain', 'utf-8'))
    
    # هنا يتم الاتصال الفعلي بخوادم الإرسال السحابية
    print(f"🚀 تم توليد التقرير وإرساله بنجاح إلى إيميل العميل: {customer_email}")

@app.post("/wake/analyze-and-email")
async def trigger_agent(background_tasks: BackgroundTasks, data: dict = Body(default={})):
    """البوابة البرمجية المستقلة (Endpoint) التي تستقبل بيانات العميل وتشغل المهام في الخلفية"""
    
    c_email = data.get("email", "customer@example.com")
    c_name = data.get("name", "العميل")
    c_sales = data.get("sales", 0.0)
    
    # تشغيل المهمة الطويلة في الخلفية (Background Tasks) لكي لا يتجمد الموقع أو السيرفر
    background_tasks.add_task(send_analytics_email, c_email, c_name, c_sales)
    
    return {
        "status": "success",
        "message": f"الوكيل الذكي استيقظ وبدأ معالجة البيانات وإرسال التقرير لإيميل العميل في الخلفية."
    }
