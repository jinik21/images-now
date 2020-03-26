#pip install simple-image-download
#pip install flask
from flask import Flask,render_template,request
from simple_image_download import simple_image_download as simp
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from zipfile import ZipFile
import shutil



response = simp.simple_image_download




app=Flask( __name__)
@app.route("/",methods=["POST","GET"])
def index():
    return render_template('imagesnow.html')
    
@app.route("/thankU",methods=["POST"])
def thankU():
    keyword=request.form.get("keyword")
    noi=int(request.form.get("noi"))
    email=request.form.get("email")
    arguments = {"keywords":keyword,"limit":noi}
    response().download(keyword,noi)
    of=keyword
    of.replace(" ","")
    
    
    
    keyword="/root/gidm/simple_images/"+keyword
    
    
    shutil.make_archive(of, 'zip',keyword)
    fromaddr = "imagedownloadmanager007@gmail.com"
    toaddr = email
    
    # instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # storing the senders email address   
    msg['From'] = fromaddr 
    
    # storing the receivers email address  
    msg['To'] = toaddr 
    
    # storing the subject  
    msg['Subject'] = "IMAGES"
    
    # string to store the body of the mail 
    body = "HI THERE ,\n HERE ARE THE IMAGES YOU ASKED FOR\n\n\n\n\n\n\nTHANK YOU \nIMAGES NOW\nKEEP DOWNLOADING............"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    # open the file to be sent  
    filename = of+".zip"
    path=of+".zip"
    attachment = open(path, "rb") 
    
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    
    # encode into base64 
    encoders.encode_base64(p) 
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, "nikheel@007") 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit() 






    return render_template('thankU.html',)





app.run(debug=True)
