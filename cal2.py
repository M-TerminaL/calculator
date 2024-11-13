#-----------Library---------------------------------------------------------------------------------------------------
from     tkinter   import  *
import   math
from     tkinter   import  messagebox
import   random    as      rnd
#-----------Variable---------------------------------------------------------------------------------------------------
switch = None
memory = 0
#-----------Menubar Functions------------------------------------------------------------------------------------------------
def exit_():
    result = messagebox.askyesno("Calculator", 'confirm if you want to exit')
    if result > 0:
        win.destroy()
def standard():
    win1.state('normal')
    win .state('withdrawn')
def scientific():
    win .state('normal')
    win1.state('withdrawn')
def aboutus():
    messagebox.showinfo('Mr.TerminaL', 'سازنده برنامه : عليرضا بابايي ')
def version():
    messagebox.showinfo('Calculator', 'Version : 0.0.1')
def help_():
    messagebox.showinfo('Help', 'ميتوانيد از دو حالت ماشين حساب مهندسي و ساده در قسمت منو استفاده کنيد')
#-----------Backend functions in scientific---------------------------------------------------------------------------   
def btn_1():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '1')
def btn_2():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '2')
def btn_3():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '3')
def btn_4():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '4')
def btn_5():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '5')
def btn_6():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '6')
def btn_7():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '7')
def btn_8():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '8')
def btn_9():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '9')
def btn_0():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.insert(END, '0')
def btn_Taqsim():
    txt_disply.insert(END, '/')
def btn_zarb():
    txt_disply.insert(END, '*')
def btn_subtract():
    txt_disply.insert(END, '-')
def btn_plus(): 
    index = len(txt_disply.get())
    txt_disply.insert(index, '+')
def btn_eval():
    try:
        result = eval(txt_disply.get())
        result_disply.delete(0, END)
        result_disply.insert(0, str(result))
    except Exception:
        messagebox.showerror('Invalid Values', 'Please Check Operator And Try Again')
def btn_parantez_baz():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    index = len(txt_disply.get())
    txt_disply.insert(index, '(')
def btn_parantez_baste():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    index = len(txt_disply.get())
    txt_disply.insert(index, ')')
def btn_MC():
    global memory
    memory = 0
def btn_Mplus():
    try:
        global memory
        memory = memory + float(eval(txt_disply.get()))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Your Operator')
def btn_Mminus():
    try:
        global memory
        memory = memory - float(eval(txt_disply.get()))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Your Operator')
def btn_MR():
    txt_disply.delete(0, END)
    txt_disply.insert(0, str(memory))
def btn_AC():
    txt_disply.delete(0, END)
    result_disply.delete(0, END)
    txt_disply.insert(0, '0')
def btn_PlusMinus():
    if txt_disply.get() == '0':
        messagebox.showerror('Error', 'The number zero is neutral')
        return
    index = len(txt_disply.get())
    txt_disply.insert(0, '-')
def btn_Darsad():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    try:
        result = float(eval(txt_disply.get())) * 0.01
        txt_disply   .delete(0, END)
        txt_disply   .insert(END, str(result))
        result_disply.insert(0,   str(result))
    except Exception:
        messagebox.showerror('Error' , 'Check your operator')
        txt_disply.insert(0, '0')
def btn_round():
    try:
        answer = float(txt_disply.get())
        res = round(answer)
        result_disply.delete(0, END)
        result_disply.insert(0, str(res))
    except Exception:
        messagebox.showerror('Error', 'Check Your Operator')
def btn_x2():
    index = len(txt_disply.get())
    txt_disply.insert(index, '**2')
def btn_x3():
    index = len(txt_disply.get())
    txt_disply.insert(index, '**3')
def btn_xy():
    index = len(txt_disply.get())
    txt_disply.insert(index, '**')
def btn_ex():
    txt_disply.delete(0, END)
    txt_disply.insert(0, str(math.e) + str('**'))
def btn_10x():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    txt_disply.delete(0, END)
    index = len(txt_disply.get())
    txt_disply.insert(index, str(10) + str('**'))
def btn_1x_om():
    try:
        result = 1 / float(eval(txt_disply.get()))
        result_disply.delete(0, END)
        result_disply.insert(0, str(result))
    except SyntaxError:
        messagebox.showerror('SyntaxError', 'Check Your Operator')
    except ZeroDivisionError:
        #messagebox.showerror('ZeroDivisinError', 'INF value')
        result_disply.insert(0, math.inf)
    except:
        messagebox.showerror('Error', 'Please Check Your Operator')     
def btn_radicalx():
    try:
        result = float(txt_disply.get())
        #txt_disply.delete(0, END)
        result_disply.delete(0, END)
        result_disply.insert(0, str(math.sqrt(result)))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def btn_radicalx3():
    try:
        result = float(txt_disply.get())
        res = math.sqrt(result) ** 1/3
        #txt_disply.delete(0, END)
        result_disply.delete(0, END)
        result_disply.insert(0, res)
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def btn_radicalx4():
    try:
        result = float(txt_disply.get())
        res = math.sqrt(result) ** 1/4
        result_disply.delete(0, END)
        result_disply.insert(0, res)
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def btn_ln():
    try:
        result = float(txt_disply.get())
        #txt_disply.delete(0, END)
        result_disply.delete(0, END)
        result_disply.insert(0, str(math.log(result)))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def btn_log10():
    try:
        result = float(txt_disply.get())
        #txt_disply.delete(0, END)
        result_disply.delete(0, END)
        result_disply.insert(0, str(math.log10(result)))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def btn_factorial():
    try:
        result = int(txt_disply.get())
        res = math.factorial(result)
        #txt_disply.delete(0, END)
        #txt_disply.insert(0, result)
        result_disply.delete(0, END)
        result_disply.insert(0, str(res))
    except Exception:
        messagebox.showerror('Value Error', 'Value Should be an Integer')
