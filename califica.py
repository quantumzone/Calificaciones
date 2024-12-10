import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

class GradeProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Calificaciones CONALEP")
        self.root.geometry("800x600")
        
        # Variables
        self.grades_file = tk.StringVar()
        self.subjects_file = tk.StringVar()
        self.output_dir = tk.StringVar()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # File selection section
        ttk.Label(main_frame, text="Archivo de Calificaciones (Excel):").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.grades_file, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=lambda: self.browse_file(self.grades_file)).grid(row=0, column=2)
        
        ttk.Label(main_frame, text="Archivo de Materias y Docentes (Excel):").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.subjects_file, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=lambda: self.browse_file(self.subjects_file)).grid(row=1, column=2)
        
        ttk.Label(main_frame, text="Carpeta de Salida:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.output_dir, width=50).grid(row=2, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_directory).grid(row=2, column=2)
        
        # Process button
        ttk.Button(main_frame, text="Procesar y Generar Boletas", 
                  command=self.process_grades, style='Accent.TButton').grid(row=3, column=0, columnspan=3, pady=20)
        
        # Progress section
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(main_frame, length=300, mode='determinate', 
                                          variable=self.progress_var)
        self.progress_bar.grid(row=4, column=0, columnspan=3, pady=10)
        
        self.status_label = ttk.Label(main_frame, text="")
        self.status_label.grid(row=5, column=0, columnspan=3)

    def browse_file(self, var):
        filename = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )
        if filename:
            var.set(filename)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir.set(directory)

    def convert_to_ten_scale(self, percentage):
        """Convert percentage to 10-point scale using rule of three"""
        return (percentage * 10) / 100

    def process_grades(self):
        try:
            # Read Excel files
            grades_df = pd.read_excel(self.grades_file.get())
            subjects_df = pd.read_excel(self.subjects_file.get())
            
            # Convert percentages to 10-scale
            grade_columns = ['CCVE00','INII00','PEMA00','ATDI00','IDME00','IMCH00','ITSO00','FOSO00']

            for col in grade_columns:
                grades_df[col] = grades_df[col].apply(self.convert_to_ten_scale)
            
            # Generate PDFs
            self.generate_report_cards(grades_df, subjects_df)
            
            messagebox.showinfo("Éxito", "Proceso completado exitosamente!")
            self.status_label.config(text="Proceso completado exitosamente!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante el proceso: {str(e)}")
            self.status_label.config(text=f"Error: {str(e)}")

    def generate_report_cards(self, grades_df, subjects_df):
        output_file = os.path.join(self.output_dir.get(), "boletas.pdf")
        c = canvas.Canvas(output_file, pagesize=letter)
        
        # Configure font
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
        
        students_per_page = 2
        total_students = len(grades_df)
        
        for i in range(0, total_students, students_per_page):
            # First student on page
            if i < total_students:
                self.draw_report_card(c, grades_df.iloc[i], subjects_df, 0)
            
            # Second student on page
            if i + 1 < total_students:
                self.draw_report_card(c, grades_df.iloc[i + 1], subjects_df, 4.5 * inch)
            
            c.showPage()
            
            # Update progress
            self.progress_var.set((i + 1) / total_students * 100)
            self.root.update()
        
        c.save()

    def draw_report_card(self, c, student_data, subjects_df, y_offset):
        # Draw logo
        # c.drawImage("conalep_logo.png", 1*inch, (10-y_offset)*inch, width=1*inch, height=0.5*inch)
        
        # Draw header
        c.setFont('Arial', 12)
        c.drawString(1*inch, (9.5-y_offset)*inch, "BOLETA DE CALIFICACIONES 2DO. CORTE")
        
        # Draw student info
        c.setFont('Arial', 10)
        c.drawString(1*inch, (9-y_offset)*inch, f"Nombre del Alumno: {student_data['Alumno']}")
        c.drawString(1*inch, (8.7-y_offset)*inch, f"Matrícula: {student_data['Matricula']}")
        
        # Draw grades
        y = 8.2
        for idx, row in subjects_df.iterrows():
            c.drawString(1*inch, (y-y_offset)*inch, f"{row['Materia']}")
            c.drawString(5*inch, (y-y_offset)*inch, f"{student_data[row['Columna']]:.1f}")
            y -= 0.3
        
        # Draw footer
        c.setFont('Arial', 8)
        c.drawString(1*inch, (5-y_offset)*inch, "Director del plantel Conalep Apatzingán")

def main():
    root = tk.Tk()
    app = GradeProcessorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()