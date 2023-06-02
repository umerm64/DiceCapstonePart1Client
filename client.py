import requests as req
import time
import hashlib
import os

if __name__ == '__main__':
    try:
        server = os.getenv('SERVER_IP')
        if server is None: 
            raise Exception("SERVER_IP environment variable not found")
        filename = '/clientdata/file.txt'
        url = 'http://'+server+':5000/download_file'
        print(url)
        res = req.get(url)
        if (res.status_code == 200):
            f = open(filename, 'wb')
            f.write(res.content)
            f.close()

            url = 'http://'+server+':5000/checksum'
            res = req.get(url)
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
