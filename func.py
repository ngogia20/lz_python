import oci
from python_terraform import *
import wget
import os, zipfile
import io
from fdk import response

ret = "Nikesh"
# Import Code from Github or Orahub
def ocr_lz():
    #os.system('pwd')
    #os.system('ls -l') # /tmp/oci_lz
    #dirlist=os.listdir(os.getcwd()) #[]
    #print(dirlist,flush=True)
    #dir_name='/tmp'
    #gurl = "https://github.com/ngogia20/oci_lz/archive/refs/heads/master.zip"
    #ret="200"
    #wget.download(gurl,out=dir_name)
    # dir_name = '/tmp' #os.getcwd()
    #extension = ".zip"
    #ret="900"
    #ret="100"
    #for item in os.listdir(dir_name): # loop through items in dir
        #if item.endswith(extension): # check for ".zip" extension
        #    file_name = os.path.abspath(item) # get full path of files
        #    zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        #    zip_ref.extractall(dir_name) # extract file to dir
        #    zip_ref.close() # close file
        #    os.remove(file_name) # delete zipped file
    #try:
    #    os.system('terraform init')
    #    os.system('terraform plan')
    #    os.system('terraform apply -auto-approve')
    #except (Exception, ValueError) as e2:
    #    print("SEE ERROR",flush=True)
    #    print(str(e2), flush=True)
    os.system('ls -l')
    os.system('cp -rf oci_lz /tmp')

    os.system('terraform -chdir=/tmp/oci_lz init')
    os.system('terraform -chdir=/tmp/oci_lz plan')

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