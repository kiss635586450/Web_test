import re

def check_string(text, pattern):
    """"
    ����ַ����Ƿ����ָ������
    :param text: ��Ҫ�����ַ���
    :param pattern: ��ʽ���ʽ���磺'^[a-zA-Z]+$'
    :return: ����ָ���ַ�ʱ�����棬����Ϊ��
    """
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False

def is_email(text):
    """
        ����ַ����Ƿ���email
        :param text: ��Ҫ�����ַ���
        :return: ����ָ���ַ�ʱ�����棬����Ϊ��
        """
    return check_string(text, '[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')

def is_phone(text):
    """
       ����ַ����Ƿ��ǵ绰
       :param text: ��Ҫ�����ַ���
       :return: ����ָ���ַ�ʱ�����棬����Ϊ��
    """
    return check_string(text, '\(?0\d{2,3}[) -]?\d{7,8}$')

def is_mobile(text):
    """
    �Ƿ����ֻ�����
    :param text:
    :return:
    """
    return check_string(text, '^1[3578]\d{9}$|^147\d{8}$')

def is_letters(text):
    """
           ����ַ����Ƿ�ȫ����ĸ
           :param text: ��Ҫ�����ַ���
           :return: ����ָ���ַ�ʱ�����棬����Ϊ��
    """
    return check_string(text, '^[a-zA-Z]+$')

def is_idcard(text):
    """
    �Ƿ������֤����
    :param text:
    :return:
    """
    ic = IdentityCard()
    return ic.check(text.upper())

def filter_str(text, filter='\||<|>|&|%|~|\^|;|\''):
    """"
    �����ַ���
    filter:���˵����ݣ������
    """
    if text:
        return re.subn(filter, '', text)[0]
    else:
        return ''

def filter_tags(hemlstr):
    """
    ����HTML�еı�ǩ
    :param hemlstr:
    :return:
    """
    re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I)#ƥ��CDATA
    re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br = re.compile('<br\s*?/?>')#������
    re_h = re.compile('</?\w+[^>]*>')#HTML��ǩ
    re_comment = re.compile('<!--[^>]*-->')#HTMLע��
    s = re_cdata.sub('', hemlstr)#ȥ��CDATA
    s = re_script.sub('', s)#ȥ��script
    s = re_style.sub('', s)#ȥ��style
    s = re_br.sub('\n', s)#ȥ��brת��Ϊ����
    s = re_h.sub('', s)#ȥ��html��ǩ
    s = re_comment.sub('', s)#ȥ��htmlע��
    #ȥ������Ŀ���
    blank_line = re.compile('\n+')
    s = blank_line.sub('\n', s)
    s = replaceCharEntity(s)#�滻ʵ��
    return s

def replaceCharEntity(htmlstr):
    """
    �滻���õ�HTML�ַ�
    :param htmlstr:
    :return:
    """
    CHAR_ENTITIES = {
        'nbsp': ' ', '160': ' ',
        'lt': '<', '60': '<',
        'gt': '>', '62': '>',
        'amp': '&', '38': '&',
        'quot': '"', '34': '"',
    }
    re_charEntity = re.compile(r'&#?(?P<name>\w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()#entityȫ�ƣ���&gt
        key = sz.group('name')#ȥ��&����entity����&gt��Ϊgt
        try:
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            #�Կ��ַ������
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr

def string(text, is_return_null = False):
    """
    sql�ַ���ƴ��ר�ú���
    �����ַ���������ӡ���Ʋ�ţ������������ݿ�sql���
    :param text:
    :param is_return_null:�Ƿ񷵻�null���ǵĻ����ַ���Ϊ��ʱ����null�����򷵻�''
    :return:
    """
    if not text is None and text != '':
        return "'" + str(text) + "'"
    elif not is_return_null:
        return "''"
    else:
        return "null"

def cut_str(text, length):
    """
    ���ַ�����ȡָ�������ַ���
    :param text:
    :param length:
    :return:
    """
    if not text or not isinstance(text, str):
        return text
    tem = ''
    try:
        tem = text.encode('utf8')#?/?tem = text.decode('utf8')
    except:
        pass
    if not tem or tem == '':
        try:
            tem = text[0: length]
        except:
            tem = text
    return tem[0: length]

class IdentityCard:
    """
    ���֤������֤��
    """
    def  __init__(self):
        self.__Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        self.__Ti = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    def calculate(self, code):
        """
        ����У��λ
        :param code:
        :return:
        """
        sum = 0
        for i in range(17):
            sum += int(code[i]) * self.__Wi[i]
        return self.__Ti[sum % 11]

    def check(self, code):
        """
        �������ĺ����Ƿ���ȷ
        :param code:
        :return:
        """
        if (len(code) != 18):
            return False
        if self.calculate(code) != code[17]:
            return False
        return True