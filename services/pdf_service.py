import PyPDF2
from fastapi import HTTPException

def extract_text_from_pdf(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)

            if reader.is_encrypted:
                raise HTTPException(
                    status_code=400,
                    detail="Encrypted PDFs are not supported."
                )

            total_pages = len(reader.pages)
            pages = []
            full_text = ""

            for page_num, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                pages.append({
                    "page_number": page_num + 1,
                    "text": text.strip(),
                })
                full_text += text + "\n"

            return {
                "total_pages": total_pages,
                "full_text": full_text.strip(),
                "pages": pages,
            }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to extract text: {str(e)}"
        )