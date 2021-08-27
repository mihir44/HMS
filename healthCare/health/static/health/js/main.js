$(function () {
	$("form[name='contactForm']").validate({
		rules: {
			name: "required",
			category: "required",
			email: {
				required: true,
				email: true
			},
			phone: {
				required: true,
				minlength: 10,
				maxlength: 10
			},
			message: {
				maxlength: 500,
				required: true
			}
		},
		messages: {
			name: "Please enter your firstname",
			category: "Please enter the category",
			password: {
				required: "Please provide a mobile number",
				minlength: "Your mobile number must be at least 10 digits",
				maxlength: "Your mobile number should not exceed 10 digits"
			},
			email: "Please enter a valid email address",
			message: {
				required: "Please enter the message",
				maxlength: "Your message should not exceed more than 500 characters"
			}
		},
		submitHandler: function (form) {
			form.submit();
		}
	});
});
