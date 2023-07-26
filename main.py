import tkinter

window=tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300,height=300)

label1=tkinter.Label(text="Enter your weight")
label1.config(pady=7, padx=7)
label1.pack()

weight=tkinter.Entry()
weight.pack()

label2=tkinter.Label(text="Enter your height")
label2.pack()

height=tkinter.Entry()
height.pack(padx=5, pady=5)

def calculator():
    weight_value =weight.get()
    height_value =height.get()


    if weight_value =="" or height_value =="":
        print("Enter both weight and height")
    else:
        try:
            weight_value = float(weight_value)
            height_value = float(height_value)
            bmi = weight_value / pow((height_value / 100), 2)
            if weight_value<=0 or height_value<=0:
                print("The values must be greater than 0")
            else:
                if (bmi < 18.5):
                    classification = "Under Weight"
                elif (bmi >= 18.5 and bmi < 25):
                    classification = "Normal"
                elif (bmi >= 25 and bmi < 30):
                    classification = "Over Weight"
                elif (bmi >= 30):
                    classification = "Obese"
                print("Your BMI is {:.2f} {}".format(bmi, classification))

        except ValueError:
            print("Enter a valid number")


button=tkinter.Button(text="Calculate",command=calculator)
button.config(pady=5,padx=5)
button.pack()


window.mainloop()