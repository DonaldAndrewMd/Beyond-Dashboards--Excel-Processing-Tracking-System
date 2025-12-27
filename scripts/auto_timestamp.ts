
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
   const dataRange: ExcelScript.Range = table.getRangeBetweenHeaderAndTotal();
   const values: (string | number | boolean)[][] = dataRange.getValues();
   const headers: (string | number | boolean)[] = table.getHeaderRowRange().getValues()[0];
   const nameIndex: number = headers.indexOf("Name");
   const authCodeIndex: number = headers.indexOf("AUTH CODE");
   const orderTimeIndex: number = headers.indexOf("Order Time");
   
   //If one if one of these are not found stop the script and log the error
   if ([nameIndex, authCodeIndex, orderTimeIndex].includes(-1)) {
    console.log("One or more required columns are missing.");
    return;
  }

   const now: Date = new Date();
  const timestamp: string = getFormattedTimestamp(now);
  let lastName: string = "";
  let lastAuthCode: string = "";
  for (let i: number = 0; i < values.length; i++) {
    const row: (string | number | boolean)[] = values[i];
    const name: string = (row[nameIndex] as string)?.toString().trim();
    const authCode: string = (row[authCodeIndex] as string)?.toString().trim();
    const orderTime: string = (row[orderTimeIndex] as string)?.toString();
    const rowRange: ExcelScript.Range = dataRange.getRow(i);
   
    // Auto-fill AUTH CODE
    if (name) {
      if (authCode) {
        lastName = name;
        lastAuthCode = authCode;
      } else if (name === lastName && lastAuthCode) {
        rowRange.getCell(0, authCodeIndex).setValue(lastAuthCode);
      } else {
        lastName = name;
        lastAuthCode = "";
      }
    } else {
      lastName = "";
      lastAuthCode = "";
    }
    // Set Order Time if AUTH CODE is filled and Order Time is blank
    if ((!orderTime || orderTime === "") && (authCode || lastAuthCode)) {
      rowRange.getCell(0, orderTimeIndex).setValue(timestamp);
    }
  }

/* The Create a timestamp format that is independent of regional settings, 
the date columns are to be forced to string format and padded accordingly*/

  function getFormattedTimestamp(date: Date): string {
    const pad = (n: number) => n.toString().padStart(2, '0');
    const day = pad(date.getDate());
    const month = pad(date.getMonth() + 1);
    const year = date.getFullYear();
    let hour = date.getHours();
    const minute = pad(date.getMinutes());
    const ampm = hour >= 12 ? "PM" : "AM";
    hour = hour % 12 || 12;
    return `${day}/${month}/${year} ${pad(hour)}:${minute} ${ampm}`;
  }
   
}