def btn_sin():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            answer = math.sin(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.sin(answer)
            #txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_cos():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            answer = math.cos(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.cos(answer)
            #txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_tan():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            answer = math.tan(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.tan(answer)
            #txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_asin():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            nswer = math.asin(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.asin(answer)
            #txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_acos():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            nswer = math.acos(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.acos(answer)
            txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_atan():
    try:
        answer = float(txt_disply.get())
        if switch is True:
            nswer = math.atan(math.radians(answer))
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
        else:
            answer = math.atan(answer)
            txt_disply.delete(0, END)
            result_disply.delete(0, END)
            result_disply.insert(0, str(answer))
    except Exception:
        messagebox.showerror('Value Error', 'check your operator')
def btn_e():
    #if txt_disply.get() == '0':
        #txt_disply.delete(0, END)
    txt_disply.delete(0, END)
    #result_disply.delete(0, END)
    #index = len(txt_disply.get())
    result_disply.delete(0, END)
    txt_disply.insert(END, str(math.e))
    result_disply.insert(END, str(math.e))
    #result_disply.insert(index, str(math.e))
def btn_back():
    #data = txt_disply.get()
    index = len(txt_disply.get())
    txt_disply.delete(index-1)
    if txt_disply.get() == '':
        txt_disply.insert(0, '0')
def btn_convert():
    global switch
    if switch is None:
        switch = True
        b41['text'] = 'Deg' + str(' ') + str(chr(186))
    else:
        switch = None
        b41['text'] = 'Rad'
def btn_pi():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    index = len(txt_disply.get())
    result_disply.delete(0, END)
    txt_disply.delete(0, END)
    txt_disply.insert(index, str(math.pi))
    result_disply.delete(0, END)
    result_disply.insert(index, str(math.pi))
def btn_rand():
    if txt_disply.get() == '0':
        txt_disply.delete(0, END)
    res = rnd.random()
    txt_disply.delete(0, END)
    txt_disply.insert(0, str(res))
def btn_dotted():
    index = len(txt_disply.get())
    txt_disply.insert(index, '.')
#------- Backend functions in Standard------------------------------------------------------------------------------
def button1():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '1')
def button2():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '2')
def button3():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '3')
def button4():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '4')
def button5():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '5')
def button6():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '6')
def button7():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '7')
def button8():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '8')
def button9():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '9')
def button_zarb():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '*')
def button_jam():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '+')
def button_tafrigh():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '-')
def button_taghsim():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '/')
def button0():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    txt_disply_standard.insert(END, '0')
def buttonEval():
    try:
        result = eval(txt_disply_standard.get())
        result_disply_standard.insert(0, str(result))
    except Exception:
        messagebox.showerror('Value Error', 'Check Your Operator')
def button_darsad():
    if txt_disply_standard.get() == '0':
        txt_disply_standard.delete(0, END)
    try:
        result = float(eval(txt_disply_standard.get())) * 0.01
        txt_disply_standard.delete(0, END)
        txt_disply_standard.insert(END, str(result))
        result_disply_standard.insert(0, str(result))
    except Exception:
        messagebox.showerror('Error' , 'Check your operator')
def button_ce():
    txt_disply_standard.delete(0, END)
    result_disply_standard.delete(0, END)
    txt_disply_standard.insert(0, '0')
def button_c():
    txt_disply_standard.delete(0, END)
    result_disply_standard.delete(0, END)
    txt_disply_standard.insert(0, '0')
def button_back():
    index = len(txt_disply_standard.get())
    txt_disply_standard.delete(index-1)
    if txt_disply_standard.get() == '':
        txt_disply_standard.insert(0, '0')
def button_1x_om():
    try:
        result = 1 / float(eval(txt_disply_standard.get()))
        result_disply_standard.delete(0, END)
        result_disply_standard.insert(0, str(result))
    except SyntaxError:
        messagebox.showerror('SyntaxError', 'Check Your Operator')
    except ZeroDivisionError:
        #messagebox.showerror('ZeroDivisinError', 'INF value')
        result_disply_standard.insert(0, math.inf)
    except:
        messagebox.showerror('Error', 'Please Check Your Operator')
def button_x2():
    index = len(txt_disply_standard.get())
    txt_disply_standard.insert(index, '**2')
def button_2radicalx():
    try:
        result = float(txt_disply_standard.get())
        #txt_disply_standard.delete(0, END)
        result_disply_standard.delete(0, END)
        result_disply_standard.insert(0, str(math.sqrt(result)))
    except Exception:
        messagebox.showerror('Value Error', 'Please Check Operator And Try Again')
def button_plusminus():
    if txt_disply_standard.get() == '0':
        messagebox.showerror('Error', 'The number zero is neutral')
        return
    index = len(txt_disply_standard.get())
    txt_disply_standard.insert(0, '-')    
#------- Scientific functions for bind------------------------------------------------------------------------------------
def func1(event=None):
    b1['bg'] = '#FF69B4'
    b1['fg'] = 'black'
def func1_(event=None):
    b1['bg'] = '#333333'
    b1['fg'] = 'white'
def func2(event=None):
    b2['bg'] = '#FF69B4'
    b2['fg'] = 'black'
def func2_(event=None):
    b2['bg'] = '#333333'
    b2['fg'] = 'white'
def func3(event=None):
    b3['bg'] = '#FF69B4'
    b3['fg'] = 'black'
