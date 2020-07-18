// Class definition
var patient_related_form = function() {
    // Private functions
    let patient_related_js;
    patient_related_js = function () {
    var $myForm = $('.my-ajax-form')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    })

    function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        // $myForm.reset(); // reset form data
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }


    };
    // Public functions
    return {
        init: function() {
            patient_related_js();
        }
    };
}();

// Initialization
jQuery(document).ready(function() {
    patient_related_form.init();
});