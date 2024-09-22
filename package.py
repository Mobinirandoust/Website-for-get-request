from random import randint

urls = {
    'index':'/',
    'land7':'/landsat7',
    'land8':'/landsat8',
    'land9':'/landsat9',
    "SuperUSer":"/admin",
    'del7':"/admin/delete7/<name>",
    'del8':"/admin/delete8/<name>",
    'del9':"/admin/delete9/<name>",
    'get':"/<name>",
    'store':"/store/images/",
    'getcode':"/get-code/",
    "gcup":"/getcode/admin/update"
}

def unic():
    n = 1
    for i in range(1,10):
        n *= randint(1,9)
    return n