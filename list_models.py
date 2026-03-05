import google.generativeai as genai
import os

key = os.environ.get('GEMINI_API_KEY')
print('Key present', bool(key))
if key:
    genai.configure(api_key=key)
    try:
        models = genai.list_models()
        print('models = [')
        for m in models:
            print(' ', m)
        print(']')
    except Exception as e:
        print('error listing models', e)
