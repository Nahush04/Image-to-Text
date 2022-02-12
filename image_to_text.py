from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'#add Tesseract path

root = Tk()
root.title('Image to Text') 

newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

def extract(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_string(img)
    print(texts)

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),bg="#DAF7A6",fg="#467451",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#97CFE5",fg="#4F2264",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

root.mainloop()