def func3_(event=None):
    b3['bg'] = '#333333'
    b3['fg'] = 'white'
def func4(event=None):
    b4['bg'] = '#FF69B4'
    b4['fg'] = 'black'
def func4_(event=None):
    b4['bg'] = '#333333'
    b4['fg'] = 'white'
def func5(event=None):
    b5['bg'] = '#FF69B4'
    b5['fg'] = 'black'
def func5_(event=None):
    b5['bg'] = '#333333'
    b5['fg'] = 'white'
def func6(event=None):
    b6['bg'] = '#FF69B4'
    b6['fg'] = 'black'
def func6_(event=None):
    b6['bg'] = '#333333'
    b6['fg'] = 'white'
def func7(event=None):
    b7['bg'] = '#FF69B4'
    b7['fg'] = 'black'
def func7_(event=None):
    b7['bg'] = '#333333'
    b7['fg'] = 'white'
def func8(event=None):
    b8['bg'] = '#FF69B4'
    b8['fg'] = 'black'
def func8_(event=None):
    b8['bg'] = '#333333'
    b8['fg'] = 'white'
def func9(event=None):
    b9['bg'] = '#FF69B4'
    b9['fg'] = 'black'
def func9_(event=None):
    b9['bg'] = '#333333'
    b9['fg'] = 'white'
def func10(event=None):
    b10['bg'] = '#FF69B4'
    b10['fg'] = 'black'
def func10_(event=None):
    b10['bg'] = '#333333'
    b10['fg'] = 'white'
def func11(event=None):
    b11['bg'] = '#FF69B4'
    b11['fg'] = 'black'
def func11_(event=None):
    b11['bg'] = '#333333'
    b11['fg'] = 'white'
def func12(event=None):
    b12['bg'] = '#FF69B4'
    b12['fg'] = 'black'
def func12_(event=None):
    b12['bg'] = '#333333'
    b12['fg'] = 'white'
def func13(event=None):
    b13['bg'] = '#FF69B4'
    b13['fg'] = 'black'
def func13_(event=None):
    b13['bg'] = '#333333'
    b13['fg'] = 'white'
def func14(event=None):
    b14['bg'] = '#FF69B4'
    b14['fg'] = 'black'
def func14_(event=None):
    b14['bg'] = '#333333'
    b14['fg'] = 'white'
def func15(event=None):
    b15['bg'] = '#FF69B4'
    b15['fg'] = 'black'
def func15_(event=None):
    b15['bg'] = '#333333'
    b15['fg'] = 'white'
def func16(event=None):
    b16['bg'] = '#FF69B4'
    b16['fg'] = 'black'
def func16_(event=None):
    b16['bg'] = '#333333'
    b16['fg'] = 'white'
def func17(event=None):
    b17['bg'] = '#FF69B4'
    b17['fg'] = 'black'
def func17_(event=None):
    b17['bg'] = '#333333'
    b17['fg'] = 'white'
def func18(event=None):
    b18['bg'] = '#FF69B4'
    b18['fg'] = 'black'
def func18_(event=None):
    b18['bg'] = '#333333'
    b18['fg'] = 'white'
def func19(event=None):
    b19['bg'] = '#FF69B4'
    b19['fg'] = 'black'
def func19_(event=None):
    b19['bg'] = '#333333'
    b19['fg'] = 'white'
def func20(event=None):
    b20['bg'] = '#FF69B4'
    b20['fg'] = 'black'
def func20_(event=None):
    b20['bg'] = '#333333'
    b20['fg'] = 'white'
def func21(event=None):
    b21['bg'] = '#FF69B4'
    b21['fg'] = 'black'
def func21_(event=None):
    b21['bg'] = '#333333'
    b21['fg'] = 'white'
def func22(event=None):
    b22['bg'] = '#FF69B4'
    b22['fg'] = 'black'
def func22_(event=None):
    b22['bg'] = '#333333'
    b22['fg'] = 'white'
def func23(event=None):
    b23['bg'] = '#FF69B4'
    b23['fg'] = 'black'
def func23_(event=None):
    b23['bg'] = '#333333'
    b23['fg'] = 'white'
def func24(event=None):
    b24['bg'] = '#FF69B4'
    b24['fg'] = 'black'
def func24_(event=None):
    b24['bg'] = '#333333'
    b24['fg'] = 'white'
def func25(event=None):
    b25['bg'] = '#FF69B4'
    b25['fg'] = 'black'
def func25_(event=None):
    b25['bg'] = '#333333'
    b25['fg'] = 'white'
def func26(event=None):
    b26['bg'] = '#FF69B4'
    b26['fg'] = 'black'
def func26_(event=None):
    b26['bg'] = '#333333'
    b26['fg'] = 'white'
def func27(event=None):
    b27['bg'] = '#FF69B4'
    b27['fg'] = 'black'
def func27_(event=None):
    b27['bg'] = '#333333'
    b27['fg'] = 'white'
def func28(event=None):
    b28['bg'] = '#FF69B4'
    b28['fg'] = 'black'
def func28_(event=None):
    b28['bg'] = '#333333'
    b28['fg'] = 'white'
def func29(event=None):
    b29['bg'] = '#FF69B4'
    b29['fg'] = 'black'
def func29_(event=None):
    b29['bg'] = '#333333'
    b29['fg'] = 'white'
def func30(event=None):
    b30['bg'] = '#FF69B4'
    b30['fg'] = 'black'
def func30_(event=None):
    b30['bg'] = '#333333'
    b30['fg'] = 'white'
def func31(event=None):
    b31['bg'] = '#FF69B4'
    b31['fg'] = 'black'
