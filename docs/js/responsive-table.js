const tables = document.querySelectorAll("table"); // query all table in page
tables.forEach((element) => {
  // append table-responsive class from bootstrap
  element.className += " table-responsive";
});
