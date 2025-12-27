
function main(workbook: ExcelScript.Workbook) {
   //Select the active sheet
  const sheet: ExcelScript.Worksheet = workbook.getActiveWorksheet();

/*On the workbook there are 4 mains Sheets for each quarter to prevent overloading
Select the table that starts with "Q" (for Quarter) in the active sheet*/
  
  const table: ExcelScript.Table = sheet.getTables().find(t => t.getName().startsWith("Q"));
  if (!table) {
    console.log("Table not found.");
    return;
  }

}
