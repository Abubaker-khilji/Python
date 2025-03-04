import fitz  # PyMuPDF
from PyPDF2 import PdfReader, PdfWriter
import os

# =============================================
# 1. Fill the PDF Template with Data
# =============================================
def fill_pdf_template("C:\\Users\\254\\Downloads\\AUTOMATION", "C:\Users\254\Downloads\AUTOMATION", data):
    """
    Fills form fields in a PDF template with provided data.
    - Assumes the PDF has form fields with specific names (e.g., "customer_name").
    - Handles multiple measures dynamically (e.g., "measure_1_design_date").
    """
    doc = fitz.open("C:\\Users\\254\\Downloads\\AUTOMATION\\COORDINATION TEMPLATE-M rana.pdf")
    
    for page in doc:
        widgets = page.widgets()
        for widget in widgets:
            field_name = widget.field_name
            
            # Fill customer/date fields
            if field_name in data:
                widget.field_value = str(data[field_name])
                widget.update()
            
            # Fill measure-specific fields (e.g., measure_0_design_date)
            if field_name.startswith("measure_"):
                parts = field_name.split("_")
                if len(parts) == 3 and parts[0] == "measure":
                    measure_idx = int(parts[1])
                    field_type = parts[2]
                    if measure_idx < len(data["measures"]):
                        value = data["measures"][measure_idx].get(field_type, "")
                        widget.field_value = str(value)
                        widget.update()
    
    doc.save(output_path)

# =============================================
# 2. Split the Filled PDF into Smaller Documents
# =============================================
def split_pdf(input_path, output_config, base_folder="output"):
    """
    Splits a PDF into smaller documents based on page ranges.
    - output_config: Dictionary of {doc_name: [list_of_page_indices]}
    - Pages are 0-indexed.
    """
    reader = PdfReader(input_path)
    
    for doc_name, pages in output_config.items():
        writer = PdfWriter()
        output_dir = os.path.join(base_folder, doc_name)
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract pages
        for page_num in pages:
            if page_num < len(reader.pages):
                writer.add_page(reader.pages[page_num])
        
        # Save to file
        output_path = os.path.join(output_dir, f"{doc_name}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)

# =============================================
# 3. Example Usage
# =============================================
if __name__ == "_main_":
    # Define input data
    data = {
        "customer_name": "John Doe",
        "address": "123 Main St",
        "design_date": "2023-10-01",
        "install_date": "2023-10-05",
        "handover_date": "2023-10-10",
        "measures": [
            {
                "design_date": "2023-10-01",
                "install_date": "2023-10-05",
                "installer": "Alice"
            },
            {
                "design_date": "2023-10-02",
                "install_date": "2023-10-06",
                "installer": "Bob"
            }
        ]
    }
    
    # Fill the template
    fill_pdf_template(
        template_path="template.pdf",
        output_path="filled_template.pdf",
        data=data
    )
    
    # Split into smaller documents (customize page ranges)
    output_config = {
        "risk_assessment": [0, 1],   # Pages 0-1
        "io_doc": [2],               # Page 2
        "des_vent": [3],             # Page 3
        "specifications": [4, 5]     # Pages 4-5
    }
    
    split_pdf(
        input_path="filled_template.pdf",
        output_config=output_config,
        base_folder="output_documents"
    )

    print("Pipeline executed successfully!")