import ssocket
import Tkinter as tk

class guified:
	def __init__(self,root):
		frame=tk.Frame(root)
		frame.grid()
		
		self.chatarea=tk.LabelFrame(frame,text="chat")
		self.chatarea.grid(column=0,row=1,sticky=tk.E)

		wd=40
		self.labellist=[]
		
		chattext=tk.Frame(frame)
		chattext.grid(column=0,row=2,sticky=tk.E)
	
		wd_btn=7
		textBox=tk.Text(chattext,height=2,width=wd-wd_btn)
		textBox.grid(column=0,row=0)
		textBox.bind("<Return>",lambda event:self.btnpress(event,textBox))

		btn=tk.Button(chattext,text="Send",width=wd_btn)
		btn.grid(column=1,row=0)
		btn.bind("<Button-1>",lambda event:self.btnpress(event,textBox))

		# Sidebar

		sidebox=tk.Frame(frame)
		sidebox.grid(column=1,row=0,sticky=tk.W)

		label1=tk.Label(sidebox,text="This text is over here",width=wd)
		label1.grid()

	def btnpress(self,event,textBox):
		txt=textBox.get(0.0,tk.INSERT)
		textBox.delete(0.0,tk.END)
		if len(self.labellist)%2:
			color="green"
			anchor=tk.E
		else:
			color="red"
			anchor=tk.W
		w=tk.Label(self.chatarea,text=txt,anchor=anchor,width=40,fg=color,bg="black")
		w.grid(row=len(self.labellist))
		self.labellist.append(w)
		return "break"	

	def __init2__(self,root):
		frame=tk.Frame(root)
		frame.pack(expand=True)

		chatbox=tk.LabelFrame(frame,text="Chat",padx=5,pady=5)
		chatbox.pack(side=tk.TOP,expand=True)

		chatarea=tk.Frame(chatbox,width=200,height=200)
		chatarea.pack(side=tk.TOP)
		chatarea.pack_propagate(0)

		labellist=[]
		w=tk.Label(chatarea,text="Hi",anchor=tk.W)
		w.pack(side=tk.TOP)
		labellist.append(w)
		w=tk.Label(chatarea,text="Hella %s %s"%(str(labellist[0]["height"]),str(labellist[0]["width"])),anchor=tk.E)
		w.pack(side=tk.TOP)
		labellist.append(w)

		chattext=tk.Frame(chatbox)
		chattext.pack(side=tk.BOTTOM)
		
		btn=tk.Button(frame,text="read",fg="red")
		btn.pack(side=tk.BOTTOM)
		root.update()

if __name__=="__main__":
	root=tk.Tk()
	root.minsize(300,300)
	gui=guified(root)
	root.mainloop()
