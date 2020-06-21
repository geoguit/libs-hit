# libs-hit
Sends data to Australian Liberal Party sites.

# Todo
The Northern Territory CLP and reCaptcha research on the NSW, Victoria, and Tasmania sites.

# Setup
Run the following command to install the necessary Python libraries:  
<code>pip install Pillow requests pytesseract</code>  
  
Then install the following applications:  
https://imagemagick.org/script/download.php  
https://github.com/tesseract-ocr/tesseract  
  
You may have to specify where Tesseract has been installed to in the Python script, which can be done by editing the <code>pytesseract.pytesseract.tesseract_cmd</code> value.