def func31_(event=None):
    b31['bg'] = '#333333'
    b31['fg'] = 'white'
def func32(event=None):
    b32['bg'] = '#FF69B4'
    b32['fg'] = 'black'
def func32_(event=None):
    b32['bg'] = '#333333'
    b32['fg'] = 'white'
def func33(event=None):
    b33['bg'] = '#FF69B4'
    b33['fg'] = 'black'
def func33_(event=None):
    b33['bg'] = '#333333'
    b33['fg'] = 'white'
def func34(event=None):
    b34['bg'] = '#FF69B4'
    b34['fg'] = 'black'
def func34_(event=None):
    b34['bg'] = '#333333'
    b34['fg'] = 'white'
def func35(event=None):
    b35['bg'] = '#FF69B4'
    b35['fg'] = 'black'
def func35_(event=None):
    b35['bg'] = '#333333'
    b35['fg'] = 'white'
def func36(event=None):
    b36['bg'] = '#FF69B4'
    b36['fg'] = 'black'
def func36_(event=None):
    b36['bg'] = '#333333'
    b36['fg'] = 'white'
def func37(event=None):
    b37['bg'] = '#FF69B4'
    b37['fg'] = 'black'
def func37_(event=None):
    b37['bg'] = '#333333'
    b37['fg'] = 'white'
def func38(event=None):
    b38['bg'] = '#FF69B4'
    b38['fg'] = 'black'
def func38_(event=None):
    b38['bg'] = '#333333'
    b38['fg'] = 'white'
def func39(event=None):
    b39['bg'] = '#FF69B4'
    b39['fg'] = 'black'
def func39_(event=None):
    b39['bg'] = '#333333'
    b39['fg'] = 'white'
def func40(event=None):
    b40['bg'] = '#FF69B4'
    b40['fg'] = 'black'
def func40_(event=None):
    b40['bg'] = '#333333'
    b40['fg'] = 'white'
def func41(event=None):
    b41['bg'] = '#FF69B4'
    b41['fg'] = 'black'
def func41_(event=None):
    b41['bg'] = 'DodgerBlue2'
    b41['fg'] = 'white'
def func42(event=None):
    b42['bg'] = '#FF69B4'
    b42['fg'] = 'black'
def func42_(event=None):
    b42['bg'] = '#333333'
    b42['fg'] = 'white'
def func43(event=None):
    b43['bg'] = '#FF69B4'
    b43['fg'] = 'black'
def func43_(event=None):
    b43['bg'] = '#333333'
    b43['fg'] = 'white'
def func44(event=None):
    b44['bg'] = '#FF69B4'
    b44['fg'] = 'black'
def func44_(event=None):
    b44['bg'] = '#333333'
    b44['fg'] = 'white'
def func45(event=None):
    b45['bg'] = '#FF69B4'
    b45['fg'] = 'black'
def func45_(event=None):
    b45['bg'] = '#333333'
    b45['fg'] = 'white'
def func46(event=None):
    b46['bg'] = '#FF69B4'
    b46['fg'] = 'black'
def func46_(event=None):
    b46['bg'] = '#333333'
    b46['fg'] = 'white'
def func47(event=None):
    b47['bg'] = '#FF69B4'
    b47['fg'] = 'black'
def func47_(event=None):
    b47['bg'] = '#333333'
    b47['fg'] = 'white'
def func48(event=None):
    b48['bg'] = '#FF69B4'
    b48['fg'] = 'black'
def func48_(event=None):
    b48['bg'] = '#333333'
    b48['fg'] = 'white'
def func49(event=None):
    b49['bg'] = '#FF69B4'
    b49['fg'] = 'black'
def func49_(event=None):
    b49['bg'] = 'DodgerBlue2'
    b49['fg'] = 'white'
#----------Standard def for bind--------------------------------------------------------------------------------------
def func_btn1(event=None):
    btn1['bg'] = '#FF69B4'
    btn1['fg'] = 'black'
def func_btn1_(event=None):
    btn1['bg'] = '#333333'
    btn1['fg'] = 'white'
def func_btn2(event=None):
    btn2['bg'] = '#FF69B4'
    btn2['fg'] = 'black'
def func_btn2_(event=None):
    btn2['bg'] = '#333333'
    btn2['fg'] = 'white'
def func_btn3(event=None):
    btn3['bg'] = '#FF69B4'
    btn3['fg'] = 'black'
def func_btn3_(event=None):
    btn3['bg'] = '#333333'
    btn3['fg'] = 'white'
def func_btn4(event=None):
    btn4['bg'] = '#FF69B4'
    btn4['fg'] = 'black'
def func_btn4_(event=None):
    btn4['bg'] = '#333333'
    btn4['fg'] = 'white'
def func_btn5(event=None):
    btn5['bg'] = '#FF69B4'
    btn5['fg'] = 'black'
def func_btn5_(event=None):
    btn5['bg'] = '#333333'
    btn5['fg'] = 'white'
def func_btn6(event=None):
    btn6['bg'] = '#FF69B4'
    btn6['fg'] = 'black'
def func_btn6_(event=None):
    btn6['bg'] = '#333333'
    btn6['fg'] = 'white'
def func_btn7(event=None):
    btn7['bg'] = '#FF69B4'
    btn7['fg'] = 'black'
def func_btn7_(event=None):
    btn7['bg'] = '#333333'
    btn7['fg'] = 'white'
def func_btn8(event=None):
    btn8['bg'] = '#FF69B4'
    btn8['fg'] = 'black'
def func_btn8_(event=None):
    btn8['bg'] = '#333333'
    btn8['fg'] = 'white'
def func_btn9(event=None):
    btn9['bg'] = '#FF69B4'
    btn9['fg'] = 'black'
