__author__ = 'BT'

import hashlib
import optparse

def crackPass(hashType, hashPass, dictPath):
    try:
        dictFile = open(dictPath, 'r')
    except:
        print '[-] File Can Not Open'
        exit(0)
    for word in dictFile.readlines():
        word = word.strip('\n')
        if hashType == 'md5':
            hashWord = md5Encode(word)
        elif hashType == 'sha1':
            hashWord = sha1Encode(word)
        elif hashType == 'sha256':
            hashWord = sha256Encode(word)
        elif hashType == 'sha512':
            hashWord = sha512Encode(word)
        else:
            return None
        if hashWord == hashPass:
            return word
    return None

def md5Encode(word):
    m = hashlib.md5(word)
    md5Word = m.hexdigest()
    return md5Word

def sha1Encode(word):
    s = hashlib.sha1(word)
    sha1Word = s.hexdigest()
    return sha1Word

def sha256Encode(word):
    s = hashlib.sha256(word)
    sha256Word = s.hexdigest()
    return sha256Word

def sha512Encode(word):
    s = hashlib.sha512(word)
    sha512Word = s.hexdigest()
    return sha512Word

def main():
    parser = optparse.OptionParser("usage%prog -h <hash type> -d <dictionary path> -t <hash password>")
    parser.add_option('-t', dest='hashType', type='string', help='specify hash type')
    parser.add_option('-d', dest='dictPath', type='string', help='specify dictionary file')
    parser.add_option('-g', dest='hashPass', type='string', help='specify crack hash target')
    (options, args) =parser.parse_args()
    if (options.hashType == None) | (options.dictPath == None) | (options.hashPass == None):
        print parser.usage
        exit(0)
    else:
        hashType = options.hashType
        dictPath = options.dictPath
        hashPass = options.hashPass
    if (hashType != 'md5') & (hashType != 'sha1') & (hashType != 'sha256') & (hashType != 'sha512'):
        print '[-] Hash Type Error'
        print parser.usage
        exit(0)

    resl = crackPass(hashType, hashPass, dictPath)
    if resl != None:
        print '[+] Crack Success: ' + resl + '\n'
    else:
        print '[-] Password Not Found.\n'

if __name__ == "__main__":
    main()
