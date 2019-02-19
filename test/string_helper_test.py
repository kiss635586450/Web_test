import unittest
from common import string_helper

class DbHelperTest(unittest.TestCase):
    def test_clear_xss(self):
        print('-----test_clear_xss------')
        print(string_helper.clear_xss('<script src="javascript:alert(1);">abc</script>'))
        print(string_helper.clear_xss('<iframe src="javascript:alert(1);">abc</iframe>'))
        print(string_helper.clear_xss(
            '<div style="width:0;height:0;background:url(javascript:document.body.onload = function(){alert(/XSS/);};">div</div>'))
        print(string_helper.clear_xss('<img src = "#"/**/onerror = alert(/XSS/)>'))
        print(string_helper.clear_xss('<img src = j ava script:al er t(/XSS/)>'))
        print(string_helper.clear_xss("""<img src = j
    ava script :a ler t(/xss/)>"""))
        print(string_helper.clear_xss('<img src="javacript:alert(\'abc\')"></img>'))
        print(string_helper.clear_xss('<img src="https://www.baidu.com/img/baidu_jgylogo3.gif"></img>'))
        print(string_helper.clear_xss('<p src="javascript:alert(1);">abc</p>'))
        print(string_helper.clear_xss("""<input type="text" value="琅琊榜" onclick="javascript:alert('handsome boy')">"""))
        print(string_helper.clear_xss('<p onclick="javascript:alert("handsome boy")>abc</p>'))
        print(string_helper.clear_xss('<a href="javascript:alert(1);">abc</a>'))
        print(string_helper.clear_xss('<a href="/api/">abc</a>'))
        print(string_helper.clear_xss('<a href="http://www.baidu.com">abc</a>'))
        print(string_helper.clear_xss('<marquee onstart="alert(/XSS/)">文字</marquee>'))
        print(string_helper.clear_xss('<div style="" onmouseenter="alert(/XSS/)">文字</div>'))
        print(string_helper.clear_xss('<li style = "TEST:e-xpression(alert(/XSS/))"></li>'))
        print(string_helper.clear_xss('<input id = 1 type = "text" value="" <script>alert(/XSS/)</script>"/>'))
        print(string_helper.clear_xss('<base href="http://www.labsecurity.org"/>'))
        print(string_helper.clear_xss('<div id="x">alert%28document.cookie%29%3B</div>'))
        print(string_helper.clear_xss('<limited_xss_point>eval(unescape(x.innerHTML));</limited_xss_point>'))

if __name__ == '__main__':
    unittest.main()