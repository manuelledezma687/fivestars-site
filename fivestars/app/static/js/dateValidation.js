const today = new Date();
const daysToDisable = 0; 
const disabledDate = new Date(today.getTime() - (daysToDisable * 24 * 60 * 60 * 1000)).toISOString().split('T')[0];
document.getElementById("date").setAttribute("min", disabledDate);
