import oci
from python_terraform import *
import wget
import os, zipfile
import io
from fdk import response

ret = "Nikesh"
# Import Code from Github or Orahub
def ocr_lz():
    #os.chdir('/tmp/oci_lz')
    #dirlist1=os.listdir(os.getcwd())
    #print(dirlist1,flush=True)
    os.system('pwd')
    os.system('ls -l')
    gurl = "https://github.com/ngogia20/oci_lz/archive/refs/heads/master.zip"
    wget.download(gurl)
    extension = ".zip"
    ret="900"
    #os.chdir(dir_name) # change directory from working dir to dir with files
    ret="100"
    dir_name=os.getcwd()
    for item in os.listdir(os.getcwd()): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file

    os.chdir("oci_lz-master")
    #os.mkdir('/tmp/newoci_lz')
    #os.chdir('/tmp/newoci_lz')
    #os.system('cp -rf /tmp/oci_lz /tmp/newoci_lz')
    dirlist=os.listdir(os.getcwd())
    print(dirlist,flush=True)
    #wget.download('https://objectstorage.ap-mumbai-1.oraclecloud.com/n/apaccpt03/b/pyt_exp/o/oci_api_key.pem')
    #os.system('chmod 777 /tmp/newoci_lz/*')
    #dir_list = os.listdir(os.getcwd())
    #print(dir_list,flush=True)
    #print("Check Here",flush=True)
    try:
        os.system('terraform init')
        os.system('terraform plan')
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