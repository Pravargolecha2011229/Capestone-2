import os
import app

os.environ['GEMINI_API_KEY'] = "AIzaSyAsSgA2Sez4YZ6QvfPpYQXWE3w4BqyFZ08"

m = app.get_model()
print('got model', m)
if m:
    print('name', getattr(m,'name',None))
    try:
        r = m.generate_content('test')
        print('response', r.text[:100])
    except Exception as e:
        print('generation error', e)
