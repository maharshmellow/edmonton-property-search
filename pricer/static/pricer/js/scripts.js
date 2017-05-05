
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



// var addresses = [
//     { value: '1708 62 Street SW'},
// {value: '33 FAIRWAY DRIVE NW'},
// ];



$('#addressBarField').autocomplete({
	// lookup: addresses,
    serviceUrl: '/addresses',
	onSelect: function (suggestion) {
		window.location.href = '/redirect?address=' + document.getElementById("addressBarField").value;
    }
});
