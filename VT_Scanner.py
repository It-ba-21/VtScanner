import requests
import time
from tkinter import *
from tkinterdnd2 import TkinterDnD, DND_FILES

API_KEY = "8041fc865e31f7119f255f5a14619ca284aa2978108a54baaf27a0dd3fa274e4"

def scan_file(file_path):

    result_box.insert(END, "\nUploading file...\n")

    url = "https://www.virustotal.com/api/v3/files"

    headers = {"x-apikey": API_KEY}

    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, headers=headers, files=files)

    analysis_id = response.json()["data"]["id"]

    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

    while True:
        r = requests.get(analysis_url, headers=headers)
        result = r.json()

        if result["data"]["attributes"]["status"] == "completed":
            break

        time.sleep(3)

    stats = result["data"]["attributes"]["stats"]

    result_box.insert(END, "\n===== RESULT =====\n")
    result_box.insert(END, f"Malicious: {stats['malicious']}\n")
    result_box.insert(END, f"Suspicious: {stats['suspicious']}\n")
    result_box.insert(END, f"Undetected: {stats['undetected']}\n")
    result_box.insert(END, f"Harmless: {stats['harmless']}\n")


def drop(event):

    file_path = event.data.replace("{","").replace("}","")

    result_box.insert(END, f"\nFile: {file_path}\n")

    scan_file(file_path)


app = TkinterDnD.Tk()
app.title("Mini VirusTotal Scanner")
app.geometry("500x400")

label = Label(app,text="Drag & Drop File Below",font=("Arial",14))
label.pack(pady=10)

drop_area = Label(app,text="DROP FILE HERE",bg="lightblue",width=40,height=5)
drop_area.pack(pady=20)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind("<<Drop>>", drop)

result_box = Text(app,height=10,width=60)
result_box.pack(pady=10)

app.mainloop()