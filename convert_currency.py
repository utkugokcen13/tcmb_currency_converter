# Effective dollar value will be taken from the TCMB website.

# https://www.turkiye.gov.tr/doviz-kurlari

from tkinter import *
from tkinter import messagebox
from bs4 import *
import requests



window = Tk()

window.title("Currency Converter")
window.configure(background='light grey')
window.resizable(width="false",height="false")

def convert_dollar():
    site = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")

    soup = BeautifulSoup(site.text, "html.parser")

    efektif_dolar_satis = soup.find('td', text='1 ABD DOLARI').find_next_sibling('td') \
        .find_next_sibling('td') \
        .find_next_sibling('td') \
        .find_next_sibling('td').text

    tl_miktar = dollar_txt.get() * float(efektif_dolar_satis)
    lira_txt.set(round(tl_miktar,2))
    messagebox.showinfo("Hatırlatma","TCMB efektif dolar alış fiyatından çevrilmiştir.")



# ekranı ortala
def center_window(w, h):
    # get screen width and height
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(300, 250)

dollar_label = Label(window,text="Dollar: ",font="Arial 12 bold",bg='light grey', fg='black')
dollar_label.grid(row=0,column=0,padx=10,pady=10,sticky='E')


dollar_txt = DoubleVar();
dollar_entry = Entry(window, width=10, textvariable=dollar_txt,justify=RIGHT)
dollar_entry.grid(row=0,column=1)


lira_label = Label(window,text="Türk Lirası:",font="Arial 12 bold",bg='light grey', fg='black')
lira_label.grid(row=1,column=0,padx=10,pady=10,sticky='W')

lira_txt = DoubleVar();
lira_entry = Entry(window, width=10, textvariable=lira_txt,justify=RIGHT)
lira_entry.grid(row=1,column=1)

cevir_buton = Button(window, text='ÇEVİR', font='Arial 10 bold', bg='blue', fg='white',command=convert_dollar)
cevir_buton.grid(row=3, column=1, pady=(15,0))

window.mainloop()