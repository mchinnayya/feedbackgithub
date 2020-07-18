// Class definition
var KTSelect2 = function() {
    // Private functions
    var select2_remote = function() {
        $('.kt_select2').select2({
            placeholder: "--------------"
        });

        function formatRepo(repo) {
			// console.log('i am calling');
			// console.log(repo);
            if (repo.loading) return repo.text;
            if (repo.loading) return repo.text;
            var markup = "<div class='select2-result-repository clearfix'>" +
                "<div class='select2-result-repository__meta'>" +
                "<div class='select2-result-repository__title'>" + repo.text + "</div>";
            markup += "</div>";
            return markup;
        }

        function formatRepoSelection(repo) {
            $('#text_search_input').val(repo.id);
            return repo.text;
        }

        $("#patient_list").select2({
            placeholder: "Search patient",
            allowClear: true,
            ajax: {
                url: "http://127.0.0.1:8000/api/patient/",
				type: "GET",
                delay: 250,
                data: function(params) {
                    return {
                        q: params.term, // search term
                        page: params.page
                    };
                },
                processResults: function(data, params) {
                    // parse the results into the format expected by Select2
                    // since we are using custom formatting functions we do not need to
                    // alter the remote JSON data, except to indicate that infinite
                    // scrolling can be used
                    params.page = params.page || 1;

                    return {
                        results: $.map(data, function(obj) {
							return {
							  id: obj.id,
							  result: obj,
							  text: obj.first_name + " " + obj.last_name + " ( "+ obj.patient_code + " )"
							};
						  })
                    };
                },
                cache: false
            },
            escapeMarkup: function(markup) {
                return markup;
            }, // let our custom formatter work
            minimumInputLength: 2,
            templateResult: formatRepo, // omitted for brevity, see the source of this page
            templateSelection: formatRepoSelection // omitted for brevity, see the source of this page
        });

        function formatRepoForPatientDetails(repo) {
			// console.log('i am calling');
			// console.log(repo);
            if (repo.loading) return repo.text;
            if (repo.loading) return repo.text;
            var markup = "<div class='select2-result-repository clearfix'>" +
                "<div class='select2-result-repository__meta'>" +
                "<div class='select2-result-repository__title'><b>" + repo.full_name + "</b></div>"+
                "<div class='select2-result-repository__title'>Patient Code:" + repo.patient_code + "</div>"+
                "<div class='select2-result-repository__title'>Mobile: " + repo.mobile + "</div>" +
                "<div class='select2-result-repository__title'>Email: " + repo.email + "</div>";
            markup += "</div>";
            return markup;
        }
        $("#patient_details_search").select2({
            placeholder: "Search Patient By First name, Last name, Patient Code, Mobile, Email",
            allowClear: true,
            ajax: {
                url: "http://127.0.0.1:8000/api/patient/details",
				type: "GET",
                delay: 250,
                data: function(params) {
                    return {
                        q: params.term, // search term
                        page: params.page
                    };
                },
                processResults: function(data, params) {
                    // parse the results into the format expected by Select2
                    // since we are using custom formatting functions we do not need to
                    // alter the remote JSON data, except to indicate that infinite
                    // scrolling can be used
                    params.page = params.page || 1;

                    return {
                        results: $.map(data, function(obj) {
							return {
							  id: obj.id,
							  result: obj,
                              text: obj.first_name + " " + obj.last_name + " ( "+ obj.patient_code + " )",
							  full_name: obj.first_name + " " + obj.last_name,
							  patient_code: obj.patient_code,
                              mobile: obj.mobile_number,
                              email: obj.email
							};
						  })
                    };
                },
                cache: false
            },
            escapeMarkup: function(markup) {
                return markup;
            }, // let our custom formatter work
            minimumInputLength: 2,
            templateResult: formatRepoForPatientDetails, // omitted for brevity, see the source of this page
            templateSelection: formatRepoSelection // omitted for brevity, see the source of this page
        });
    }
    // Public functions
    return {
        init: function() {
            select2_remote();
        }
    };
}();

// Initialization
jQuery(document).ready(function() {
    KTSelect2.init();
});