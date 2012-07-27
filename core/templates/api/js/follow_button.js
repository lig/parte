{% load i18n %}
$(function() {
	//var follow_button = $('<button class="btn btn-large" id="follow_button"></button>');
	var follow_button = $('<button class="btn btn-success btn-large" id="follow_button">{% trans 'Follow' %}</button>');
	{% if user.is_authenticated %}
	follow_button.click(function(){
		alert('You are user {{ user.username }} on site {{ SITE.domain }} viewing ' + document.location.href);
	});
	{% endif %}
	$('#follow_button_container').html(follow_button);
})
