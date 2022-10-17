import oci
from python_terraform import *
import wget
import os, zipfile
import io
from fdk import response

ret = "Nikesh"
# Import Code from Github or Orahub
def ocr_lz():
    dir_name = '/tmp'
    os.chdir(dir_name)
    gurl = "https://github.com/ngogia20/oci_lz/archive/refs/heads/master.zip"
    ret="200"
    wget.download(gurl,out=dir_name)
    # dir_name = '/tmp' #os.getcwd()
    extension = ".zip"
    ret="900"
    os.chdir(dir_name) # change directory from working dir to dir with files
    ret="100"
    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
    ret="22222"
    os.chdir("oci_lz-master")
    dir_list = os.listdir(os.getcwd())
    print(dir_list,flush=True)
    print("Check Here",flush=True)
    t = Terraform(os.getcwd())
    print(t,flush=True)

    comm=os.system('terraform -version')
    print("With Siva Sir Nikesh",flush=True)
    print(comm,flush=True)

    #ret0,stdout0, stderr0=t.init()
    #print("With Siva",flush=True)
    #print(stderr0,flush=True)
    
    #ret1,stdout1, stderr1=t.plan()
    #print("With Siva1",flush=True)
    #print(stderr1,flush=True)
    
    #ret2,stdout2, stderr2=t.apply(skip_plan=True)
    #print("With Siva2",flush=True)
    #print(stderr2,flush=True)
    
    return "Success"

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