
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent)) {
	$('#backplate').height($(window).height() - 10);
} else {
	$('#backplate').height($(window).height() - 100);
}

$("#addressBarField").keyup(function(e) {
	if (e.keyCode == 13) {
		window.location.href = '/redirect?address=' + document.getElementById("addressBarField").value;
	}
});

$('#addressBarField').autocomplete({
	// lookup: addresses,
    serviceUrl: '/addresses',
	onSelect: function (suggestion) {
		window.location.href = '/redirect?address=' + document.getElementById("addressBarField").value;
    }
});
