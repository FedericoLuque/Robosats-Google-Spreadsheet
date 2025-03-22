import gspread
from google.oauth2.service_account import Credentials
import json
import os
import tkinter as tk
from tkinter import messagebox

# Leer los datos sensibles desde el archivo config.json
def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

config = load_config()

def update_google_sheet(json_data): 
    # Cargar credenciales desde el archivo JSON
    creds = Credentials.from_service_account_file(config['google_credentials_file'], scopes=config['google_scopes'])
    client = gspread.authorize(creds)
    
    # Abrir la hoja de cálculo usando el ID desde el archivo de configuración
    sheet = client.open_by_key(config['google_sheet_id']).worksheet(config['sheet_name'])
    
    # Extraer datos del JSON de manera estructurada
    headers = ["coordinator", "order_id", "currency", "maker_trade_fee_percent", "maker_bond_size_sats", "maker_is_buyer", "maker_sent_fiat", "maker_received_sats", "taker_trade_fee_percent", "taker_bond_size_sats", "taker_is_buyer", "taker_sent_sats", "taker_received_fiat", "platform_contract_exchange_rate", "platform_contract_timestamp", "platform_contract_total_time", "platform_routing_budget_sats", "platform_trade_revenue_sats"]
    
    row = [
        json_data["coordinator"],
        json_data["order_id"],
        json_data["currency"],
        json_data["maker"]["trade_fee_percent"],
        json_data["maker"]["bond_size_sats"],
        json_data["maker"]["is_buyer"],
        json_data["maker"]["sent_fiat"],
        json_data["maker"]["received_sats"],
        json_data["taker"]["trade_fee_percent"],
        json_data["taker"]["bond_size_sats"],
        json_data["taker"]["is_buyer"],
        json_data["taker"]["sent_sats"],
        json_data["taker"]["received_fiat"],
        json_data["platform"]["contract_exchange_rate"],
        json_data["platform"]["contract_timestamp"],
        json_data["platform"]["contract_total_time"],
        json_data["platform"]["routing_budget_sats"],
        json_data["platform"]["trade_revenue_sats"]
    ]
    
    # Insertar encabezados si la hoja está vacía
    if not sheet.get_all_values():
        sheet.append_row(headers)
    
    # Insertar datos
    sheet.append_row(row)
    print("Datos insertados correctamente en la hoja de cálculo.")

def confirm_and_delete(file):
    # Crear una ventana de confirmación con tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    result = messagebox.askyesno("Confirmar eliminación", f"¿Deseas eliminar el archivo {file} después de procesarlo?")
    
    if result:
        os.remove(file)
        print(f"Archivo {file} eliminado.")
    else:
        print(f"Archivo {file} no eliminado.")

def show_no_files_notification():
    # Crear una ventana de notificación emergente con tkinter
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("Sin archivos JSON", "No se han encontrado archivos .json para procesar.")

# Procesar múltiples archivos trade.json en la carpeta
json_files_found = False  # Variable para verificar si hay archivos .json
for file in os.listdir():
    if file.startswith("trade") and file.endswith(".json"):
        json_files_found = True
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                update_google_sheet(data)
                # Confirmar eliminación y luego eliminar archivo
                confirm_and_delete(file)
        except Exception as e:
            print(f"Error procesando {file}: {e}")

# Si no se encontraron archivos .json, mostrar notificación
if not json_files_found:
    show_no_files_notification()
