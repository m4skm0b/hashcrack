# hashcrack

当hash破解不出时，可通过社工手段搜集可能的密码字典，然后使用此工具进行比对破解。

此工具会将字典中的每个word进行hash，然后与提供的hash进行比对。

支持md5/sha1/sha256/sha512


Options:

  -h, --help   show this help message and exit
  
  -t HASHTYPE  specify hash type, md5/sha1/sha256/sha512
  
  -d DICTPATH  specify dictionary file
  
  -g HASHPASS  specify crack hash target
