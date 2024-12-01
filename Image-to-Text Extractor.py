from tkinter import Tk, Label, Button, filedialog, Text, Scrollbar, END, messagebox
from PIL import Image
import pytesseract

# Path to Tesseract executable (modify as needed for your environment)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    """
    Extract text from an image file.
    Parameters:
        image_path (str): Path to the image file. 
    Returns:
        str: Extracted text from the image.
    """
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {e}"

def select_file():
    """
    Open a file dialog to select an image file and extract text from it.
    """
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.tiff")]
    )
    if file_path:
        try:
            extracted_text = extract_text(file_path)
            text_box.delete("1.0", END)
            text_box.insert(END, extracted_text)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = Tk()
root.title("Image to Text Extractor")
root.geometry("600x400")

Label(root, text="Select an image to extract text:", font=("Arial", 12)).pack(pady=10)

Button(root, text="Choose File", command=select_file, font=("Arial", 10)).pack(pady=5)

# Text box with scrollbar to display extracted text
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text_box = Text(root, wrap="word", yscrollcommand=scrollbar.set, font=("Arial", 10))
text_box.pack(expand=True, fill="both", padx=10, pady=10)

scrollbar.config(command=text_box.yview)

# Run the GUI
root.mainloop()