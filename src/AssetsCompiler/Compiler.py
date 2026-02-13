import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import sys

class OPNMasterDistributor:
    def __init__(self, root):
        self.root = root
        self.root.title("OPN BluePanda - Distribuidor del Compilador")
        self.root.geometry("600x550")
        
        # --- Configuración de Archivos Core ---
        # Buscamos opn.py como el punto de entrada principal
        self.main_script = tk.StringVar(value="opn.py")
        self.company = tk.StringVar(value="OPN BluePanda Corp")
        self.version = tk.StringVar(value="2.0.0.0")
        self.internal_name = tk.StringVar(value="opn_engine")
        self.icon_path = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"))
        
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Configuración del Ejecutable Maestro (opn.exe)", style="Header.TLabel").pack(pady=(0, 20))

        # --- Selección del Script Principal ---
        ttk.Label(main_frame, text="Script de Entrada Principal (ej: opn.py):").pack(anchor="w")
        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(fill="x", pady=5)
        ttk.Entry(entry_frame, textvariable=self.main_script).pack(side="left", fill="x", expand=True)
        ttk.Button(entry_frame, text="Buscar", command=self.select_main).pack(side="right", padx=5)

        # --- Metadatos de Empresa ---
        meta_frame = ttk.LabelFrame(main_frame, text=" Información de Propiedad y Versión ", padding=15)
        meta_frame.pack(fill="x", pady=20)

        fields = [
            ("Nombre Empresa:", self.company),
            ("Versión Software:", self.version),
            ("Nombre Interno:", self.internal_name),
        ]

        for i, (label, var) in enumerate(fields):
            ttk.Label(meta_frame, text=label).grid(row=i, column=0, sticky="w", pady=5)
            ttk.Entry(meta_frame, textvariable=var).grid(row=i, column=1, sticky="ew", padx=10)

        # --- Icono ---
        ttk.Label(meta_frame, text="Icono del Compilador:").grid(row=3, column=0, sticky="w", pady=5)
        ttk.Entry(meta_frame, textvariable=self.icon_path).grid(row=3, column=1, sticky="ew", padx=10)
        ttk.Button(meta_frame, text="...", width=3, command=self.select_icon).grid(row=3, column=2)

        meta_frame.columnconfigure(1, weight=1)

        # --- Botón de Construcción ---
        self.status = ttk.Label(main_frame, text="Listo para empaquetar el motor OPN", foreground="gray")
        self.status.pack(pady=10)

        self.btn_build = ttk.Button(main_frame, text="📦 CREAR OPN.EXE (ONEFILE)", command=self.run_pyinstaller)
        self.btn_build.pack(fill="x", ipady=10)

    def select_main(self):
        path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
        if path: self.main_script.set(path)

    def select_icon(self):
        path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
        if path: self.icon_path.set(path)

    def run_pyinstaller(self):
        main_file = self.main_script.get()
        if not os.path.exists(main_file):
            messagebox.showerror("Error", f"No se encuentra el archivo: {main_file}")
            return

        self.status.config(text="Empaquetando... por favor no cierres la ventana", foreground="blue")
        self.root.update()

        # Construcción del comando PyInstaller
        # --onefile: crea un solo .exe
        # --name: nombre del ejecutable final (opn.exe)
        # --collect-all: asegura que se lleven todas las dependencias de tus módulos
        cmd = [
            "pyinstaller",
            "--noconfirm",
            "--onefile",
            "--console", # El compilador suele ser de consola
            f"--name=opn",
            main_file
        ]

        if self.icon_path.get():
            cmd.append(f"--icon={self.icon_path.get()}")

        # Agregamos los otros archivos como dependencias si están en la misma carpeta
        # PyInstaller los detectará automáticamente por los 'import' en opn.py,
        # pero podemos forzar la inclusión de opn2.py y opn_compiler.py
        current_dir = os.path.dirname(os.path.abspath(main_file))
        cmd.extend(["--paths", current_dir])

        try:
            # Ejecutar proceso
            process = subprocess.run(cmd, capture_output=True, text=True)
            
            if process.returncode == 0:
                messagebox.showinfo("Éxito", "¡El compilador OPN.EXE ha sido creado en la carpeta /dist!")
                self.status.config(text="¡Proceso completado!", foreground="green")
            else:
                print(process.stderr)
                messagebox.showerror("Error PyInstaller", process.stderr[:500])
                self.status.config(text="Error en la creación", foreground="red")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = OPNMasterDistributor(root)
    root.mainloop()