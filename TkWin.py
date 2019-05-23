
import json,pathlib,os,time,requests
from tkinter import *
from tkinter import messagebox

class MyWindow:
    def __init__(self, win):

        self.lbl1=Label(win, text='URL')
        self.lbl2=Label(win, text='TOKEN')
        self.lbl3=Label(win, text='Result')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        #self.t3=Entry()
        #self.btn1 = Button(win, text='Acesso')
        #self.btn2=Button(win, text='Criptografar')
        #self.btn3=Button(win, text='Enviar Arquivo')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Acesso/Salvar', command=self.add)
        self.b2=Button(win, text='Criptografar/Decifra')
        self.b3=Button(win, text='Enviar Arquivo',command=self.send)
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
        self.b3.place(x=240, y=150)
        self.lbl3.place(x=100, y=200)
        #self.t3.place(x=200, y=200)
    def add(self):
        if self.t1.get() == '' or self.t2.get() == '':return messagebox.showinfo("Erro", "Informe URL/Token")

        result=self.salvar_arquivo(os.getcwd(),'answer','json',self.get_acesso(self.t1.get(),self.t2.get()))
        #self.t3.insert(END, str(result))
        self.lbl3.configure( text=result)
    def sub(self, event):
        self.atualizar_arquivo()
        respJson= json.loads( pathlib.Path("answer.json").read_text())
        #result=self.criptografar_sha1(self.decifra(respJson['cifrado'],5))
        #print(result)
        self.lbl3.configure( text='* DEFCIFRADO => ' +respJson['decifrado'])
        #self.t3.insert(END, str(result))
    def send(self):
        myCmd = 'node SendNode.js > out.txt'
        os.system(myCmd)
        #time.sleep(4)
        respJson= json.loads( pathlib.Path("out.txt").read_text())
        self.lbl3.configure( text=respJson)

    def get_acesso(self,url,token):
        resp = requests.get(url + '?token=' + token)
        if resp.status_code == 200:
           retorno = resp.json()
           retorno.update({'status':200})
        return retorno

    def salvar_arquivo(self,path,nome,extensao,respJson):
        if respJson['status'] != 200: return '* Arquivo não pode ser gravado!'
        try:
           respJson.pop('status')
           pathlib.Path("%s/%s.%s" % (path,nome,extensao)).write_text(json.dumps(respJson, indent=4))
           return '* Arquivo salvo com sucesso em =>  ' + os.getcwd()
        except:
           return '* Erro ao salvar Arquivo!'
    def decifra(self,mensagem, chave):
        decifrado = ''
        ignore=[' ','.','!','?',':',';',',']
        #mensagem = mensagem.replace('.','')
		mensagem = mensagem.lower()
        for letra in mensagem:
           if letra.isalpha():
             numero = ord(letra) - chave
             if numero < ord('a'):numero += 26
           letraOriginal = chr(numero)
           if letra in ignore: decifrado += letra
           else: decifrado += letraOriginal
        return decifrado
    def criptografar_sha1(self,texto):
        m = hashlib.sha1()
        m.update(texto.encode())
        return {'resumo_criptografico': m.hexdigest(),'decifrado':texto}
    def atualizar_arquivo(self):
        respJson=json.loads( pathlib.Path("answer.json").read_text())
        respJson.update( self.criptografar_sha1(self.decifra(respJson['cifrado'],5)))
        respJson.update({'status':200})
        self.salvar_arquivo(os.getcwd(),'answer','json',respJson)
		   
		   

def run():
	window=Tk()
	mywin=MyWindow(window)
	window.title("CodeNation - Criptografia de Júlio César")
	window.geometry("600x300+10+10")
	window.mainloop()

