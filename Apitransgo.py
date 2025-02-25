from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# النقطة الرئيسية
@app.route('/')
def home():
    return "مرحبًا بك في API الترجمة! استخدم /translate للترجمة أو /about لمزيد من المعلومات."

# نقطة الترجمة
@app.route('/translate', methods=['GET'])
def translate_text():
    try:
        # جلب المعالم من الطلب
        text = request.args.get('text')
        source_lang = request.args.get('source_lang')
        target_lang = request.args.get('target_lang')

        # التحقق من القيم
        if not text or not source_lang or not target_lang:
            return jsonify({"error": "يجب إدخال النص واللغتين (المصدر والهدف)."}), 400

        # الترجمة
        translated_text = translator.translate(text, src=source_lang, dest=target_lang).text
        
        # إرجاع النتيجة
        return jsonify({
            "original_text": text,
            "translated_text": translated_text,
            "source_language": source_lang,
            "target_language": target_lang
        })
    
    except Exception as e:
        return jsonify({"error": f"حدث خطأ: {str(e)}"}), 500

# نقطة about
@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "API Name": "Translation API",
        "Version": "1.0",
        "Description": "واجهة برمجة ترجمة نصوص باستخدام مكتبة googletrans",
        "Endpoints": {
            "/": "النقطة الرئيسية",
            "/translate": "نقطة الترجمة (تحتاج إلى text و source_lang و target_lang)",
            "/about": "معلومات حول الواجهة"
        }
    })

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