def func_btn9_(event=None):
    btn9['bg'] = '#333333'
    btn9['fg'] = 'white'
def func_btn10(event=None):
    btn10['bg'] = '#FF69B4'
    btn10['fg'] = 'black'
def func_btn10_(event=None):
    btn10['bg'] = '#333333'
    btn10['fg'] = 'white'
def func_btn11(event=None):
    btn11['bg'] = '#FF69B4'
    btn11['fg'] = 'black'
def func_btn11_(event=None):
    btn11['bg'] = '#333333'
    btn11['fg'] = 'white'
def func_btn12(event=None):
    btn12['bg'] = '#FF69B4'
    btn12['fg'] = 'black'
def func_btn12_(event=None):
    btn12['bg'] = '#333333'
    btn12['fg'] = 'white'
def func_btn13(event=None):
    btn13['bg'] = '#FF69B4'
    btn13['fg'] = 'black'
def func_btn13_(event=None):
    btn13['bg'] = '#333333'
    btn13['fg'] = 'white'
def func_btn14(event=None):
    btn14['bg'] = '#FF69B4'
    btn14['fg'] = 'black'
def func_btn14_(event=None):
    btn14['bg'] = '#333333'
    btn14['fg'] = 'white'
def func_btn15(event=None):
    btn15['bg'] = '#FF69B4'
    btn15['fg'] = 'black'
def func_btn15_(event=None):
    btn15['bg'] = '#333333'
    btn15['fg'] = 'white'
def func_btn16(event=None):
    btn16['bg'] = '#FF69B4'
    btn16['fg'] = 'black'
def func_btn16_(event=None):
    btn16['bg'] = '#333333'
    btn16['fg'] = 'white'
def func_btn17(event=None):
    btn17['bg'] = '#FF69B4'
    btn17['fg'] = 'black'
def func_btn17_(event=None):
    btn17['bg'] = '#333333'
    btn17['fg'] = 'white'
def func_btn18(event=None):
    btn18['bg'] = '#FF69B4'
    btn18['fg'] = 'black'
def func_btn18_(event=None):
    btn18['bg'] = '#333333'
    btn18['fg'] = 'white'
def func_btn19(event=None):
    btn19['bg'] = '#FF69B4'
    btn19['fg'] = 'black'
def func_btn19_(event=None):
    btn19['bg'] = '#333333'
    btn19['fg'] = 'white'
def func_btn20(event=None):
    btn20['bg'] = '#FF69B4'
    btn20['fg'] = 'black'
def func_btn20_(event=None):
    btn20['bg'] = '#333333'
    btn20['fg'] = 'white'
def func_btn21(event=None):
    btn21['bg'] = '#FF69B4'
    btn21['fg'] = 'black'
def func_btn21_(event=None):
    btn21['bg'] = '#333333'
    btn21['fg'] = 'white'
def func_btn22(event=None):
    btn22['bg'] = '#FF69B4'
    btn22['fg'] = 'black'
def func_btn22_(event=None):
    btn22['bg'] = '#333333'
    btn22['fg'] = 'white'
def func_btn23(event=None):
    btn23['bg'] = '#FF69B4'
    btn23['fg'] = 'black'
def func_btn23_(event=None):
    btn23['bg'] = '#333333'
    btn23['fg'] = 'white'
def func_btn24(event=None):
    btn24['bg'] = '#FF69B4'
    btn24['fg'] = 'black'
def func_btn24_(event=None):
    btn24['bg'] = 'DodgerBlue2'
    btn24['fg'] = 'white'
#--------------main window------------------------------------------------------------------------------------------------------
win = Tk()
win.title('Scientific Calculator')
win.resizable(False, False)
win.iconbitmap('calc_32.ico')
win.geometry('640x366+100+100')

frm1 = Frame(win)
frm1.place(x=0, y=0)

txt_disply = Entry(frm1, width=66, bg='firebrick1', fg='black', font=('arial', 26, 'bold'), bd=0)
txt_disply.grid(row=0, column=0)
txt_disply.insert(0, '0')


result_disply = Entry(frm1, width=66, bg='firebrick1', fg='white', font=('arial', 26, 'bold'), bd=0)
result_disply.grid(row=1, column=0)

frm2 = Frame(win)
frm2.place(x=0, y=86)
#------------TopLevel window---------------------------------------------------------------------------
win1 = Toplevel()
win1.title('Standard Calculator')
win1.geometry('285x494+100+100')
win1.title('Standard')
win1.state('withdrawn')
win1.resizable(False, False)
win1.iconbitmap('calc_32.ico')
frm3 = Frame(win1)
frm3.place(x=0, y=0)

txt_disply_standard = Entry(frm3, width=20, bg='firebrick1',bd = 0, fg='black', font=('arial', 20, 'bold'))
txt_disply_standard.grid(row=0, column=0)
txt_disply_standard.insert(0, '0')

result_disply_standard = Entry(frm3, width=20, bg='firebrick1',bd = 0, fg='white', font=('arial', 20, 'bold'))
result_disply_standard.grid(row=1, column=0)
frm4 = Frame(win1)
frm4.place(x=0, y=68)
#------------Menu Main----------------------------------------------------------------------------------------------------
menubar   = Menu(win)

