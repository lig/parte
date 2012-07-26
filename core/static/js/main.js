$(function() {
	// post form
	var id_text_height = parseInt($('#id_text').css('line-height'));
	$('#id_text').focus(function() {
		$('#id_text').animate({height: id_text_height * 5 + 'px'});
	});
	$('#id_text').blur(function() {
		$('#id_text').animate({height: id_text_height + 'px'});
	});
	
	// comment form
	$('.comment-form-container a').click(function() {
		$(this).parent().children('form').show();
		$(this).hide();
		return false;
	})
})
