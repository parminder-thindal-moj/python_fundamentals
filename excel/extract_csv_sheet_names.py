from openpyxl import load_workbook

wb = load_workbook(
    "/Users/parminder.thindal/Library/CloudStorage/OneDrive-MinistryofJustice/Cross-CJS data asset/Official Alpha-CJS documentation/Metadata/Alpha-CJS Phase 2 metadata.xlsx"
)

sheet_names = wb.sheetnames


if __name__ == "__main__":
    for sheet in sheet_names:
        print(sheet)
