import requests as req
import time
import hashlib

if __name__ == '__main__':
    try:
        filename = '/clientdata/file.txt'
        res = req.get('http://server/download_file')
        if (res.status_code == 200):
            f = open(filename, 'wb')
            f.write(res.content)
            f.close()

            res = req.get('http://server:5000/checksum')
            if (res.status_code == 200) and (res.text == hashlib.md5(open(filename,'rb').read()).hexdigest()):
                print('Correct file downloaded!')
            else:
                print('Integrity failed!')
        else:
            print('Error getting file from server,', res.status_code)
    except Exception as e:
        print('Exception: ', e)

    # while(True):
    #     time.sleep(1)
