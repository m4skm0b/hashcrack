__author__ = 'BT'

import hashlib
import optparse

def crackPass(md5Pass, dictPath):
    try:
        dictFile = open(dictPath, 'r')
    except:
        print '[-] File Can Not Open'
        exit(0)
    for word in dictFile.readlines():
        word = word.strip('\n')
        md5Word = md5Encode(word)
        if md5Word == md5Pass:
            return word
    return None

def md5Encode(word):
    m = hashlib.md5()
    m.update(word)
    md5Word = m.hexdigest()
    return md5Word

def main():
    parser = optparse.OptionParser("usage%prog -d <dictionary path> -t <md5 password>")
    parser.add_option('-d', dest='dictPath', type='string', help='specify dictionary file')
    parser.add_option('-t', dest='md5Pass', type='string', help='specify crack md5 target')
    (options, args) =parser.parse_args()
    if (options.dictPath == None) | (options.md5Pass == None):
        print parser.usage
        exit(0)
    else:
        dictPath = options.dictPath
        md5Pass = options.md5Pass

    resl = crackPass(md5Pass, dictPath)
    if resl != None:
        print '[+] Crack Success: ' + resl + '\n'
    else:
        print '[-] Password Not Found.\n'

if __name__ == "__main__":
    main()
