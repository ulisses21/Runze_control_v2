import tkinter as tk
from tkinter import ttk, messagebox
import serial.tools.list_ports
import logging
from runze_control.rotary_valve import RotaryValve

# Logging setup
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())
logger.handlers[-1].setFormatter(
    logging.Formatter(fmt='%(asctime)s:%(name)s:%(levelname)s: %(message)s'))

selector_valve = None

class RotaryValveUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rotary Valve Controller")
        self.geometry("500x320")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # COM Port selection
        tk.Label(self, text="Select COM Port:").pack(pady=5)
        self.port_combobox = ttk.Combobox(self, values=self.get_com_ports(), state="readonly")
        self.port_combobox.pack(pady=5)
        
        #Number of Ports
        tk.Label(self,text="Enter Total Number of Positions:").pack(pady=5)
        self.pos_combobox= ttk.Combobox(self,values=[6,8,10],state="readonly")
        self.pos_combobox.pack(pady=5)
       
        
        #Connect button
        tk.Button(self,text="Connect to Device",command=self.connect_valve).pack(pady=10)
        # Port input
        tk.Label(self, text="Enter Port Number (0–10):").pack(pady=5)
        self.port_entry = tk.Entry(self)
        self.port_entry.pack(pady=5)

        # Move button
        self.move_button = tk.Button(self, text="Move Clockwise", command=self.Move_CW_to_port)
        self.move_button.pack(pady=10)

        # Motor status button
        self.status_button = tk.Button(self, text="Check Motor Status", command=self.check_motor_status)
        self.status_button.pack(pady=10)

        # Footer info
        self.footer = tk.Label(self, text="", anchor="e", justify="right", font=("Arial", 10), fg="gray")
        self.footer.pack(side="bottom", fill="x", padx=10, pady=10)

        # Exit button
        tk.Button(self, text="Exit", command=self.quit).pack(side="bottom", pady=5)

    def get_com_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def connect_valve(self, event=None):
        global selector_valve
        Com_port = str(self.port_combobox.get())
        N_position = int(self.pos_combobox.get())
        try:
            selector_valve = RotaryValve(com_port=Com_port, address=0x00, position_count=N_position)
            address = selector_valve.get_address()
            baudrate = selector_valve.get_rs232_baudrate()
            firmware = selector_valve.get_firmware_version()
            self.footer.config(text=f"Address: {address} | Baudrate: {baudrate} | Firmware: {firmware}")
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    def Move_CW_to_port(self):
        N_position = int(self.pos_combobox.get())
        if selector_valve:
            try:
                port = int(self.port_entry.get())
                if 0 <= port <= N_position:
                    selector_valve.move_clockwise_to_position(port,max_port=N_position)
                    messagebox.showinfo("Success", f"Moved to Port {port}")
                else:
                    messagebox.showwarning("Invalid Input", "Port number must be between 0 and")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid integer.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Not Connected", "Please select a COM port first.")

    def check_motor_status(self):
        if selector_valve:
            try:
                status = selector_valve.get_motor_status
                messagebox.showinfo("Motor Status", f"Status: {status}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Not Connected", "Please select a COM port first.")

if __name__ == "__main__":
    app = RotaryValveUI()
    app.mainloop()
