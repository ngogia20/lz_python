import oci
from python_terraform import *
import wget
import os, zipfile
import io
from fdk import response


# Import Code from Github or Orahub
def ocr_lz():
    gurl = "https://github.com/ngogia20/oci_lz/archive/refs/heads/master.zip"
    wget.download(gurl)
    dir_name = '/tmp' #os.getcwd()
    extension = ".zip"
    os.chdir(dir_name) # change directory from working dir to dir with files

    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
    t = Terraform(working_dir=dir_name+"/oci_lz-master")

    #t = Terraform(working_dir='.')

    # Code for uploading the terraform.tfstate to Objct Storage and have the pre-authenticated url

    # Start Terraform init, apply
    return_code0, stdout0, stderr = t.init()
    return_code0, stdout2, stderr2 = t.plan()
    return_code1, stdout1, stderr1 = t.apply(skip_plan=True)

    # Websocket logic also need to be applied for logs
    print(stdout1,stderr1)
    return[stdout1,stderr1]

def handler(ctx, data: io.BytesIO=None):
    print("Entering Python Hello World handler", flush=True)
    ret = "World"
    try:
        #body = json.loads(data.getvalue())
        #name = body.get("name")
        ret=ocr_lz()
    except (Exception, ValueError) as ex:
        print(str(ex), flush=True)

    #print("Vale of name = ", name, flush=True)
    #print("Exiting Python Hello World handler", flush=True)
    return response.Response(
        ctx, response_data=json.dumps(
            {"200": ret}),
        headers={"Content-Type": "application/json"}
    )