import tkinter as tk


root = tk.Tk()
city = ""
pet = ""
GREEN = "\033[32m"
RESET = "\033[0m"

button = tk.Button(
    root,
    text = "Run",
    command = lambda : root.quit()
)


button.pack()
print(GREEN +"Click", button, "to run the final project you will build." + RESET)
button.mainloop()

print("Welcome to the Band Name Generator.")

city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

print(f"Your band name could be {city} {pet}!")