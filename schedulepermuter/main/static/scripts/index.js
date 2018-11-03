function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

$(document).ready(function() {

    $(document).on('click', '.slot', function () {
        document.getElementById("myForm").style.display = "block";
	});

    /*
	  This adds a new slot for courses
	  It first makes an ajax call to retrieve the slot id
	  Then it adds the slot to the list, basing the name off the id
    */
	$(document).on('click', '#add_slot', function () {

		url = $('#meta').attr('add_slot_url');

		//$('<li> <div class="slot" form_id="slot_form_5"><p>Slot 5</p></div></li>').appendTo('#slot_list');
		
        $.ajax({
            url: url,
            data: {},
            dataType: 'json',
            success: function (data) {
            	console.log("got response!!");
            	var slot_id = data['slot_id'];
                $('<li> <div class="slot" form_id="slot_form_' + slot_id + '"><p>Slot ' + slot_id + '</p></div></li>').appendTo('#slot_list');
            }
		});
		
	});

	/*
	$(document).on('click', '.slot', function () {
		//get slot_form_id from li element
		//add form li element to ul
		//load html into it

		var slot_form_id = $(this).attr('slot_form_id');
		var url = $('#meta').attr('render_slot_form_url');

		if ((!"#slot_form_" + slot_form_id).length) {
			var html = '<li id=slot_form_' + slot_form_id + '></li>'
			$(html).appendTo('#slot_form_list');
		}



		document.getElementById("myForm").style.display = "block";
	});
	*/
	
    $(".slot").hover(function (e) {
        $(this).html('<p>EDIT</p>');
    }, function (e) {
        $(this).html('<p>test</p>');
    });

});
