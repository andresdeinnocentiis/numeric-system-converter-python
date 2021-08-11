

""""
#####################################################################
==================== NUMERIC SYSTEM CONVERTER =======================
#####################################################################

******************** by @andresdeinnocentiis ************************
"""

import tkinter
from tkinter import IntVar, LabelFrame, PhotoImage, StringVar, Tk, Variable, ttk
from tkinter.constants import E, END, HORIZONTAL, N, S, VERTICAL, W, X, Y
from colorama import Fore



class NumSys_Converter():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Numeric System Converter")
        self.root.iconbitmap("icono.ico")
        self.root.geometry("448x398")
        self.root.resizable(width=False,height=False)
        self.root.configure(background="white")
        self.estilo1 = ttk.Style()
        self.estilo1.configure('TLabelframe', background='white')
        self.estilo2 = ttk.Style()
        
        self.img_exit_btn = PhotoImage(file="exit1.png")  
        self.img_rec_btn = PhotoImage(file="reciclar.png")
        self.img_limp_btn = PhotoImage(file="limpiar.png")
        self.img_conv_btn = PhotoImage(file="convertir.png")
        
        
        self.estilo2.configure("TButton", background="lightblue")
        self.estilo3 = ttk.Style()
        self.estilo3.configure("TLabelframe.Label",background="white")
        self.estilo4 = ttk.Style()
        self.estilo4.configure("TMenubutton",background="white")
        self.estilo5 = ttk.Style()
        self.estilo5.configure("TSeparator",background ="lightblue")
        
  
        self.numresult = ""
        self.baseresult = ""
        
        self.num_frame = ttk.LabelFrame(self.root, text="Number: ",style='TLabelframe')
        self.num_entry = ttk.Entry(self.num_frame, width=32,background="white")
        self.empty1 = ttk.Label(self.root, background="white")
        
        self.base_frame = ttk.Labelframe(self.root, text="Base: ",style='TLabelframe')
        self.base_entry = ttk.Entry(self.base_frame, width=5,background="white")
        
        self.convert_frame = ttk.LabelFrame(self.root, text="Convert to base: ")
        self.convert_options = ["BINARY","3","4","5","6","7","8","9","DECIMAL","11","12","13","14","15","HEXADECIMAL"]
        self.value = StringVar(self.root)
        self.convert_menu = ttk.OptionMenu(self.convert_frame,self.value,self.convert_options[8], *self.convert_options)
        
        self.btn_convert = ttk.Button(self.root, image=self.img_conv_btn, command=self.convert)
        # self.btn_convert = ttk.Button(self.root, text="Convert", command=self.convert)
        self.btn_clear = ttk.Button(self.root, image=self.img_limp_btn, command=self.clear)
        # self.btn_clear = ttk.Button(self.root, text="Clear", command=self.clear)
        
        self.sep0 = ttk.Separator(self.root, orient = HORIZONTAL)
        
        self.result_frame = ttk.LabelFrame(self.root, text="Result")
        self.result_number = ttk.LabelFrame(self.result_frame, width=25,text="Number")
        self.result = ttk.Label(self.result_number, text=self.numresult, width=25, wraplength=150,background="white")
        
        self.empty2 = ttk.Label(self.result_frame,background="white")
        self.result_base = ttk.LabelFrame(self.result_frame, width=5, text="Base")
        self.baseres = ttk.Label(self.result_base, text="",background="white")#self.convert_menu.get(self.convert_menu.curselection()))
        
        self.sep1 = ttk.Separator(self.root, orient = HORIZONTAL)
        
        self.btn_recycle = ttk.Button(self.root, image=self.img_rec_btn, command=self.recycle)
        # self.btn_recycle = ttk.Button(self.root, text="Recycle", command=self.recycle)
        
        self.sep2 = ttk.Separator(self.root, orient = VERTICAL)
        
        # self.exit = ttk.Button(self.root, image=self.img_exit_btn,command=quit)
        self.exit = ttk.Button(self.root, text="\n\nE\n\nX\n\n I\n\nT\n\n", command=quit)
        
        
        #################################################
        ############### PLACING ON GRID: ################
        #################################################
        
        self.num_frame.grid(row=0,column=0,padx=5, pady=5, rowspan=2,sticky=(N+S+W+E))
        self.num_entry.grid(row=0,column=0,rowspan=2,padx=5,sticky=(W+E))
        self.empty1.grid(row=0,column=1, columnspan=2,padx=5, pady=5)
        
        self.base_frame.grid(row=1,column=1,padx=5, pady=5) 
        self.base_entry.grid(row=0,column=0,padx=5, pady=5) 
        self.empty1.grid(row=0,column=1, columnspan=2,padx=5, pady=5, sticky=(W+E))
        
        self.convert_frame.grid(row=2,column=0, columnspan=2,padx=5, pady=5, sticky=(W+E))
        self.convert_menu.grid(row=0,column=0,padx=5, pady=5, sticky=(W+E)) 
        
        self.btn_convert.grid(row=3,column=0,padx=5, sticky=(W+E)) 
        # self.btn_convert.grid(row=3,column=0,padx=5, pady=5, sticky=(W+E)) 
        
        self.btn_clear.grid(row=3,column=1,padx=5,sticky=E)
        # self.btn_clear.grid(row=3,column=1,padx=5, pady=5, sticky=(W+E))
        
        self.sep0.grid(row=4,column=0, columnspan=2,padx=5, pady=5, sticky=(W+E))
        
        self.result_frame.grid(row=5,column=0,columnspan=2,padx=5, pady=5, sticky=(W+E))   
        self.result_number.grid(row=0,column=0,rowspan=2,padx=5, pady=5, sticky=(W+E)) 
        
        self.result.grid(row=0,column=0,padx=5, pady=5,rowspan=2,sticky=(N+S)) 
        self.empty2.grid(row=0,column=1, columnspan=2,padx=5, pady=5)
        self.result_base.grid(row=1,column=1,padx=5, pady=5, sticky=(W+E))
        self.baseres.grid(row=0,column=0,padx=5, pady=5) 
        
        self.sep1.grid(row=6,column=0,columnspan=2,padx=5, pady=5, sticky=(W+E)) 
        
        self.btn_recycle.grid(row=7,column=0,columnspan=2,padx=10, pady=5, sticky=(W+E))
        
        self.sep2.grid(row=0,column=3,rowspan=8,padx=5, pady=5,sticky=(N+S))
        
        self.exit.grid(row=0,column=4,rowspan=8,padx=5, pady=5,sticky=(N+S))
        
        
        
    #################################################
    ################## FUNCTIONS: ###################
    #################################################   
        
        
    def convert(self):
        num = self.num_entry.get().upper()    
        curr_base = self.base_entry.get()
        base = ""
        for i in curr_base:
            base += i
        new_base = int(base)   
        full_num = []
        for n in num:
            full_num.append(n)
        print("FULL NUM: ", full_num)
        convert_to = self.value.get()
        dic_convert_to = {"BINARY":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"DECIMAL":10,"11":11,"12":12,"13":13,"14":14,"15":15,"HEXADECIMAL":16}
        num_list = []
        dec_list = []
        counter = 0
        final = 0
        final_dec = 0
        result = ""
        hex_dic = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
        hex_dic_inverted = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        residue_list = []
        
        #######################################################################################################################        
        ################## ACA SE REALIZA LA CONVERSION PARA NUMEROS ENTEROS: #################################################
        #######################################################################################################################
        
        if "," not in full_num and "." not in full_num:
            if convert_to != "DECIMAL" and new_base != 10:

                for n in num:
                    counter += 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**(len(num)-counter))
                        num_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**(len(num)-counter))
                        num_list.append(x)
        
                for number in num_list:
                    final += int(number)
                    result = final
                    
                base_convert = dic_convert_to[convert_to]  
                residue_list = []
                residue = int(result%base_convert)
                residue_list.insert(0,residue)
                while result >= base_convert:
                    
                    result = result//base_convert
                    residue = int(result%base_convert)
                    residue_list.insert(0,residue)
                    
                residue_list.insert(0,result)
                final_result = ""
                residue_list.remove(residue_list[0])

                for n in residue_list:
                    if n < 10:
                        final_result += str(n)
                    else:
                        num_hex = hex_dic_inverted[n] 
                        final_result += num_hex
                        
                self.numresult = final_result
                self.baseresult = base_convert
                self.result.config(text=self.numresult)   
                self.baseres.config(text=self.baseresult)
            
            elif convert_to == "DECIMAL":
                for n in num:
                    counter += 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        
                        x = new*(new_base**(len(num)-counter))
                        num_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**(len(num)-counter))
                        num_list.append(x)
                        print(num_list)
                for number in num_list:
                    final += int(number)
                    result = final       

                self.numresult = result
                self.baseresult = "10"
                self.result.config(text=self.numresult)   
                self.baseres.config(text=self.baseresult)
            
            elif new_base == 10 and convert_to != "DECIMAL":
                for n in num:
                    num_list.append(n)
                final1 = ""
                for number in num_list:
                    final1 += str(number)
                    result = int(final1)
                
                print("NUM LIST: ", num_list)    
                base_convert = dic_convert_to[convert_to]  
                residue_list = []
                residue = int(result%base_convert)
                residue_list.insert(0,residue)
                print("RESULT 1:",result)
                while result >= base_convert:
                    
                    result = result//base_convert
                    print("PREV. RESULT: ", result)
                    residue = int(result%base_convert)
                    print(f"PREV. RESIDUE of {result}/{base_convert}: ", residue)
                    residue_list.insert(0,residue)
                    print("PREV. RESIDUE LIST: ", residue_list)
                    
                residue_list.insert(0,result)
                final_result = ""
                residue_list.remove(residue_list[0])
                print("RESIDUE LIST: ", residue_list)
                for n in residue_list:
                    if n < 10:
                        final_result += str(n)
                    else:
                        num_hex = hex_dic_inverted[n] 
                        final_result += num_hex
                        
                self.numresult = final_result
                self.baseresult = base_convert
                self.result.config(text=self.numresult)   
                self.baseres.config(text=self.baseresult)
                
        #######################################################################################################################        
        ################ ACA SE REALIZA LA CONVERSION PARA NUMEROS DECIMALES: #################################################
        #######################################################################################################################
        else:
            if "." in full_num:
                decimal = num.split(".")
            elif "," in full_num:
                decimal = num.split(",")
            print("DECIMAL: ", decimal)
            first_part = str(decimal[0])
            dec_part = str(decimal[1])
            print("FIRST PART: ", first_part)
            print("DEC PART: ", dec_part)
            
            #########################################################################################################
            ########### DE BASE DISTINTA DE 10 A OTRA BASE DISTINTA DE 10 ###########################################
            #########################################################################################################
            
            if convert_to != "DECIMAL" and new_base != 10:
                #PRIMERO CONVIERTO A DECIMAL LA PARTE ENTERA:  
                for n in first_part:
                    counter += 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**(len(first_part)-counter))
                        num_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**(len(first_part)-counter))
                        num_list.append(x)
        
                for number in num_list:
                    final += int(number)
                    result = final
                print("NEW RESULT DEC: ", result)  #RESULTADO PARTE ENTERA  
                
                #SEGUNDO, CONVIERTO LA BASE DECIMAL A LA BASE FINAL (LA PARTE ENTERA):
                    
                base_convert = dic_convert_to[convert_to]  
                residue_list = []
                residue = int(result%base_convert)
                residue_list.insert(0,residue)
                while result >= base_convert:
                    
                    result = result//base_convert
                    residue = int(result%base_convert)
                    residue_list.insert(0,residue)
                    
                residue_list.insert(0,result)
                final_result = ""
                residue_list.remove(residue_list[0])
                print("FINAL RESULT TO DEC: ", result) 
                print("FINAL RESIDUE TO DEC: ", residue_list) 
                for n in residue_list:
                    if n < 10:
                        final_result += str(n)
                    else:
                        num_hex = hex_dic_inverted[n] 
                        final_result += num_hex
                
                #TERCERO CONVIERTO A DECIMAL LA PARTE FRACCIONAL:
                  
                counter = 0
                for n in dec_part:
                    counter -= 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**counter)
                        dec_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**counter)
                        dec_list.append(x)
                print("LISTA DE PARTE DECIMAL: ", dec_list)
                for number in dec_list:
                    print("NUMBER DEC: ", number)
                    final_dec += float(number)
                print("SUMA DE LISTA DECIMAL: ", final_dec)
                end = False
                first_part2 = []
                while not end:
                    
                    final_dec = str(final_dec).split(".")
                    print("FINAL DEC: ", final_dec) #PARTE DECIMAL BASE 10
                    
                    if int(final_dec[0]) in hex_dic_inverted:
                        final_dec[0] = hex_dic_inverted[int(final_dec[0])]
                        first_part2.append(str(final_dec[0]))
                        print("FINAL DEC ERROR: ", final_dec[0])
                    else:
                        first_part2.append(str(final_dec[0]))
                    print("DEC PART ERROR: ", dec_part)
                    if len(first_part2)>20:
                        end = True
                    if final_dec[1]:
                        dec_part = final_dec[1]
                    str_final_dec = "0."+str(dec_part)
                    print("PARTE SI DECIMAL DE DECIMALES: ", str_final_dec)
                    final_dec = float(str_final_dec)*base_convert
                    print("MULTIPLICADO x 16: ", final_dec)
                    print("PARTE NO DECIMAL DE DECIMALES: ", first_part2)
                    str_first_part2 = ""
                    for n in first_part2[1:]:
                        str_first_part2 += n
                    
                    result_dec = "."+str(str_first_part2)
                    print("RESULT DEC: ",result_dec)
                
                
                        
                self.numresult = str(final_result)+str(result_dec)
                self.baseresult = base_convert
                self.result.config(text="{:.26s}".format(self.numresult))  
                self.baseres.config(text=self.baseresult)
            
            #########################################################################################################
            ########### DE OTRA BASE A BASE 10 ######################################################################
            #########################################################################################################
            
            elif convert_to == "DECIMAL":
                for n in first_part:
                    counter += 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**(len(first_part)-counter))
                        num_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**(len(first_part)-counter))
                        num_list.append(x)
        
                for number in num_list:
                    final += int(number)
                    result = final #RESULTADO PARTE ENTERA
                print("NEW RESULT DEC: ", result) 
                
                counter = 0
                for n in dec_part:
                    counter -= 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**counter)
                        dec_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**counter)
                        dec_list.append(x)
                print("LISTA DE PARTE DECIMAL: ", dec_list)
                for number in dec_list:
                    print("NUMBER DEC: ", number)
                    final_dec += float(number)
                print("SUMA DE LISTA DECIMAL: ", final_dec)
                

                self.numresult = result+final_dec
                self.baseresult = "10"
                self.result.config(text=self.numresult)   
                self.baseres.config(text=self.baseresult)
            
            #########################################################################################################
            ########### DE BASE 10 A OTRA BASE ######################################################################
            #########################################################################################################
            
            elif new_base == 10 and convert_to != "DECIMAL":
                
                #PRIMERO CONVIERTO LA PARTE ENTERA A LA NUEVA BASE:

                result = int(first_part)
                
                print("RESULT PARTE ENTERA: ", result)    
                base_convert = dic_convert_to[convert_to]  
                residue_list = []
                residue = int(result%base_convert)
                residue_list.insert(0,residue)
                print("RESULT 1:",result)
                while result >= base_convert:
                    
                    result = result//base_convert
                    print("PREV. RESULT: ", result)
                    residue = int(result%base_convert)
                    print(f"PREV. RESIDUE of {result}/{base_convert}: ", residue)
                    residue_list.insert(0,residue)
                    print("PREV. RESIDUE LIST: ", residue_list)
                    
                residue_list.insert(0,result)
                final_result = ""
                residue_list.remove(residue_list[0])
                print("RESIDUE LIST PARTE ENTERA: ", residue_list)
                for n in residue_list:
                    if n < 10:
                        final_result += str(n)
                    else:
                        num_hex = hex_dic_inverted[n] 
                        final_result += num_hex
                    print("FINAL RESULT PARTE ENTERA: ", final_result)
                    
                #DESPUES CONVIERTO LA PARTE FRACCIONAL A LA NUEVA BASE:    
                
                counter = 0
                for n in dec_part:
                    counter -= 1
                    if n not in hex_dic.keys(): 
                        i = n
                        new = int(i)
                        x = new*(new_base**counter)
                        dec_list.append(x)
                    else:
                        nr = hex_dic[n]
                        x = nr*(new_base**counter)
                        dec_list.append(x)
                print("LISTA DE PARTE DECIMAL: ", dec_list)
                for number in dec_list:
                    print("NUMBER DEC: ", number)
                    final_dec += float(number)
                print("SUMA DE LISTA DECIMAL: ", final_dec)
                end = False
                first_part2 = []
                while not end:
                    
                    final_dec = str(final_dec).split(".")
                    print("FINAL DEC: ", final_dec) #PARTE DECIMAL BASE 10
                    
                    if int(final_dec[0]) in hex_dic_inverted:
                        final_dec[0] = hex_dic_inverted[int(final_dec[0])]
                        first_part2.append(str(final_dec[0]))
                        print("FINAL DEC ERROR: ", final_dec[0])
                    else:
                        first_part2.append(str(final_dec[0]))
                    print("DEC PART ERROR: ", dec_part)
                    if len(first_part2)>20:
                        end = True
                    if final_dec[1]:
                        dec_part = final_dec[1]
                    str_final_dec = "0."+str(dec_part)
                    print("PARTE SI DECIMAL DE DECIMALES: ", str_final_dec)
                    final_dec = float(str_final_dec)*base_convert
                    print("MULTIPLICADO x 16: ", final_dec)
                    print("PARTE NO DECIMAL DE DECIMALES: ", first_part2)
                    str_first_part2 = ""
                    for n in first_part2[1:]:
                        str_first_part2 += n
                    
                    result_dec = "."+str(str_first_part2)
                    print("RESULT DEC: ",result_dec)
                

                self.numresult = str(final_result)+result_dec
                self.baseresult = base_convert
                self.result.config(text=self.numresult)   
                self.baseres.config(text=self.baseresult)
            
                   
    
    def clear(self):
        self.numresult = ""
        self.baseresult = ""
        self.num_entry.delete(0, END)
        self.base_entry.delete(0, END) 
        self.result.config(text=self.numresult)   
        self.baseres.config(text=self.baseresult) 
        
        
            
    def recycle(self):
        num = self.numresult
        base = self.baseresult
        self.num_entry.delete(0, END)
        self.base_entry.delete(0, END)
        self.num_entry.insert(0,num)
        self.base_entry.insert(0,base)
        self.result.config(text="")   
        self.baseres.config(text="")   
        
        
    def execute(self):
        self.root.mainloop()




def main():
    app = NumSys_Converter()
    app.execute()


main()
    