filemenu  = Menu(menubar, tearoff=0)
menubar .add_cascade(label='File',       menu=filemenu)
filemenu.add_command(label='Standard',   command=standard)
filemenu.add_command(label='Scientific', command=scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit',       command=exit_)

aboutmenu = Menu(menubar, tearoff=0)
menubar  .add_cascade(label='About',    menu=aboutmenu)
aboutmenu.add_command(label='About Us', command=aboutus)
aboutmenu.add_command(label='Version',  command=version)

helpmenu  = Menu(menubar, tearoff=0)
menubar .add_cascade(label='Help',      menu=helpmenu)
helpmenu.add_command(label="View Help", command=help_)

win.config(menu = menubar)
#------------toplevel Menu----------------------------------------------------------------------------------------------------
menubar   = Menu(win1)

filemenu  = Menu(menubar, tearoff=0)
menubar .add_cascade(label='File'      , menu=filemenu)
filemenu.add_command(label='Standard'  , command = standard  )
filemenu.add_command(label='Scientific', command = scientific)
filemenu.add_separator()
filemenu.add_command(label='Exit'      , command = exit_     )

aboutmenu = Menu(menubar, tearoff=0)
menubar  .add_cascade(label='About',     menu=aboutmenu)
aboutmenu.add_command(label='About Us',  command=aboutus)
aboutmenu.add_command(label='Version',   command=version)

helpmenu  = Menu(menubar, tearoff=0)
menubar .add_cascade(label='Help'     ,  menu=helpmenu)
helpmenu.add_command(label="View Help",  command=help_)

win1.config(menu = menubar)
#---------Buttons of Scientific calculator------------------------------------------------------------------------
b1  = Button(frm2, text='(' ,bg='#333333',fg = 'white', font=('tahoma', 12), width=6, height=2,relief="flat", command = btn_parantez_baz)
b2  = Button(frm2, text=')' ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_parantez_baste)
b3  = Button(frm2, text='MC',bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_MC)
b4  = Button(frm2, text='M+',bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_Mplus)
b5  = Button(frm2, text='M-',bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_Mminus)
b6  = Button(frm2, text='MR',bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_MR)
b7  = Button(frm2, text='AC',bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_AC)
b8  = Button(frm2, text='±' ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_PlusMinus)
b9  = Button(frm2, text='٪' ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_Darsad)
b10 = Button(frm2, text='÷' ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_Taqsim)

b11 = Button(frm2, text='round'      ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_round)
b12 = Button(frm2, text='x²'         ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_x2)
b13 = Button(frm2, text='x³'         ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_x3)
b14 = Button(frm2, text='x^y'        ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_xy)
b15 = Button(frm2, text='e^x'        ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_ex)
b16 = Button(frm2, text='10^x'       ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_10x)
b17 = Button(frm2, text='7'          ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_7)
b18 = Button(frm2, text='8'          ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_8)
b19 = Button(frm2, text='9'          ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_9)
b20 = Button(frm2, text=str(chr(215)),bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command=btn_zarb)

b21 = Button(frm2, text='1/x'   ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_1x_om)
b22 = Button(frm2, text='√x'    ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_radicalx)
b23 = Button(frm2, text='√x^3'  ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_radicalx3)
b24 = Button(frm2, text='√x^4'  ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_radicalx4)
b25 = Button(frm2, text='ln'    ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_ln)
b26 = Button(frm2, text='log10' ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_log10)
b27 = Button(frm2, text='4'     ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_4)
b28 = Button(frm2, text='5'     ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_5)
b29 = Button(frm2, text='6'     ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_6)
b30 = Button(frm2, text='-'     ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_subtract)

b31 = Button(frm2, text='X!'          ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_factorial)
b32 = Button(frm2, text='sin'         ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_sin)
b33 = Button(frm2, text='cos'         ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_cos)
b34 = Button(frm2, text='tan'         ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_tan)
b35 = Button(frm2, text='e'           ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_e)
b36 = Button(frm2, text=str(chr(171)) ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_back)
b37 = Button(frm2, text='1'           ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_1)
b38 = Button(frm2, text='2'           ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_2)
b39 = Button(frm2, text='3'           ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_3)
b40 = Button(frm2, text='+'           ,bg='#333333',fg = 'white', font=('Tahoma', 12),width=6, height=2,relief="flat", command = btn_plus)

b41 = Button(frm2, text='Deg' + str(' ') + str(chr(186)) ,bg='DodgerBlue2',fg = 'white', font=('Tahoma', 12), width=6, height=2,relief="flat", command = btn_convert)

b42 = Button(frm2, text='sin-1',bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_asin)
b43 = Button(frm2, text='cos-1',bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_acos)
b44 = Button(frm2, text='tan-1',bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_atan)
b45 = Button(frm2, text='π'    ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_pi)
b46 = Button(frm2, text='Rand' ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_rand)
b47 = Button(frm2, text='  0'  ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=13,  height=2,relief="flat", command = btn_0)
b48 = Button(frm2, text='.'    ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_dotted)
b49 = Button(frm2, text='='    ,bg='DodgerBlue2',fg = 'white', font=('Tahoma', 12),width=6 ,  height=2,relief="flat", command = btn_eval)

b1 .grid(row=1, column=0)
b2 .grid(row=1, column=1)
b3 .grid(row=1, column=2)
b4 .grid(row=1, column=3)
b5 .grid(row=1, column=4)
b6 .grid(row=1, column=5)
b7 .grid(row=1, column=6)
b8 .grid(row=1, column=7)
b9 .grid(row=1, column=8)
b10.grid(row=1, column=9)
b11.grid(row=2, column=0)
b12.grid(row=2, column=1)
b13.grid(row=2, column=2)
b14.grid(row=2, column=3)
b15.grid(row=2, column=4)
b16.grid(row=2, column=5)
b17.grid(row=2, column=6)
b18.grid(row=2, column=7)
b19.grid(row=2, column=8)
b20.grid(row=2, column=9)
b21.grid(row=3, column=0)
b22.grid(row=3, column=1)
b23.grid(row=3, column=2)
b24.grid(row=3, column=3)
b25.grid(row=3, column=4)
b26.grid(row=3, column=5)
b27.grid(row=3, column=6)
b28.grid(row=3, column=7)
b29.grid(row=3, column=8)
b30.grid(row=3, column=9)
b31.grid(row=4, column=0)
b32.grid(row=4, column=1)
b33.grid(row=4, column=2)
b34.grid(row=4, column=3)
b35.grid(row=4, column=4)
b36.grid(row=4, column=5)
b37.grid(row=4, column=6)
b38.grid(row=4, column=7)
b39.grid(row=4, column=8)
b40.grid(row=4, column=9)
b41.grid(row=5, column=0)
b42.grid(row=5, column=1)
b43.grid(row=5, column=2)
b44.grid(row=5, column=3)
b45.grid(row=5, column=4)
b46.grid(row=5, column=5)
b47.grid(row=5, column=6, columnspan=2,sticky='e')
b48.grid(row=5, column=8)
b49.grid(row=5, column=9)

b1.bind('<Motion>',  func1)
b1.bind('<Leave>' ,  func1_)

b2.bind('<Motion>' , func2)
b2.bind('<Leave>'  , func2_)

b3.bind('<Motion>' , func3)
b3.bind('<Leave>'  , func3_)

b4.bind('<Motion>' , func4)
b4.bind('<Leave>'  , func4_)
 
b5.bind('<Motion>' , func5)
b5.bind('<Leave>'  , func5_)

b6.bind('<Motion>' , func6)
b6.bind('<Leave>'  , func6_)

b7.bind('<Motion>' , func7)
b7.bind('<Leave>'  , func7_)

b8.bind('<Motion>' , func8)
b8.bind('<Leave>'  , func8_)

b9.bind('<Motion>' , func9)
b9.bind('<Leave>'  , func9_)

b10.bind('<Motion>', func10)
b10.bind('<Leave>' , func10_)

b11.bind('<Motion>', func11)
b11.bind('<Leave>' , func11_)

b12.bind('<Motion>', func12)
b12.bind('<Leave>' , func12_)

b13.bind('<Motion>', func13)
b13.bind('<Leave>' , func13_)

b14.bind('<Motion>', func14)
b14.bind('<Leave>' , func14_)

b15.bind('<Motion>', func15)
b15.bind('<Leave>',  func15_)

b16.bind('<Motion>', func16)
b16.bind('<Leave>' , func16_)

b17.bind('<Motion>', func17)
b17.bind('<Leave>' , func17_)

b18.bind('<Motion>', func18)
b18.bind('<Leave>' , func18_)

b19.bind('<Motion>', func19)
b19.bind('<Leave>' , func19_)

b20.bind('<Motion>', func20)
b20.bind('<Leave>' , func20_)

b21.bind('<Motion>', func21)
b21.bind('<Leave>' , func21_)

b22.bind('<Motion>', func22)
b22.bind('<Leave>' , func22_)

b23.bind('<Motion>', func23)
b23.bind('<Leave>' , func23_)

b24.bind('<Motion>', func24)
b24.bind('<Leave>' , func24_)

b25.bind('<Motion>', func25)
b25.bind('<Leave>' , func25_)

b26.bind('<Motion>', func26)
b26.bind('<Leave>' , func26_)

b27.bind('<Motion>', func27)
b27.bind('<Leave>' , func27_)

b28.bind('<Motion>', func28)
b28.bind('<Leave>' , func28_)

b29.bind('<Motion>', func29)
b29.bind('<Leave>' , func29_)

b30.bind('<Motion>', func30)
b30.bind('<Leave>' , func30_)

b31.bind('<Motion>', func31)
b31.bind('<Leave>' , func31_)

b32.bind('<Motion>', func32)
b32.bind('<Leave>' , func32_)

b33.bind('<Motion>', func33)
b33.bind('<Leave>' , func33_)

b34.bind('<Motion>', func34)
b34.bind('<Leave>' , func34_)

b35.bind('<Motion>', func35)
b35.bind('<Leave>' , func35_)

b36.bind('<Motion>', func36)
b36.bind('<Leave>' , func36_)

b37.bind('<Motion>', func37)
b37.bind('<Leave>' , func37_)

b38.bind('<Motion>', func38)
b38.bind('<Leave>' , func38_)

b39.bind('<Motion>', func39)
b39.bind('<Leave>' , func39_)

b40.bind('<Motion>', func40)
b40.bind('<Leave>' , func40_)

b41.bind('<Motion>', func41)
b41.bind('<Leave>' , func41_)

b42.bind('<Motion>', func42)
b42.bind('<Leave>' , func42_)

b43.bind('<Motion>', func43)
b43.bind('<Leave>' , func43_)

b44.bind('<Motion>', func44)
b44.bind('<Leave>' , func44_)

b45.bind('<Motion>', func45)
b45.bind('<Leave>' , func45_)

b46.bind('<Motion>', func46)
b46.bind('<Leave>' , func46_)

b47.bind('<Motion>', func47)
b47.bind('<Leave>' , func47_)

b48.bind('<Motion>', func48)
b48.bind('<Leave>' , func48_)

b49.bind('<Motion>', func49)
b49.bind('<Leave>' , func49_)
#---------Buttons of Standard calculator------------------------------------------------------------------------
btn1  =  Button(frm4, text='٪'          ,bg='#333333',fg = 'white', font=('tahoma', 12), width=7, height=3,relief="flat", command = button_darsad)
btn2  =  Button(frm4, text='CE'         ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_ce)
btn3  =  Button(frm4, text='C'          ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_c)
btn4  =  Button(frm4, text=str(chr(171)),bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_back)

btn5  =  Button(frm4, text='1/x',bg='#333333',fg = 'white' ,font=('tahoma', 12), width=7, height=3,relief="flat", command = button_1x_om)
btn6  =  Button(frm4, text='x2' ,bg='#333333',fg = 'white' ,font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_x2)
btn7  =  Button(frm4, text='√x' ,bg='#333333',fg = 'white' ,font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_2radicalx)
btn8  =  Button(frm4, text='÷'  ,bg='#333333',fg = 'white' ,font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_taghsim)

btn9  =  Button(frm4, text='7'          ,bg='#333333',fg = 'white', font=('tahoma', 12), width=7, height=3,relief="flat", command = button7)
btn10 =  Button(frm4, text='8'          ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button8)
btn11 =  Button(frm4, text='9'          ,bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button9)
btn12 =  Button(frm4, text=str(chr(215)),bg='#333333',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_zarb)

btn13 =  Button(frm4, text='4' ,bg='#333333',fg = 'white' , font=('tahoma', 12), width=7, height=3,relief="flat", command = button4)
btn14 =  Button(frm4, text='5' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button5)
btn15 =  Button(frm4, text='6' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button6)
btn16 =  Button(frm4, text='-' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_tafrigh)

btn17 =  Button(frm4, text='1' ,bg='#333333',fg = 'white' , font=('tahoma', 12), width=7, height=3,relief="flat", command = button1)
btn18 =  Button(frm4, text='2' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button2)
btn19 =  Button(frm4, text='3' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button3)
btn20 =  Button(frm4, text='+' ,bg='#333333',fg = 'white' , font=('Tahoma', 12), width=7, height=3,relief="flat", command = button_jam)
 
btn21 =  Button(frm4, text='±' ,bg='#333333'    ,fg = 'white', font=('tahoma', 12), width=7, height=3,relief="flat", command=button_plusminus)
btn22 =  Button(frm4, text='0' ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command=button0)
btn23 =  Button(frm4, text='.' ,bg='#333333'    ,fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command=btn_dotted)
btn24 =  Button(frm4, text='=' ,bg='DodgerBlue2',fg = 'white', font=('Tahoma', 12), width=7, height=3,relief="flat", command=buttonEval)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=1, column=3)

btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1)
btn7.grid(row=2, column=2)
btn8.grid(row=2, column=3)

btn9.grid(row=3, column=0)
btn10.grid(row=3, column=1)
btn11.grid(row=3, column=2)
btn12.grid(row=3, column=3)

btn13.grid(row=4, column=0)
btn14.grid(row=4, column=1)
btn15.grid(row=4, column=2)
btn16.grid(row=4, column=3)

btn17.grid(row=5, column=0)
btn18.grid(row=5, column=1)
btn19.grid(row=5, column=2)
btn20.grid(row=5, column=3)

btn21.grid(row=6, column=0)
btn22.grid(row=6, column=1)
btn23.grid(row=6, column=2)
btn24.grid(row=6, column=3)

btn1 .bind('<Motion>',  func_btn1)
btn1 .bind('<Leave>',   func_btn1_)

btn2 .bind('<Motion>',  func_btn2)
btn2 .bind('<Leave>',   func_btn2_)

btn3 .bind('<Motion>',  func_btn3)
btn3 .bind('<Leave>',   func_btn3_)

btn4 .bind('<Motion>',  func_btn4)
btn4 .bind('<Leave>',   func_btn4_)

btn5 .bind('<Motion>',  func_btn5)
btn5 .bind('<Leave>',   func_btn5_)

