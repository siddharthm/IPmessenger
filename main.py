import ssocket
import Tkinter as tk

class guified:
	def __init__(self,root):
		frame=tk.Frame(root)
		frame.grid()
		self.wd=40
	
		# Tab area
		
		tab_area=tk.Frame(frame)
		tab_area.grid(row=0,sticky="n")
		lbl=tk.Label(tab_area,text="Heya this is text")
		lbl.grid()
		

		#Scrollable chat box

		self.canvas_frame=tk.Canvas(frame)
		self.canvas_frame.grid(row=1,column=0,sticky=tk.W)

		self.canvas=tk.Canvas(self.canvas_frame,height=200,width=325)

		self.chatarea=tk.Frame(self.canvas)
	
		self.vsb=tk.Scrollbar(self.canvas_frame,orient="vertical",command=self.canvas.yview)

		self.canvas.configure(yscrollcommand=self.vsb.set)
		
		self.vsb.grid(column=1,row=0,sticky="nsew")
		self.canvas.grid(column=0,row=0)
		self.canvas.create_window((0,0),window=self.chatarea,anchor="nw",tags=self.chatarea)
		self.chatarea.bind("<Configure>", self.OnFrameConfigure)


		self.labellist=[]
		
		# Chat input box

		chattext=tk.Frame(frame)
		chattext.grid(column=0,row=2,sticky=tk.W)
	
		wd_btn=4
		textBox=tk.Text(chattext,height=2,width=self.wd)
		textBox.grid(column=0,row=0)
		textBox.bind("<Return>",lambda event:self.btnpress(event,textBox))

		btn=tk.Button(chattext,text="Send",width=wd_btn)
		btn.grid(column=1,row=0)
		btn.bind("<Button-1>",lambda event:self.btnpress(event,textBox))

		# Sidebar

		sidebox=tk.Frame(frame)
		sidebox.grid(column=1,row=1,sticky=tk.W)

		label1=tk.Label(sidebox,text="This text is over here",width=self.wd)
		label1.grid()

	def btnpress(self,event,textBox):
		txt=textBox.get(0.0,tk.INSERT)
		textBox.delete(0.0,tk.END)
		if txt=="":
			return 'break'
		if len(self.labellist)%2:
			color="green"
			anchor=tk.E
			jf=tk.RIGHT
		else:
			color="red"
			anchor=tk.W
			jf=tk.LEFT
		w=tk.Label(self.chatarea,text=txt,anchor=anchor,width=self.wd,wraplength=300,fg=color,bg="black",justify=jf,padx=2)
		w.grid(row=len(self.labellist))
		self.labellist.append(w)
		self.chatarea.update_idletasks()
		if len(self.labellist)>5:
			self.canvas.yview_moveto(1.0)
		return "break"	

	def OnFrameConfigure(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__=="__main__":
	root=tk.Tk()
	root.minsize(300,300)
	gui=guified(root)
	
	root.mainloop()
