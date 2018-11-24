// helper function for madlibform.html page
function validateUserInput(event) {
  // grab all input tags
  const $input = $('input');

  // iterate over each input element and check if value is of min length (3)
  $input.each((idx, element) => {
    const $element = $(element);
    const valueLength = $element.val().length;
    if (valueLength < 3) {
      alert(
        'Please make sure all input values are at least 3 characters long.'
      );
      // prevent submit when values input does not meet requirement
      event.preventDefault();
      // returning false will break out of jQuery forEach loop
      return false;
    }
  });
}

// jQuery Wait for DOM ON Load
$(function() {
  // frequently used jQuery objects - cache area
  const $card_container = $('#card__container');

  // event listener to validate user input for madlibform.html input words
  $card_container.on('submit', '#word-input', validateUserInput);
});
