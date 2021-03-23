/// this script works for Google Sheets-script ///
/// it creates a function that can be used to load a Looker public Look into a spreadsheet
/// and pull fresh data each time the spreadsheet is opened
/// Note: Looker's Google Sheets Action is less brittle than this
/// /// /// /// /// /// /// /// /// /// /// /// /// /// 




function onOpen(){
/// get current spreadsheet url and sheet
var e=SpreadsheetApp.getActiveSpreadsheet();
/// create menu -- refresh and refresh all under "Looker"
var t=[{name:"Refresh This Sheet",functionName:"Refresh"},{name:"Refresh All Sheets",functionName:"RefreshAll"}];
e.addMenu("Looker",t)
Refresh(e)
}
function onInstall(e){
onOpen(e)
}
function Refresh(e){
/// current sheet if no active sheet passed
var t=SpreadsheetApp.getActiveSheet();
if(typeof e!=="undefined"){
t=e
}
/// find which cell has our fetch function
var n=t.getDataRange();
var r=find("ImportXML",n);
var y=find("lookerFetchData", n);
for(var i=0;i<r.length;i++){
/// add refresh time
r[i].setValue(r[i].getFormula().replace(/(.gsxml[^"]*)"/,".gsxml?apply_formatting=true&apply_vis=true&refresh="+(new Date).getTime()+'"'))
}
for(var i=0;i<y.length;i++){
y[i].setValue(y[i].getFormula().replace(/(.html[^"]*|.txt[^"]*)"/,".txt?apply_formatting=true&apply_vis=true&refresh="+(new Date).getTime()+'"'))
}
}
function RefreshAll(){
var e=SpreadsheetApp.getActiveSpreadsheet().getSheets();
for(var t=0;t<e.length;t++){
Refresh(e[t])
}
}
/// find all formulas that(used in refresh)
function find(e,t){
var n=t.getFormulas();
/// n is now a list of coordinates with formulas (eg A1)
var r=[];
for(var i=0;i<n.length;i++){
for(var s=0;s<n[i].length;s++){
var x = n[i][s].toUpperCase();
if(x.indexOf(e)>-1){
r.push(t.getCell(i+1,s+1))
}
}
}
return r
}