btn6 .bind('<Motion>',  func_btn6)
btn6 .bind('<Leave>',   func_btn6_)

btn7 .bind('<Motion>',  func_btn7)
btn7 .bind('<Leave>',   func_btn7_)

btn8 .bind('<Motion>',  func_btn8)
btn8 .bind('<Leave>',   func_btn8_)

btn9 .bind('<Motion>',  func_btn9)
btn9 .bind('<Leave>',   func_btn9_)

btn10.bind('<Motion>',  func_btn10)
btn10.bind('<Leave>',   func_btn10_)

btn11.bind('<Motion>',  func_btn11)
btn11.bind('<Leave>',   func_btn11_)

btn12.bind('<Motion>',  func_btn12)
btn12.bind('<Leave>',   func_btn12_)

btn13.bind('<Motion>',  func_btn13)
btn13.bind('<Leave>',   func_btn13_)

btn14.bind('<Motion>',  func_btn14)
btn14.bind('<Leave>',   func_btn14_)

btn15.bind('<Motion>',  func_btn15)
btn15.bind('<Leave>',   func_btn15_)

btn16.bind('<Motion>',  func_btn16)
btn16.bind('<Leave>',   func_btn16_)

btn17.bind('<Motion>',  func_btn17)
btn17.bind('<Leave>',   func_btn17_)

btn18.bind('<Motion>',  func_btn18)
btn18.bind('<Leave>',   func_btn18_)

btn19.bind('<Motion>',  func_btn19)
btn19.bind('<Leave>',   func_btn19_)

btn20.bind('<Motion>',  func_btn20)
btn20.bind('<Leave>',   func_btn20_)

btn21.bind('<Motion>',  func_btn21)
btn21.bind('<Leave>',   func_btn21_)

btn22.bind('<Motion>',  func_btn22)
btn22.bind('<Leave>',   func_btn22_)

btn23.bind('<Motion>',  func_btn23)
btn23.bind('<Leave>',   func_btn23_)

btn24.bind('<Motion>',  func_btn24)
btn24.bind('<Leave>',   func_btn24_)

win.mainloop()
