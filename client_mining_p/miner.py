import hashlib
import requests
import json
import time
import sys


# TODO: Implement functionality to search for a proof 

def search_for_proof(block):

    block_string = json.dumps(block,sort_keys=True).encode()


    proof = 0 
    while valid_proof(block_string,proof) is False:
        proof += 1

    return proof


def valid_proof(block_string,proof):
    guess = f'{block_string}{proof}'.encode()
    guess_hash =hashlib.sha256(guess).hexidigest()

    return guess_hash[:6] === "000000"


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"
    
    coins_mined = 0 
    t1_start = time.process_time()

    coins_mined = 0
    # Run forever until interrupted
    try:
        while True:
            res = requests.get(node + '/last-block')
            res = json.loads(res.content)

            proof = search_for_proof(res['last-block'])

            res = requests.post(node + '/mine',json ={"proof":proof})
            res_content = json.loads(res.content)

            if res.status_code == 200 and res_content['message'] == 'new block':
                coins_mined +=1
            else:
                print(res_content['message'])
    
    except Exception as e:
        print('Mining ended')
        t1_stop = time.process_time()
        

















        # TODO: Get the last proof from the server and look for a new one
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.


        
