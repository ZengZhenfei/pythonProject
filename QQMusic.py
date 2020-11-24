from PyExecJS import execjs


def get_sign(data):
    with open('a.js', 'r', encoding='utf-8') as f:
        text = f.read()
    js_data = execjs.compile(text)
    sign = js_data.call('get_sign', data)
    return sign


if __name__ == "__main__":
    data = '{"comm":{"ct":24,"cv":0},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":2,"sin":0,"cur_page":1}}}'
    sign = get_sign(data)
    print(data)
    print(sign)