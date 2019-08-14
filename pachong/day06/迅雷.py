import base64


def download_address_translation(original_address):
    original_address = str(original_address)
    if "thunder://" in original_address:
        original_address = original_address.replace('thunder://', '')
        print(original_address)
        original_address = base64.b64decode(original_address)
        print(original_address)
        original_address = original_address.decode('gbk')
        print(original_address)
        original_address = original_address[2:len(original_address) - 2]

    return {'origin': original_address}


def create_thuder_url(original_address):
    original_address = str(original_address)
    original_address = 'AA' + original_address + 'ZZ'
    print(original_address)
    original_address = original_address.encode('gbk')
    print(original_address)
    original_address = base64.b64encode(original_address)
    print(original_address)
    original_address = 'thunder://' + original_address.decode()
    thunder_address = original_address

    return thunder_address


base_thunder_address = 'thunder://QUFodHRwczovL2F2YXRhci5jc2RuLm5ldC8yLzAvOC8zX3dlaXhpbl80MDkwNzM4Mi5qcGdaWg=='
print('输入迅雷地址:', base_thunder_address)
address = download_address_translation(base_thunder_address)
print('还原下载地址:', address.get('origin'))
thunder_address = create_thuder_url(address.get('origin'))
print('还原迅雷地址:', thunder_address)
