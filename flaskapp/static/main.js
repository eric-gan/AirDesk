
function sendGet(route, cb) {
	var url = API_BASE_URL + route;
	$('#requests-content').append('GET ' + url);
	$('#requests-content').append('<br/>');
	$.get(url, function(data) {
		$('#responses-content').append(JSON.stringify(data) + ' (status 200)');
		$('#responses-content').append('<br/>');
		if (cb) cb(data);
	});
}

function sendPost(route, d, cb) {
	var url = API_BASE_URL + route;
	$('#requests-content').append('POST ' + url + ' ' + JSON.stringify(d));
	$('#requests-content').append('<br/>');
	$.post(url, d, function(data) {
		console.log(data)
		$('#responses-content').append('' + JSON.stringify(data) + ' (status 200)');
		$('#responses-content').append('<br/>');
		if (cb) cb(data);
	});
}

$(document).ajaxError(function(event, jqxhr, settings, error) {
	$('#responses-content').append('Error status ' + jqxhr.status + ' <br/>');
});

$(function() {
	sendGet('/counter', function(data) {
		$('#number').text(data);
	});

	$('#add').click(function() {
		sendPost('/add', {}, function() {
			sendGet('/counter', function(data) {
				$('#number').text(data);
			});
		});
	});

	$('#subtract').click(function() {
		sendPost('/subtract', {}, function() {
			sendGet('/counter', function(data) {
				$('#number').text(data);
			});
		});
	});
});
