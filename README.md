# Batch Scatterplot Generator

This Python script creates scatterplots from all `.csv` and `.xlsx` files in an `input_folder`, automatically labeling axes using the files’ headers. A blue line connects the dots on each scatterplot. Output images are saved in a `scatterplots` folder.

---

## Dependencies

- **Python 3.x**
- **pandas**
- **matplotlib**
- **openpyxl** (for reading Excel `.xlsx` files)

---

## Install Dependencies

With pip:

```bash
pip install pandas matplotlib openpyxl
```