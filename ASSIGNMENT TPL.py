import requests
import json
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Currency Converter")

#LABELS AND DROPDWON MENUS FOR THE USER
from_currency_label = tk.Label(root, text="From Currency")
from_currency_label.grid(row=0, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, width=20, state="readonly")
from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)

#TO CURRENCY THE USER WANT
to_currency_label = tk.Label(root, text="To Currency")
to_currency_label.grid(row=1, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, width=20, state="readonly")
to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

#AMOUNT TO BE CONVERTED
amount_label = tk.Label(root, text="Amount")
amount_label.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

#CONVERTED AMOUNT
converted_amount_label = tk.Label(root, text="Converted Amount")
converted_amount_label.grid(row=3, column=0, padx=10, pady=10)
converted_amount_value_label = tk.Label(root, text="")
converted_amount_value_label.grid(row=3, column=1, padx=10, pady=10)

#CREATE THE CONVERT BUTTON FROM ONE CURRENCY TO ANOTHER
def convert():
    app_id = "013032b5ab484713a9978b55fc8082c7"
    amount = amount_entry.get()
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    url = f"https://openexchangerates.org/api/latest.json?app_id={app_id}"
    response = requests.get(url)
    if response.status_code != 200:
        # API call was not successful, handle the error
        converted_amount_value_label.config(text="Error: API call failed")
        return
    data = json.loads(response.text)
    if "rates" not in data:
        # API response does not contain expected data, handle the error
        converted_amount_value_label.config(text="Error: API response format is not valid")
        return
    to = data["rates"][from_currency]
    exchange_rate = data["rates"][to_currency]
    converted_amount_value_label.config(text=f"{exchange_rate/to * float(amount):.2f}")

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=4, column=0, padx=10, pady=10)

#CODE FOR THE RESET BUTTON TO INITIALIZE IT WITH 0 AGAIN
def reset():
    from_currency_combobox.set("")
    to_currency_combobox.set("")
    amount_entry.delete(0, tk.END)
    converted_amount_value_label.config(text="")

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.grid(row=4, column=1, padx=10, pady=10)

#URL OF CURRENCY WEBSITE
url = "https://openexchangerates.org/api/currencies.json"
response = requests.get(url)
data = json.loads(response.text)
currencies = list(data.keys())
from_currency_combobox["values"] = currencies
to_currency_combobox["values"] = currencies

root.mainloop()