// jQuery Wait for DOM ON Load
$(function() {
  // frequently used jQuery objects - cache area
  const $card_container = $('#card__container');

  // event listener for validating form submission
  $card_container.on('submit');

  // on submit action
  //   grab all values from form elements
  //   check values if they match specific condition
  //   if any are invalid, let use know, then return false

  /* Sample Code
  function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
  } */

  /* Sample HTMl
  <form name="myForm" action="/action_page.php" onsubmit="return validateForm()" method="post"> 
    Name: <input type="text" name="fname">
    <input type="submit" value="Submit">
  </form>*/
});
