// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()

$('#ar-create').click(function(){

  $("#arrest_number").val(function() {
    let getRandomId = (min = 0, max = 1000000) => {
      min = Math.ceil(min);
      max = Math.floor(max);
      let num =  Math.floor(Math.random() * (max - min + 1)) + min;
      return num.toString().padStart(6, "0")
    };
          
    invoice_number = 'AR' + getRandomId()
    return invoice_number;
  });
});