import hashlib

def md5(str):
    """
    MD5加密
    :param str:
    :return:
    """
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()