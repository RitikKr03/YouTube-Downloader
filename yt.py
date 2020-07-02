from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *

# yt = YouTube("https://www.youtube.com/watch?v=xLpZZScqgKo")
# print(yt.title)
# print(yt.description)
# print(yt.views)
# print(yt.rating)
# print(yt.length)
# print(yt.author)
# print(yt.thumbnail_url)
# st = yt.streams.first()
# st.download()

font = ('verdana', 20)
file_size = 0


#oncomplete callback function
def completeDownload(stream=None, path=None):
    print("Download Completed")
    showinfo("Message", "File has been downloaded")
    DLBtn['text'] = "Download Video"
    DLBtn['state'] = "active"
    urlField.delete(0, END)


#onprogress callback function
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percent = (100 * ((file_size - bytes_remaining) / file_size))
    DLBtn['text'] = "{:00.0f} % downloaded".format(percent)


#dl function
def startDownload(url):
    global file_size
    path = askdirectory()
    if path is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completeDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path)

    except Exception as e:
        print(e)
        print("Something went wrong!!")


def btnClicked():
    try:
        DLBtn['text'] = "Please wait..."
        DLBtn['state'] = 'disabled'
        url = urlField.get()
        if url == '':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()


    except EXCEPTION as e:
        print(e)


#GUI
root = Tk()
root.title("My YT Downloader")
root.iconbitmap("img/icon.ico")
root.geometry("500x600")

#mainicon
file = PhotoImage(file="img/logo.png")
headingIcon = Label(root, image=file)
headingIcon.pack(side=TOP, pady=3)

#URL
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

#DLButton
DLBtn = Button(root, text="Download Video", font=font, relief='ridge', command=btnClicked)
DLBtn.pack(side=TOP, pady=20)

root.mainloop()
