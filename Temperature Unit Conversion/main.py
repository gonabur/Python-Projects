import customtkinter as tk
from tkinter import ttk, messagebox
class mainApp:
    def __init__(self, master):
        self.master = master
        self.__create_widgets()
        self.__configure_widgets()
        self.__position_widgets()
    def __create_widgets(self):

        #Constructores
        self.mainFrame = tk.CTkFrame(self.master)
        self.frame_inputs = tk.CTkLabel(self.mainFrame, text= "Pasaje:")
        self.frame_formulas = tk.CTkLabel(self.mainFrame, text= "Fórmulas utilizadas:")
        
        self.title = tk.CTkLabel(self.mainFrame, text = "Pasaje de unidades")
        
                    #Valor a convertir
        self.ask_user = tk.CTkLabel(self.frame_inputs, text= "Grados:")
        self.first_Options = ttk.Combobox(self.frame_inputs, values= ["Celsius", "Farenheit", "Kelvin"], state= "readonly", postcommand= self.__show_options_first_combobox)
        self.base = tk.CTkEntry(self.frame_inputs)
        
                    #Conversión
        self.result = tk.CTkLabel(self.frame_inputs, text = "Unidad a convertir: ")
        self.final_options = ttk.Combobox(self.frame_inputs, state= "readonly", postcommand= self.__show_second_options)
        self.button_convertir = tk.CTkButton(self.frame_inputs, text= "Convertir", command = self.__button_callback_result)

                #Mostrar Formulas
        self.primer_formula = tk.CTkLabel(self.frame_formulas, text= "°C -> °F = 1.8 * °C + 32")
        self.segunda_formula = tk.CTkLabel(self.frame_formulas, text= "°F -> °C = 5/9 * (°F - 32)")
        self.tercera_formula = tk.CTkLabel(self.frame_formulas, text= "°C -> °K = °C + 273")
        
    def __configure_widgets(self):
        #configure - Widgets
        self.title.configure(font= ("Helvetica", 22, "normal"))
        self.frame_inputs.configure(font = ("Helvetica", 20), padx = 15)


        self.first_Options.current(0)
        self.first_Options.configure(width= 10)
        self.base.configure(width= 60)
        
        self.final_options.configure(width = 8)
    def __position_widgets(self):    
        #Contenedores
        self.mainFrame.place(relheight= 1, relwidth= 1)
        self.frame_inputs.grid(row = 1, column= 0, columnspan= 3, rowspan = 4)
        self.frame_formulas.grid(row = 5)
        #Título
        self.title.grid(row = 0, column= 0, padx= 10, pady= 10, columnspan= 3)
        
        #Inputs - First
        self.ask_user.grid(row = 2, column = 0, padx = 10)
        self.base.grid(row = 2, column= 1, padx = 10)
        self.first_Options.grid(row = 2, column= 2, padx = 10)
        
        #Conversiones - Final
        self.result.grid(row = 4, column = 1, columnspan= 1, sticky= "e", pady= 10)
        self.final_options.grid(row = 4, column= 2, columnspan= 1, sticky= "e")
        
        self.button_convertir.grid(row = 5, column= 2)
        #Mostrar en frame FORMULAS
        self.primer_formula.grid(row = 0, column= 0, sticky= "w")
        self.segunda_formula.grid(row = 1, column= 0, sticky= "w")
        self.tercera_formula.grid(row = 2, column= 0, sticky= "w")
    def __show_options_first_combobox(self):
        self.option_logic_value = self.first_Options.current()
        
    def __show_second_options(self):
        self.__show_options_first_combobox()
        if self.option_logic_value == 0:
            self.final_options.configure(values = ["Farenheit", "Kelvin"])
        elif self.option_logic_value == 1:
            self.final_options.configure(values = ["Celsius", "Kelvin"])
        else:
            self.final_options.configure(values = ["Celsius", "Farenheit"])
    def __button_callback_result(self):
        one,two, three = self.__get_user_inputs()
        if one == "Celsius":
            if two == "Farenheit":
                self.variable_result = round(self.__fFarenheit(three), 2)
                messagebox.showinfo(title= "Conversión Celsius a Farenheit", message= f"Grados Celsius: {three}\nGrados Farenheit: {self.variable_result}°F")
            elif two == "Kelvin":
                self.variable_result = round(self.__fKelvin(three), 2)
                messagebox.showinfo(title= "Conversión Celsius a Kelvin", message= f"Grados Celsius: {three}\nGrados Kelvin: {self.variable_result}°K")
        elif one == "Farenheit":
            if two == "Celsius":
                self.variable_result = round(self.__fCelcius(three),2)
                messagebox.showinfo(title= "Conversión Farenheit a Celsius", message= f"Grados Farenheit : {three}\nGrados Celsius: {self.variable_result}°C")
            elif two == "Kelvin":
                variable_temp_result = self.__fCelcius(three) #Almacenar temporalmente celsius
                self.variable_result = round(self.__fKelvin(variable_temp_result),2)
                messagebox.showinfo(title= "Conversión Farenheit a Kelvin", message= f"Grados Farenheit: {three}\nGrados Kelvin: {self.variable_result}°K")
        elif one == "Kelvin":
            if two == "Celsius":
                self.variable_result = round(self.__fkelvin_c(three),2)
                messagebox.showinfo(title= "Conversión Kelvin a Celsius", message= f"Grados Kelvin : {three} °K\nGrados Celsius: {self.variable_result} °C")
            elif two == "Farenheit":
                variable_temp_result = self.__fkelvin_c(three) #Almacenar temporalmente celsius
                print(variable_temp_result)
                self.variable_result = round(self.__fFarenheit(variable_temp_result),2)
                messagebox.showinfo(title= "Conversión Kelvin a Farenheit", message= f"Grados Kelvin: {three} °K\nGrados Farenheit: {self.variable_result} °F")
            
    def __fFarenheit(self,grades_c):
        f = (1.8 * grades_c) + 32
        return f
        
    def __fCelcius(self,grades_f):
        c = (5/9) * (grades_f - 32)
        return c
        
    def __fKelvin(self,grades_c):
        k = grades_c + 273
        return k
    def __fkelvin_c(self, grades_k):
        k = grades_k - 273
        return k
        
    def __get_user_inputs(self):
        #Entry
        try:
            self.grades_input = float(self.base.get())
            
        except ValueError:
                messagebox.showerror(title= "Error", message="VALUE ERROR - Se espera un valor númerico")
        #ComboBox
        self.first_choice = self.first_Options.get()
        self.second_choice = self.final_options.get()
        
        return self.first_choice, self.second_choice, self.grades_input





if __name__ == "__main__":
    print("Aplicación para el pasaje de unidades de temperatura")
    
    app = tk.CTk()
    ventana = mainApp(app)

    app.geometry("400x300")
    app.resizable(False, False)
    app.title("Pasaje de unidades de Temperatura")
    app.iconbitmap("C:/Users/gonzx/Desktop/Develop/Python 2k24/Proyectos/Pasaje Temperatura/temp.ico")
    app.mainloop()