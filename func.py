import oci
from python_terraform import *
import wget
import os, zipfile
import io
from fdk import response

ret = "Nikesh"
# Import Code from Github or Orahub
def ocr_lz():
    os.system('cp -rf /function/oci_lz /tmp/oci_lz')
    os.system('chmod 777 /tmp/oci_lz')
    os.chdir('/tmp/oci_lz')
    wget.download('https://objectstorage.ap-mumbai-1.oraclecloud.com/n/apaccpt03/b/pyt_exp/o/oci_api_key.pem')
    os.system('chmod 777 /tmp/oci_lz/*')
    #dir_list = os.listdir(os.getcwd())
    #print(dir_list,flush=True)
    #print("Check Here",flush=True)
    try:
        os.system('terraform apply -auto-approve')
    except (Exception, ValueError) as e2:
        print("SEE ERROR",flush=True)
        print(str(e2), flush=True)

    #print("With Siva Sir Nikesh 3",flush=True)
    #print(comm4,flush=True)

    #t = Terraform('/function/oci_lz-master')
    #ret2,stdout2, stderr2=t.apply(skip_plan=True)
    
    return "success"

    # Websocket logic also need to be applied for logs
    #print(stdout1,stderr1)
    #return[stdout1,stderr1]

def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Set LZß handler", flush=True)
    ret = "World"
    try:
        #body = json.loads(data.getvalue())
        #name = body.get("name")
        ret="Gogia"
        ret=ocr_lz()
        print(ret,flush=True)
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)

    return response.Response(
        ctx, response_data=json.dumps(
            {"200": ret}),
        headers={"Content-Type": "application/json"}
    )